import book

book.create_table()
while True:
    prompt = '''
--------------------------------------------------------------------------
1. 책정보 등록 2. 책 수정 3. 책정보 삭제 4. 책 리스트 출력 5. 검색 6. 종료
--------------------------------------------------------------------------
 >>> '''
    menu = input(prompt)
    if menu == '1':
        try:
            book.insert_books()
        except Exception as e:
            print(e)
    elif menu == '2':
        print(book.update_book())
    elif menu == '3':
        print(book.delete_book())
    elif menu == '4':
        print(book.all_books())
    elif menu == '5':
        print(book.big_books())
    elif menu == '6':
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')
