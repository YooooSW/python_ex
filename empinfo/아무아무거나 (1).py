worker=[{'name': '김화영', 'gender': 'F', 'tel': '010-4909-5658', 'age': '27','work':'cashier'},
           {'name': '신성혁', 'gender': 'M', 'tel': '010-1234-5678', 'age': '25','work':'kitchen'},
           {'name': '김상철', 'gender': 'M', 'tel': '010-1234-5678', 'age': '28','work':'serving'},
           {'name': '유승완', 'gender': 'M', 'tel': '010-1234-5678', 'age': '30','work':'kitchen'}]

while True:
    menu=input(
'''
-----------------------------------------
|1. 근무자 정보 입력
|2. 근무자 정보 수정
|3. 근무자 정보 조회
|4. 근무자 정보 삭제
|5. 근무자 리스트
|6. 근무자 근무시간 입력 및 수정
|7. 종료
|8. 급여 지급 기준
|9. Tmi
-----------------------------------------
'''
)
    if menu=='1':
        name=input('이름을 입력하세요:')
        gender=input('성별을 입력하세요')
        tel=input('전화번호를 입력하세요')
        age=input('나이를 입력하세요')
        work=input('직무를 입력하세요')

    elif menu=='2':
        name=input('수정할 직원의 이름>>>')
        idx=-1
        for i, item in enumerate(worker):
            if item['name']==name:
                idx=1
                while True:
                    update=input('수정할 정보 >>> gender,tel,age,work,exit(종료)')
                    if update in ('gender','tel','age','work'):
                        worker[idx][update]=input(f'{update}수정내용>>>')
                    elif update=='exit':
                        break   

                print(worker[idx])
                break     
    elif menu=='3':
        name = input('검색할 이름 >>>')
        idx = -1
        for i, item in enumerate(worker):
            if item['name'] == name:
                idx = i
                print(item[i])
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')
    elif menu == '4':
       name=input('직원 이름으로 검색>>>')
       idx=-1
       for i, item in enumerate(worker):
           if item['name'] == name:
            print(item,'삭제!')
            idx=i
            print(item)
            break
    elif menu=='5':
        name = input('검색할 이름 >>>')
        idx = -1
        for i, item in enumerate(worker):
            if item['name'] == name:
                idx = i
                print(item)
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')
    elif menu=='6':
        minimenu=int(input(''' 메뉴를 선택하세요
            1. 근무시간 입력 
            2. 근무시간 수정 '''))
        if minimenu=='1':
                name1=input('이름을 입력하세요>>>')
                day=int(input('금주 총 주간 근무 시간을 입력하세요>>>'))
                night=int(input('금주 총 야간 근무 시간을 입력하세요>>>'))
        else:
                name1=input('이름을 입력하세요>>>')
                day=int(input('수정하실 주간 근무 시간을 입력하세요'))
                night=int(input('수정하실 야간 근무 시간을 입력하세요'))

    elif menu=='7':
        print('프로그램 종료!')
    elif menu=='8':
        print(
'''
현재 서빙,캐셔는 최저시급, 주방은 최저시급의 1.2배를 지급하고 있습니다.
그리고 야간근무는 주간근무의 1.5배의 시급을 지급합니다.
주휴수당은 주 15시간 이상 근무 시 급여의 1.2배를 지급합니다.
''')    
    # elif menu=='9':
    #     if list(worker[0].keys())[4]=='kitchen':
    #         day=int(input('금주 총 주간 근무 시간을 입력하세요>>>'))
    #         night=int(input('금주 총 야간 근무 시간을 입력하세요>>>'))
    #         if day+night<15:
    #             week = (day+(night*1.5))*1.2*9620
    #             month = week*4
    #             print('%.f 원이 지급됩니다' %month)                
    #             print("{0}원으로 무엇을 할 수 있을까요?".format(month))
    #             print("PC방 (1500원 기준) : {0}시간".format(month // 1500))
    #             print("강남 24평 집 사는데 걸리는 시간 (25억원 기준) : {0}달".format(2500000000 //month ))
    #             print('급여는 매달 10일에 지급됩니다.')
    #         else:
    #             week = (day+(night*1.5))*1.2*9620*1.2
    #             month = week*4
    #             print('%.f 원이 지급됩니다' %month)
    #             print("{0}원으로 무엇을 할 수 있을까요?".format(month))
    #             print("PC방 (1500원 기준) : {0}시간".format(month // 1500))
    #             print("강남 24평 집 사는데 걸리는 시간 (25억원 기준) : {0}달".format(2500000000 //month ))
    #             print('급여는 매달 10일에 지급됩니다.')
    #     if list(worker[0].keys())[4]=='serving':
    #         day=int(input('금주 총 주간 근무 시간을 입력하세요>>>'))
    #         night=int(input('금주 총 야간 근무 시간을 입력하세요>>>'))
    #         if day+night<15:
    #             week = (day+(night*1.5))*9620
    #             month = week*4
    #             print('%.f 원이 지급됩니다' %month)
    #             print("{0}원으로 무엇을 할 수 있을까요?".format(month))
    #             print("PC방 (1500원 기준) : {0}시간".format(month // 1500))
    #             print("강남 24평 집 사는데 걸리는 시간 (25억원 기준) : {0}시간".format(2500000000 //month ))
    #             print('급여는 매달 10일에 지급됩니다.')
    #         else:
    #             week = (day+(night*1.5))*9620*1.2
    #             month = week*4
    #             print('%.f 원이 지급됩니다' %month)
    #             print("{0}원으로 무엇을 할 수 있을까요?".format(month))
    #             print("점심 (9000원 기준) : {0}끼".format(month // 9000))
    #             print("강남 24평 집 사는데 걸리는 시간 (25억원 기준) : {0}시간".format(2500000000 //month ))
    #             print('급여는 매달 10일에 지급됩니다.')
    #     if list(worker[0].keys())[4]=='cashier':
    #         day=int(input('금주 총 주간 근무 시간을 입력하세요>>>'))
    #         night=int(input('금주 총 야간 근무 시간을 입력하세요>>>'))
    #         if day+night<15:
    #             week = (day+(night*1.5))*9620
    #             month = week*4
    #             print('%.f 원이 지급됩니다' %month)
    #             print("{0}원으로 무엇을 할 수 있을까요?".format(month))
    #             print("PC방 (1500원 기준) : {0}시간".format(month // 1500))
    #             print("강남 24평 집 사는데 걸리는 시간 (25억원 기준) : {0}시간".format(2500000000 //month))
    #             print('급여는 매달 10일에 지급됩니다.')
    #         else:
    #             week = (day+(night*1.5))*9620*1.2
    #             month = week*4
    #             print('%.f 원이 지급됩니다' %month)
    #             print("{0}원으로 무엇을 할 수 있을까요?".format(month))
    #             print("PC방 (1500원 기준) : {0}시간".format(month // 1500))
    #             print("강남 24평 집 사는데 걸리는 시간 (25억원 기준) : {0}시간".format(2500000000 //month ))
    #             print('급여는 매달 10일에 지급됩니다.')