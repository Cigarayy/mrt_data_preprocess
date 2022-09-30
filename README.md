# mrt_data_preprocess

必須先將臺北捷運每日分時各站OD流量統計資料從政府公開資料平台上下載 \
https://data.taipei/api/dataset/63f31c7e-7fc3-418b-bd82-b95158755b4d/resource/eb481f58-1238-4cff-8caa-fa7bb20cb4f4/download

程式碼以2017年至2022年為例 \
並將所需要年份以及月份依序下載並放置至以年為單位的資料夾內(程式碼內需改為自訂路徑，路徑很重要!!) \
Bike_MRT_MinDist.xlsx 為捷運站各站編號檔案，可用於未來合併資料時之主鍵
