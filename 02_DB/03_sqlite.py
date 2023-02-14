import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
# select * from stocks where symbol = 'rhat'
symbol = input('종목이름을 입력하세요 >>> ')
# sql = "select * from stocks where symbol = '%s'" % symbol
sql = "select * from stocks where symbol = :1"  # ? or :1 가능
cur.execute(sql,(symbol,))
print(cur.fetchone())
conn.close()

# [] 리스트 [원하는데이터]
# () 튜플 데이터가하나 (원하는데이터,) 한개일때는, 나머진 상관X

# 데이터 검색