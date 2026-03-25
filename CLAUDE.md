# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案概述

Python 網頁爬蟲，從 7-Eleven 官方網站 (ibon) 抓取全台門市資料並輸出結構化 YAML 檔案。屬於 go-edpay.com 付款系統的一部分，門市資料供帳務前端做門市查詢使用。

## 常用指令

```bash
pip install -r requirements.txt   # 安裝依賴
python 711.py                     # 執行爬蟲（會覆寫 stores.yaml 及各縣市 .html 檔）
```

本專案無測試或 lint 設定。

## 運作流程

1. `711.py` 請求 `https://www.ibon.com.tw/retail_inquiry.aspx` 取得縣市列表
2. 對每個縣市 POST 至 `retail_inquiry_ajax.aspx` 取得門市清單
3. 解析 HTML 表格（`table.font16`），擷取門市編號（key）、門市名稱、地址
4. 將各縣市原始 HTML 回應存為 `{縣市}.html` 供除錯用（已 gitignore）
5. 所有門市寫入 `stores.yaml`，以門市編號（字串）為 key，包含 `store` 和 `address` 欄位

## 輸出格式（stores.yaml）

```yaml
'110817':
  store: 千翔
  address: 台北市中正區許昌街17號1樓
```

Key 為門市編號字串。目前資料集約 7,277 筆，涵蓋 23 個縣市。

## 主要依賴

- `httpx` — HTTP 客戶端
- `beautifulsoup4` — HTML 解析
- `pyyaml` — YAML 序列化

## 注意事項

- 爬蟲使用的是 ibon 非公開 API，程式內未內建速率限制，請勿密集呼叫
- HTML 檔僅供本地除錯，已透過 `.gitignore` 排除於 git 之外
- `stores.yaml` 有提交至 git，作為下游使用的快取資料集
