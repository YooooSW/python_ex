import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
sql = 'insert into stocks values(?,?,?,?,?)'
# data = ('2023-01-08','buy','ibm',1000,45.00)
# cur.execute(sql,data)
data = [('2023-01-08','buy','ibm',1000,45.00),
        ('2023-02-11','sell','ibm',500,48.00),
        ('2023-03-08','buy','mstf',400,72.00),
        ('2023-07-20','buy','rhat',120,37.00),
        ('2023-11-08','sell','rhat',150,45.00)]
cur.executemany(sql,data)
conn.commit()
conn.close()

# 데이터 입력