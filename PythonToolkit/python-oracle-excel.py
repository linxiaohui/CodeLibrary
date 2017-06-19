# -*- coding:UTF-8 -*-

# Python读取Oracle写入Excel模板的示例程序

import cx_Oracle
import xlrd
import xlwt
from xlutils.copy import copy
import xlwt
import datetime
import calendar
import os

tns=cx_Oracle.makedsn(os.environ['ORACLEHOST'],1521,os.environ['ORACLE_SID'])
db=cx_Oracle.connect(os.environ['DCUSERNAME'],os.environ['DCPASSWORD'],tns)
cr=db.cursor()


# 获取上月最后一天的日期
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
print('上月最后一日的日期为:',lastMonth)

# 获取上个周一/周五的日期
preFriday = datetime.date.today()
oneday = datetime.timedelta(days=1)
while preFriday.weekday() != calendar.FRIDAY:
    preFriday -= oneday

# 上周四日期
preThursday = preFriday-oneday

preMonday = preFriday
while preMonday.weekday() != calendar.MONDAY:
    preMonday -= oneday

holdSQL="""select to_date(%s,'YYYYMMDD') from dual where dummy like 'X%%'"""%(lastMonth.strftime('%Y%m%d'))
print(holdSQL)
cr.execute(holdSQL)
rs=cr.fetchall()

template="模板.xls"
resultName="%04d%02d%02d.xls"%(preFriday.year,preFriday.month,preFriday.day)

# 导出数据
# wb = xlwt.Workbook()
# ws = wb.add_sheet('')
rb = xlrd.open_workbook(template,formatting_info=True)
rsheet = rb.sheet_by_index(0)
wb = copy(rb)
wsheet = wb.get_sheet(0)

font = xlwt.Font() 
font.name = 'Segoe UI'
font.bold = True
font.height = 180
styleHeader = xlwt.XFStyle()
styleHeader.font = font
row = 0

style = xlwt.easyxf("font:name 宋体,height 240",num_format_str="¥#,##0.00;¥-#,##0.00")
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
style.borders = borders

style2 = xlwt.easyxf("font:name 宋体,height 240")
style2.borders = borders

style3 = xlwt.easyxf("font:name 宋体,height 240", num_format_str="#,##0.00")
style3.borders = borders

# 打印首行
col = 1
for h in cr.description:
    ws.write(row, col, h[0], styleHeader)
    col+=1
row+=1

style = []
# A
style.append(xlwt.easyxf("font:name Segoe UI,height 180"))
# B
style.append(xlwt.easyxf("font:name Segoe UI,height 180", num_format_str="0.0000"))

for r in rs:
    ws.write(row, 0, row, style[0])
    col=1
    for c in r:
        ws.write(row, col, c, style[col])
        col+=1
    row+=1

wb.save(resultName)
