import oracledb
oracledb.init_oracle_client()

def create_table():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = '''
            create table employee(
                empid number primary key,
                name varchar2(20),
                gender varchar2(10),
                tel varchar2(20),
                age number(4),
                work varchar2(10),
                daytime number(4),
                nighttime number(4)
            )
            '''
            try:
                cur.execute(sql)
            except Exception as e:
                print(e)

def insert_emp():
    with oracledb.connect('SCOTT/TIGER@localgost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = 'insert into employee values(empcard_seq.NEXTVAL,:1,:2,:3,:4,:5,:6,:7)'
            name = input('')

# def drop_table():
#     with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
#         with conn.cursor() as cur:
#             sql = '''
#             drop table employee
#             '''
#             try:
#                 cur.execute(sql)
#             except Exception as e:
#                 print(e)

if __name__ == '__main__':
    create_table()
    # drop_table()