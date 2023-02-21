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
    part text,
    time integer)
    ''')
    conn.commit()
    conn.close()
# 직원정보입력
def insert_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'insert into employee(name,gender,tel,age,work,part,time,salary) values(?,?,?,?,?,?,?)'
    name = input('이름 ')
    gender = input('성별 ')
    tel = input('전화번호 ')
    age = input('나이 ')
    work = input('직무 ')
    part = input('주간,야간 ')
    time = input('시간 ')
    cur.execute(sql,(name,gender,tel,age,work,part,time))
    conn.commit()
    conn.close()
insert_emp()

# 직원전체정보조회
def all_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'select * from employee'
    cur.execute(sql)
    for item in cur.fetchall():
        print(item)
    conn.close()
# all_emp()

#직원정보수정
def update_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    all_emp()
    name = input('수정할 직원이름')
    check = 1
    while check:
        col = input('수정할 정보(gender,tel,age,work,part)')
        if col in ('gender','tel','age','work','part'):
            check = 0
    value = input(f'{col}수정할 내용 입력')
    sql = f'update employee set {col} = ? where name = ?'
    cur.execute(sql,(value,name))
    conn.commit()
    conn.close()
# update_emp()

# def update_time():

#삭제할 직원
def delete_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    all_emp()
    name = input('삭제할 직원 ')
    sql = 'delete from employee where name = ?'
    cur.execute(sql,[name])
    conn.commit()
    conn.close()
# delete_emp()

# def addtime_emp():
#     conn = sqlite3.connect(path + '/empinfo.db')
#     cur = conn.cursor()
#     all_emp()
#     total_time = []
#     name = input('시간입력할 직원이름 ')
#     check = 1
#     while check:

#     sql = 'update employee set'
    
# def salary():
#     conn = sqlite3.connect(path + '/empinfo.db')
#     cur = conn.cursor()
#     sql = 'alter table employee add column salary integer'
#     cur.execute(sql)
#     conn.commit()
#     conn.close()
# salary()


# create_table()
# insert_emp()
# drop_table()