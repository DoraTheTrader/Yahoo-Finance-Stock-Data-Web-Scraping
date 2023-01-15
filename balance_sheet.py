import requests
from bs4 import BeautifulSoup
import csv


balance_sheet = {}

url = "https://finance.yahoo.com/quote/AKSEN.IS/balance-sheet?p=AKSEN.IS"

headers = {"User-Agent" : "Chromium/1.47.171"}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")

balance_sheet_fetch = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})

for t in balance_sheet_fetch:
    rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
    for row in rows:
        balance_sheet[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1]

with open('balance_sheet.csv', mode='w') as csv_file:
    fieldnames = ['Period', 'Value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in balance_sheet.items():
        writer.writerow({'Period': key, 'Value': value})