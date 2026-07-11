# Taiwan 7-Eleven Store Scraper

## Overview
這個專案提供台灣 7-Eleven 門市列表爬蟲，可直接利用已抓取的 `stores.yaml` 清單快速使用。

- 最新資料版本：2026/07/11 (7295筆) 
- 採用Github Action 每日自動更新
- 參考文章：[iThome - 使用爬蟲取得 7-11 門市清單](https://ithelp.ithome.com.tw/articles/10193779)

## Project Structure
```
.
├─ 711.py              # 爬蟲程式
├─ stores.yaml         # 最新7-11全台門市資料 7295 筆 (2026/07/11)
├─ stores.json         # 同上資料的 JSON 壓縮版（單行，適合機器讀取）
├─ stores-pretty.json  # 同上資料的 JSON 美化版（縮排 2 空白，適合人閱讀／diff）
└─ requirements.txt    # 依賴
```

## Output Formats
每次爬取會同步輸出三種格式，內容完全相同，依使用情境選用：

| 檔名 | 格式 | 適合用途 |
| --- | --- | --- |
| `stores.yaml` | YAML | 給人看、版本控制 diff 友善 |
| `stores.json` | JSON（單行壓縮） | 程式讀取、檔案最小化 |
| `stores-pretty.json` | JSON（indent=2） | 給人看、跨語言除錯 |

資料結構皆以門市編號為 key：
```json
{
  "110817": { "store": "千翔", "address": "台北市中正區許昌街17號1樓" }
}
```

## Usage
1. 若不需要最新資料，可直接使用 repo 內已生成的 `stores.yaml` / `stores.json` / `stores-pretty.json`。
2. 若需重新爬取，執行 `python 711.py`，結果將會輸出覆蓋上述三個檔案。

## Notes
- 使用非公開 API 請保持禮貌，避免造成伺服器負擔。
- 請勿過度大量呼叫，建議對資料做好快取與重用，如果你沒有特殊需求歡迎直接每日從本專案抓取最新資訊。
- 若需長期使用，建議定期重新抓取以更新門市資訊。
- 爬蟲行為需遵循相關網站使用規範與法律。

## License
資料來源為台灣 7-Eleven 官方網站，請依照原服務條款使用；

