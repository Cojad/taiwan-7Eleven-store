import os
import httpx
import yaml
from bs4 import BeautifulSoup

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    all_stores = {}

    with httpx.Client(base_url="https://www.ibon.com.tw") as client:
        # 取得城市列表
        res = client.get("/retail_inquiry.aspx")
        cities = [opt.text.strip() for opt in BeautifulSoup(res.text, "html.parser").select("#Class1 option")]
        
        print(f"正在處理 {len(cities)} 個城市...")

        for city in cities:
            print(f"處理城市: {city}")
            res = client.post("/retail_inquiry_ajax.aspx", data={"strTargetField": "COUNTY", "strKeyWords": city})

            # 儲存原始回應以便除錯
            filename = city.replace("/", "_")
            with open(os.path.join(SCRIPT_DIR, f"{filename}.html"), "w", encoding="utf-8") as f:
                f.write(res.text)
            print(f"  已儲存 {filename}.html")

            # 只選擇 store_table 中的 tr，排除表頭和其他 tr
            table = BeautifulSoup(res.text, "html.parser").select_one("table.font16")
            if not table:
                print(f"  找不到表格，繼續下一個城市")
                continue
            print(f"  找到表格，有 {len(table.select('tr'))} 行")

            all_stores.update({
                cols[0].text.strip(): {
                    "store": cols[1].text.strip(),
                    "address": cols[2].text.strip()
                }
                for row in table.select("tr")
                if row.get("style") and (cols := row.select("td")) and len(cols) >= 3
            })
            print(f"  完成，已處理 {len([r for r in table.select('tr') if r.get('style')])} 筆店鋪")

    # 儲存為 YAML，allow_unicode 確保中文不亂碼，sort_keys=False 保持插入順序 (Python 3.7+)
    with open(os.path.join(SCRIPT_DIR, "stores.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(all_stores, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print(f"完成。已將 {len(all_stores)} 筆資料寫入 stores.yaml")

if __name__ == "__main__":
    main()