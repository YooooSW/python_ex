import sqlite3,os

path = os.path.dirname(__file__)

def create_table():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    cur.execute('''
    create table employee(
    empid integer primary key autoincrement,
    name text,
    gender text,
    tel text,
    age integer,
    work text,
    part text)
    ''')
    conn.commit()
    conn.close()
# create_table()

def create_table2():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    cur.execute('''
    create table jobtime(
    name text,
    time integer,
    date timestamp default current_timestamp)
    ''')
    conn.commit()
    conn.close()
# create_table2()

def insert_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'insert into employee(name,gender,tel,age,work,part) values(?,?,?,?,?,?)'
    name = input('이름 ')
    gender = input('성별 ')
    tel = input('전화번호 ')
    age = input('나이 ')
    work = input('직무 ')
    part = input('주간,야간 ')
    cur.execute(sql,(name,gender,tel,age,work,part))
    conn.commit()
    conn.close()
# insert_emp()

def insert_jobtime():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'insert into jobtime(name,time) values(?,?)'
    name = input('이름 ')
    time = input('시간 ')
    cur.execute(sql,(name,time))
    conn.commit()
    conn.close()
insert_jobtime()