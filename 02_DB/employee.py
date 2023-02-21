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
                job varchar2(10)
            )
            '''
            try:
                cur.execute(sql)
            except Exception as e:
                print(e)

# def insert_emp():
#     with oracledb.connect('SCOTT/TIGER@localgost:1521/xe') as conn:
#         with conn.cursor() as cur:
#             sql = 'insert into employee values'


if __name__ == '__main__':
    create_table()