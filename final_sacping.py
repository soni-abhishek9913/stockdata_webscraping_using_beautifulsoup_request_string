import pandas as pd
import requests
import time
from io import StringIO

base_url = "https://www.screener.in/screens/71064/all-stocks/?page={}"
start_page = 1
end_page = 211   
output_file = "all_stocks_data.csv"

all_data = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for page in range(start_page, end_page + 1):
    url = base_url.format(page)
    print(f"Fetching Page {page} -> {url}")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f" Failed page {page} | Status: {response.status_code}")
        continue

 
    dfs = pd.read_html(StringIO(response.text))

    if len(dfs) == 0:
        print(f" No table found on page {page}")
        continue

    df = dfs[0]
    df["Page"] = page
    all_data.append(df)

    time.sleep(1)

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv(output_file, index=False)
    print(f"\n Saved {len(final_df)} rows into '{output_file}'")
else:
    print("\n No data extracted.")
