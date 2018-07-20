#！usr/bin/env python

__author__ = 'Camille'

'''
data from numbers.txt to test3.xlsx

'''
from openpyxl.workbook import Workbook
import json


wb = Workbook()
sheet = wb.active
with open('numbers.txt', 'r', encoding='utf-8') as n:
    numbers = json.loads(n.read())
    for number in numbers:
        sheet.append(number)
wb.save('test3.xlsx')

