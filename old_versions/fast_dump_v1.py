#!/usr/bin/env python3

import requests
import time

page_num = 1
price_data = ''

while True:
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(page_num))
    if req.status_code == 200:
        price_data += '\n' + req.text
    else:
        price_data += "API error"
    print("... getting page "+str(page_num))
    page_num += 1
    if req.text == "":
        break

with open('.data/{}_full_output.py'.format(int(time.time())), 'a') as f1:
    f1.write('\n'+ price_data)


price_data_format1 = price_data.replace(',','\n')
with open('.data/{}_lines_removed.py'.format(int(time.time())), 'a') as f2:
    f2.write('\n' + price_data_format1)


price_data_format2 = price_data_format1.split('\n')
with open('.data/{}_xyxy.py'.format(int(time.time())), 'a') as f3:
    f3.write(str(price_data_format2))

prices = price_data_format2[::2]
k=1
with open('.data/{}_prices.py'.format(int(time.time())), 'a') as f4:
    while k<len(prices):
        f4.write('{!r}\n'.format(prices[k]))
        k+=1

timestamps = price_data_format2[1::2]
j=1
with open('.data/{}_stamps.py'.format(int(time.time())), 'a') as f5:
    while j<len(timestamps):
        f5.write('{!r}\n'.format(timestamps[j]))
        j += 1

