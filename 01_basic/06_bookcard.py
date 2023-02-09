<<<<<<< HEAD
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
=======
# 도서관리 프로그램
# 데이터 구조는 리스트를 이용
# 일련번호(중복x), 책이름, 출판사, .....
# 1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)

book = [['11', '오렌지나무', '큰나무', '13000원'],
        ['12', '감나무', '작은나무', '14000원']]

while True:
    menu = input('''
--------------------------------------------
1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
--------------------------------------------
>>> ''')
    if menu == '1':
        while True:
            num = input('일련번호를 입력하세요 >>>')
            check = 0
            for item in book:
                if item[0] == num:
                    check = 1
            if check == 0:
                break
            print('중복되는 일련번호')
        
        name = input('책이름을 입력하세요. >>>')
        publisher = input('출판사를 입력하세요. >>>')
        price = input('책가격을 입력하세요. >>>')
        book.append([num,name,publisher,price])
        print(book)

    elif menu == '2':
        num = input('수정할 일련번호 >>>')
        for i, item in enumerate(book):
            if item[0] == num:
                numok = i
                update = int(input('수정할 정보(1.책이름, 2.출판사, 3.가격)>>>'))
                book[numok][update] = input('수정내용 >>>')
                print(book[numok])
                break
        if numok == -1:
            print('등록되지 않은 번호입니다.')

    elif menu == '3':
        num = input('삭제할 일련번호를 입력하세요. >>>')
        delok = 0
        for i, item in enumerate(book):
            if item[0] == num:
                print(item, '삭제!!')
                del book[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 데이터입니다.')

    elif menu == '4':
        for item in book:
            print(f'''
-------------------------------------------
    일련번호 : {item[0]}
    책 이 름 : {item[1]}
    출 판 사 : {item[2]}
    책 가 격 : {item[3]}

            ''')
    elif menu == '5':
        num = input('검색할 번호을 입력하세요. >>>')
        numok = -1
        for i, item in enumerate(book):
            if item[0] == num:
                numok = i
                print(item)
                break
        if numok == -1:
            print('등록되지 않은 번호입니다.')

    elif menu in ('6','Q','q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')
>>>>>>> origin/master
