import sqlite3
import time
con=sqlite3.connect('D:\\python_code\\project\\python project main\\main\\log.db')
print('connected...')
#con.execute('''create table logrecord
 #           (query varchar(50),time varchar(50));
 #           ''')
#cursor=con.execute('select * from logrecord;')
#for j in cursor:
#    print("query:",j[0],"\ntime:",j[1])
#con.execute('''create table resp
 #           (response varchar(20));
 #           ''')
#con.execute('''insert into resp(response)
#             values('boring'),('hey'),('nice');''')
#con.commit()
#cursor=con.execute('select * from resp;')
#for r in cursor:
#    print(r)    
cursor=con.execute('select * from logrecord;')
for j in cursor:
    print("query:",j[0],"\ntime:",j[1])
print("record")
