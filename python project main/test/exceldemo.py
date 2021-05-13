import sqlite3
import time
from pyexcel_xls import save_data
from pyexcel_xls import read_data
import xlsxwriter as xw
con=sqlite3.connect('D:\\python_code\\project\\python project main\\test\\data1.db')
print('connected...')
wb=xw.Workbook("time.xls")
sh=wb.add_worksheet("record list")
time1=time.time()
time2=time.ctime(time1)
sql=("""insert into timerecord(time)
    values('{}');""".format(time2))
cursor=con.cursor()
cursor1=con.cursor()
cursor.execute(sql)
con.commit()
print('inserted')
cursor=con.execute('select * from timerecord;')
row=1
for r in cursor:
    (r[0])
    print(r)
    

#    for q in range(len(r)):
#        sh.write(row,q,r[q])
#    row=row+1
#print('successfully written')
#con.close()
#wb.close()
