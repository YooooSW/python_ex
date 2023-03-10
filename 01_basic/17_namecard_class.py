# 클래스 Card,  CardBook
# --------------------------------------------------------------------------------
# 1.CardBook 생성 2.Card 추가 3.Card 삭제 4.Card 내용 보기 5.전체목록 보기 6.종료
# --------------------------------------------------------------------------------
# >>> ''')

import namecard as nc
import pickle, os

path = os.path.dirname(__file__)
# print(__file__)
# print(path)
cardbook = None

with open('01_basic/cardbook.pickle', 'rb') as f:
    cardbook = pickle.load(f)

while True:
    menu = input('''
--------------------------------------------------------------------------------
1.CardBook 생성 2.Card 추가 3.Card 삭제 4.Card 내용 보기 5.전체목록 보기 6.종료
--------------------------------------------------------------------------------
>>> ''')
    if menu == '1':
        if cardbook == None:
            cardbook = nc.CardBook(input('타이틀을 입력하세요.'))
        else:
            print('생성된 cardbook이 존재합니다.')
    elif menu == '2':
        if cardbook == None:
            print('cardbook 생성한 후 추가 가능합니다.')
        else:
            name = input('이름을 입력하세요 >>> ')
            address = input('주소를 입력하세요 >>> ')
            tel = input('전화번호를 입력하세요 >>> ')
            email = input('이메일을 입력하세요 >>> ')
            card = nc.Card(name,address,tel,email)
            cardbook.add_card(card)
    elif menu == '3':
        if cardbook == None:
            print('cardbook 생성한 후 추가 가능합니다.')
        else:
            print(list(cardbook.cards.keys()))
            page = int(input('page number >>> '))
            card = cardbook.remove_card(page)
            print(card, '-> 삭제')
    elif menu == '4':
        if cardbook == None:
            print('cardbook 생성한 후 추가 가능합니다.')
        else:
            print(list(cardbook.cards.keys()))
            page = int(input('page number >>> '))
            card = cardbook.cards[page]
            print(card)
    elif menu == '5':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            key = input('정렬 키(입력값:name,address,tel,email) >>> ')
            sort = bool(input('오름차순(enter),내림차순(1) >>>'))
            # print(sort,type(sort))
            if key in ('name','address','tel','email'):
                cardbook.list_cards(key,sort)
            else:
                cardbook.list_cards(reverse=sort)
    elif menu == '6':
        print('프로그램 종료')
        break


with open('01_basic/cardbook.pickle','wb') as f:
    pickle.dump(cardbook,f)
