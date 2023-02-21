import sqlite3,os

path = os.path.dirname(__file__)

def create_table():
    conn = sqlite3.connect(path + '/test.db')
    cur = conn.cursor()
    cur.execute('''
    create table employee(
    empid integer primary key autoincrement,
    name text,
    gender text,
    tel text)
    ''')
    conn.commit()
    conn.close()

def insert_emp():
    conn = sqlite3.connect(path + '/test.db')
    cur = conn.cursor()
    sql = 'insert into employee values(?,?,?,?)'
    name = input('이름 ')
    gender = input('성별 ')
    tel = input('전화번호 ')
    cur.executemany(sql,(name,gender,tel,))
    conn.commit()
    conn.close()


# create_table()
insert_emp()
# drop_table()
# insert_emp()