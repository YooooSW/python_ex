# 도서관리 프로그램
# 데이터 구조는 리스트를 이용
# 일련번호(중복x), 책이름, 출판사, .....
# 1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
import json

import bookfunc as bf
book = []

while True:
    menu = input('''
--------------------------------------------
1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
--------------------------------------------
>>> ''')
    if menu == '1':
        bf.save(book)
    elif menu == '2':
        bf.update(book)
    elif menu == '3':
        bf.delete(book)
    elif menu == '4':
        bf.booklist(book)
    elif menu == '5':
        bf.search(book)
    elif menu in ('6','Q','q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')