# 도서관리 프로그램
# 데이터 구조는 리스트를 이용
# 일련번호(중복x), 책이름, 출판사, .....
# 1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
import bookcard as bc

bookcard = None

while True:
    menu = input('''
-----------------------------------------------------------------------
1.book저장 2.book수정 3.book삭제 4.book내용 보기 5.전체목록 보기 6.종료
-----------------------------------------------------------------------
>>> ''')
    if menu == '1':
        if bookcard == None:
            print('bookcard 생성한 후 추가 가능합니다.')
        else:
            num = input('일련번호 >>> ')
            name = input('책이름 >>> ')
            publi = input('출판사 >>> ')
            price = input('책가격 >>> ')
            card = bc.Book(num,name,publi,price)
            bookcard.add_card(card)

    elif menu == '2':
        pass

    elif menu == '3':
        if bookcard == None:
            print('bookcard 생성한 후 추가 가능합니다.')
        else:
            print(list(bookcard.books.key()))
            number = int(input('삭제할 일련번호 >>> '))
            card = bookcard.remove_card(number)
            print(number, '->삭제')

    elif menu == '4':
        if bookcard == None:
            print('bookcard 생성한 후 추가 가능합니다.')
        else:
            print(list(bookcard.books.keys()))
            number = int(input('page number >>> '))
            book = bookcard.cards[number]
            print(book)

    elif menu == '5':
        if bookcard == None:
            print('bookcard 생성한 후 추가 가능합니다.')
        else:
            key = input('정렬 키(입력값:num,name,publi,price) >>> ')
            sort = bool(input('오름차순(enter),내림차순(1) >>>'))
            # print(sort,type(sort))
            if key in ('num','name','publi','price'):
                bookcard.list_cards(key,sort)
            else:
                bookcard.list_cards(reverse=sort)

    elif menu in ('6','Q','q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')