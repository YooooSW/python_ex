import json

# card=[{'name':'홍길동','address':'광주','tel':'111-2222-3333','email':'hong@naver.com'}, 
#       {'name':'김놀부','address':'부산','tel':'111-2222-3333','email':'kim@naver.com'}]
card = []

with open('01_basic/namecard.data','r') as f:
    card = json.load(f)

while True:
    menu = input('''
--------------------------------------------
1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
--------------------------------------------
>>> ''')
    if menu == '1':
        while True:
            name = input('이름을 입력하세요 >>> ')
            check = 0
            for item in card:
                if item['name'] == name:
                    check = 1
            if check == 0:
                    break
            print('중복되는 이름이 있습니다.')
                
        address = input('주소를 입력하세요 >>> ')
        tel = input('전화번호를 입력하세요 >>> ')
        email = input('이메일을 입력하세요 >>> ')
        card.append({'name':name, 'address':address, 'tel':tel, 'email':email})
        print(card)
            
    elif menu == '2':
        name = input('수정할 데이터 이름 >>>')
        foundok = -1
        for i, item in enumerate(card):
            if item['name'] == name:
                foundok = i

                while True:
                    update = input('수정할 정보 - address,tel,email,exit(종료) >>> ')
                    if update in ('address', 'tel', 'email'):
                        card[foundok][update] = input(f'{update}수정내용 >>> ')
                    elif update == 'exit':
                        break

                print(card[foundok])
                break
        if foundok == -1:
            print('등록되지 않은 이름입니다.')

    elif menu == '3':
        name = input('삭제할 이름을 입력하세요. >>> ')
        delok = 0
        for i, item in enumerate(card):
            if item['name'] == name:
                print(item, '삭제!!')
                del card[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 데이터 입니다.')

    elif menu == '4':
        for item in card:
            print(f'''
-------------------------------------------
    이    름 : {item['name']}
    주    소 : {item['address']}
    전화번호 : {item['tel']}
    이 메 일 : {item['email']}

            ''')
    elif menu == '5':
        name = input('검색할 이름을 입력하세요. >>> ')
        foundok = -1
        for i, item in enumerate(card):
            if item['name'] == name:
                foundok = i
                print(item)
                break
        if foundok == -1:
            print('등록되지 않은 이름입니다.')

    elif menu in ('6','Q','q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')

with open('01_basic/namecard.data','w') as f:
    json.dump(card,f,indent=2)