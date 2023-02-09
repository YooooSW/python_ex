import json

def save(book):
    while True:
        num = input('일련번호를 입력하세요 >>>')
        check = 0
        for item in book:
            if item['num'] == num:
                check = 1
        if check == 0:
            break
        print('중복되는 일련번호')
    
    name = input('책이름을 입력하세요. >>>')
    publisher = input('출판사를 입력하세요. >>>')
    price = input('책가격을 입력하세요. >>>')
    book.append({'num':num,'name':name,'publisher':publisher,'price':price})
    print(book)

def update(book):
    num = input('수정할 일련번호 >>>')
    numok = -1
    for i, item in enumerate(book):
        if item['num'] == num:
            numok = i

            while True:
                update = input('수정할 정보 - name,publisher,price,exit(종료)>>>')
                if update in ('name','publisher','price'):
                    book[numok][update] = input(f'{update}수정내용 >>>')
                elif update == 'exit':
                    break

            print(book[numok])
            break
    if numok == -1:
        print('등록되지 않은 번호입니다.')

def delete(book):
    num = input('삭제할 일련번호를 입력하세요. >>>')
    delok = 0
    for i, item in enumerate(book):
        if item['num'] == num:
            print(item, '삭제되었습니다.')
            del book[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 데이터입니다.')

def booklist(book):
    for item in book:
            print(f'''
-------------------------------------------
    일련번호 : {item['num']}
    책 이 름 : {item['name']}
    출 판 사 : {item['publisher']}
    책 가 격 : {item['price']}
            ''')

def search(book):
    num = input('검색할 번호을 입력하세요. >>>')
    numok = -1
    for i, item in enumerate(book):
        if item['num'] == num:
            numok = i
            print(item)
            break
    if numok == -1:
        print('등록되지 않은 번호입니다.')

