#!/usr/bin/env python

from bs4 import BeautifulSoup
import openpyxl

file_name = 'output/current-holdings-india.xlsx'
workbook = openpyxl.load_workbook(file_name)
worksheet = workbook.worksheets[1]

# delete all rows except header
worksheet.delete_rows(2, worksheet.max_row - 1)

HTMLFile = open("input/groww_investment_page.html", "r")
index = HTMLFile.read()
soup = BeautifulSoup(index, "html.parser")

row_id = 0
col_id = 0
count = 0

for row in soup.find_all('tr', class_='holdingRow_stockItemHover__GWd5z'):
    symbol = row['data-holding-parent'].strip()

    if row.a != None:
        name = row.a.contents[0].string.replace('\n     ', "")
        quantity = row.span.contents[0].string.replace('\n     ', "").replace('shares', "")
        avg_buy_price_raw = row.findNext('span').findNext('span').findNext('span')
        # print(avg_buy_price_raw)
        avg_buy_price_str = avg_buy_price_raw.contents[0].replace('\n     ', "")
        avg_buy_price_float = float(avg_buy_price_str.split("₹")[1].replace(',', ''))

        row_values = symbol, quantity, avg_buy_price_float
        worksheet.append(row_values)
        count = count + 1
        print(count, symbol, name, quantity, avg_buy_price_float)
    # print(soup.prettify())
workbook.save(file_name)
workbook.close()
