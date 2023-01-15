import requests
from bs4 import BeautifulSoup
import csv


cash_flow = {}

url = "https://finance.yahoo.com/quote/AKSEN.IS/cash-flow?p=AKSEN.IS"

headers = {"User-Agent": "Chromium/1.47.171"}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")

cash_flow_fetch = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})

for t in cash_flow_fetch:
    rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
    for row in rows:
        cash_flow[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1]

with open('cash_flow.csv', mode='w') as csv_file:
    fieldnames = ['Period', 'Value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in cash_flow.items():
        writer.writerow({'Period': key, 'Value': value})
