import pandas as pd
import numpy as np
import os

for i in range(2017, 2022):
    for n in range(1,13):
        
        # 更改原始資料檔案名稱
        rawPath = f'C:/MRT_raw/{i-1911}_raw'
        f_oldname = os.path.join(rawPath, f"臺北捷運每日分時各站OD流量統計資料_{i}0{n}.csv")
        f_newname = os.path.join(rawPath, f"MRT_{i}_{n}.csv")
        if n > 9:
            f_oldname = os.path.join(rawPath, f"臺北捷運每日分時各站OD流量統計資料_{i}{n}.csv")
            f_newname = os.path.join(rawPath, f"MRT_{i}_{n}.csv")
        os.rename(f_oldname, f_newname)
        
        # 資料處理
        df = pd.read_csv(rawPath + f"/MRT_{i}_{n}.csv")
        df['出站'] = df['出站'].str.replace("BL板橋","板橋")
        df['出站'] = df['出站']+"站"
        df['出站'] = df['出站'].str.replace("台北車站站","台北車站")
        df['出站'] = df['出站'].str.replace("大橋頭站站","大橋頭站")
        df[['年','月','日']] = df.日期.str.split('-',expand=True)
        df = df.reindex(columns=['年','月','日','時段','進站','出站','人次'])
        df_new = df.groupby(['出站','年','月','日','時段'], as_index=False).agg({'人次':sum})
        
        # merge 捷運各站編號
        mrtId = "C:/MRT_raw/Bike_MRT_MinDist.xlsx"
        df_xls = pd.read_excel(mrtId)
        df_mrtId = df_xls[["車站名稱","車站編號"]]
        df_mrt = df_mrtId.merge(df_new, left_on="車站名稱",right_on="出站" )
        df_mrtFinal = df_mrt[['車站編號','出站','年','月','日','時段','人次']]
        
        # 寫入
        path = f'C:/MRT/{i-1911}'
        if not os.path.isdir(path):
            os.makedirs(path)
        df_mrtFinal.to_csv(path + f'/MRT_{i-1911}_{n}.csv',index=False)