# stockdata_webscraping_using_beautifulsoup_request_string

This project is a Python web scraping script that collects stock data from Screener.in using the requests library and pandas.
It automates fetching multiple pages of stock listings, extracts tabular data, and saves everything into a single CSV file for further analysis.

 
 
 Features
- Scrapes 211 pages of stock data from Screener.in.
- Extracts tables directly from HTML using pandas.read_html.
- Adds a Page column to track the source page of each row.
- Handles errors gracefully (skips failed pages or missing tables).
- Saves the final dataset into a CSV file (all_stocks_data.csv).



Output
The script generates:
all_stocks_data.csv


containing all stock rows across pages, with columns from Screener.in plus an extra Page column.


 Requirements
Make sure you have the following installed:
- Python 3.8+
- Libraries:
- pandas
- requests
- lxml (required by pandas.read_html)
Install dependencies:
pip install pandas requests lxml




 Usage
Run the script:
python screener_scraper.py


This will:
- Loop through pages 1 → 211.
- Fetch each page with a User-Agent header (to mimic a browser).
- Extract the stock table using pandas.read_html.
- Append results into a list.
- Concatenate all tables into a single DataFrame.
- Save the final dataset into all_stocks_data.csv.

How It Works (Step by Step)
- Setup: Define base URL, page range, output file, and headers.
- Loop Pages: Iterate through each page number, format URL, and send request.
- Check Response: Skip if status code ≠ 200.
- Extract Table: Use pd.read_html to parse HTML tables.
- Store Data: Add a Page column and append to list.
- Delay: Sleep 1 second between requests to avoid server overload.
- Save CSV: Concatenate all DataFrames and export to CSV.


Notes
- Be mindful of rate limits: the script uses time.sleep(1) to avoid hitting the server too aggressively.
- The structure of Screener.in pages may change, so class names or table formats might need updating in the future.
- Always respect the website’s robots.txt and scraping policies.

Would you like me to also add a Troubleshooting section (e.g., handling ValueError: No tables found or connection errors) so your README helps beginners run it smoothly?
