import notebook as nb
import pickle
# note_1 = nb.Note('세상 사는 데 도움이 되는 명언')
# note_2 = nb.Note('삶이 있는 한 희망은 있다')

# notebook_1 = nb.NoteBook('명언노트')

# notebook_1.add_note(note_1)
# notebook_1.add_note(note_2)
# print(notebook_1.get_number_of_pages())

notebook = None
with open('notedata.pickle', 'wb') as f:
    pickle.dump(notebook, f)

while True:
    menu = input('''
-----------------------------------------------------------
1.노트북 생성 2.노트추가 3.노트삭제 4.노트내용 보기 5.종료
-----------------------------------------------------------
>>> ''')
    if menu == '1':
        if notebook == None:
            notebook = nb.NoteBook(input('타이틀을 입력하세요. >>> '))
        else:
            print('생성된 노트북이 존재합니다.')
    elif menu == '2':
        if notebook == None:
            print('노트북 생성한 후 추가 가능합니다.')
        else:
            contents = input('노트내용 >>> ')
            note = nb.Note(contents)
            notebook.add_note(note)
    elif menu == '3':
        if notebook == None:
            print('노트북 생성한 후 추가 가능합니다.')
        else:
            print(list(notebook.notes.keys()))
            page = int(input('page number >>> '))
            note = notebook.remove_note(page)
            print(note, '-> 삭제')

    elif menu == '4':
        if notebook == None:
            print('노트북 생성한 후 추가 가능합니다.')
        else:
            print(list(notebook.notes.keys()))
            page = int(input('page number >>> '))
            note = notebook.notes[page]
            print(note)

    elif menu in ('5'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')


with open('notedata.pickle', 'rb') as f:
    load_notebook = pickle.load(f)
    print(load_notebook)