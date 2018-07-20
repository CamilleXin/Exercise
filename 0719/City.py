#！usr/bin/env python

__author__ = 'Camille'
'''
data from city.txt to city.py

'''

from openpyxl import Workbook
import json


wb = Workbook()
sheet = wb.active

with open('city.txt', 'r', encoding='utf-8') as c:
    cities = json.loads(c.read())
key = []
value = []
for i in cities:
    key.append(i)
    value.append(cities[i])
res = list(zip(key, value))
for r in res:
    sheet.append(r)
wb.save('test2.xlsx')




