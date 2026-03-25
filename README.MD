# Taiwan 7-Eleven Store Scraper

## Overview
這個專案提供台灣 7-Eleven 門市列表爬蟲，可直接利用已抓取的 `stores.yaml` 清單快速使用。

- 最新資料版本：2026/03/25 (7277筆)
- 參考文章：[iThome - 使用爬蟲取得 7-11 門市清單](https://ithelp.ithome.com.tw/articles/10193779)

## Project Structure
```
.
├─ 711.py           # 爬蟲程式
├─ stores.yaml      # 最新7-11全台門市資料 7277 筆 (2026/03/25)
└─ requirements.txt # 依賴
```

## Usage
1. 若不需要最新資料 `stores.yaml` 內為最後更新日期時的門市資料。
2. 若需重新爬取，執行 `python 711.py`，結果將會輸出覆蓋 `stores.yaml`。

## Notes
- 使用非公開 API 請保持禮貌，避免造成伺服器負擔。
- 請勿過度大量呼叫，建議對資料做好快取與重用。
- 若需長期使用，建議定期重新抓取以更新門市資訊。
- 爬蟲行為需遵循相關網站使用規範與法律。

## License
資料來源為台灣 7-Eleven 官方網站，請依照原服務條款使用；

