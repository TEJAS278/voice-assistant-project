import sqlite3
import time
import random
con=sqlite3.connect('D:\\python_code\\project\\python project main\\test\\data1.db')
print('connected...')
#con.execute('''create table employee12
 #           (Empid int not null,
  #          Ename varchar(20) not null);
   #         ''')
#print('table crated')
#con.execute('''insert into employee12(Empid,Ename)
#            values(101,'tejas')''')
#con.commit()
#print('record inserted')
#print('=============================')
#cursor=con.execute('select * from employee12')
#for r in cursor:
#    print("Empid:",r[0],"\nEname:",r[1])
time1=time.time() #time in code
#print(time1)
time2=time.ctime(time1) #convert code to normal
#print(time2)
#con.execute('''create table timerecord
 #           (time varchar(50));
 #           ''')
#print('table crated')
#sql=("""insert into timerecord(time)
#   values('{}');""".format(time2))
cursor=con.cursor()
#cursor.execute(sql)
con.commit()
#print('inserted')
#cursor=con.execute('select * from timerecord;')
#for r in cursor:
    
    #print(time2)
#print('=======================================')
#print(time2)
#con.execute('''create table logrecord
 #           (query varchar(50),time varchar(50));
  #          ''')
cursor=con.execute('select * from logrecord;')
for j in cursor:
    print("query:",j[0],"\ntime:",j[1])
print("record")

#con.execute('''create table qa
#            (id int,response varchar(20));
 #           ''')
#con.execute('''insert into qa(id,response)
 #           values(1,'hiii'),(2,'hello');''')
con.commit()
#print('inserted')
#cursor=con.execute('select * from qa;')
#for r in cursor:
#    print("id",r[0],"resp",r[1])
con.execute('''create table files
            (id int auto_increment primary key,file_data longblob,date datetime);
            ''')
