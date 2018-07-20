# ！usr/bin/env python

__author__ = 'Camille'
'''
data from student.txt to test1.xlsx
'''
from openpyxl import Workbook
import json

# new_excel = os.getcwd() + os.sep+ "test1.xlsx"
# print(new_excel)
wb = Workbook()
sheet = wb.active
sheet.title = 'sheet1'
with open('student.txt', encoding='utf-8') as s:
    student = json.loads(s.read())
for i in student:
    student[i].insert(0, i)
    sheet.append(student[i])
wb.save('test1.xlsx')
