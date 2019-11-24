
import pymysql.cursors

conn = pymysql.connect(host='localhost',
        user='ktw',
        password='12345678',
        db='testDB')

cursor=conn.cursor()
sql = 'INSERT INTO pulse (datas) VALUES (%s)'
cursor.execute(sql, 3)
conn.commit()
conn.close()
