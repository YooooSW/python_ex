<<<<<<< HEAD
# f = open('01_basic/test.txt','r',encoding='cp949')
# # print(type(f))
# text = f.read()
# print(text)
# f.close()

# with open('01_basic/test.txt','r',encoding='cp949') as f:
#     while True:
#         text = f.readline()
#         if not text:
#             break
#         print(text)

# with open('01_basic/test_w.txt','w',encoding='utf8') as f:
#     f.write('첫줄 입력\n')

import pickle

card=[{'name':'홍길동','address':'광주','tel':'111-2222-3333','email':'hong@naver.com'}, 
       {'name':'김놀부','address':'부산','tel':'111-2222-3333','email':'kim@naver.com'}]

# f = open('01_basic/pickledata.pickle','wb')
# pickle.dump(card,f)
# f.close()

# with open('01_basic/pickledata.pickle','rb') as f:
#     data = pickle.load(f)
#     print(data)

import json

# with open('01_basic/jsontest.json', 'w') as f:
#     json.dump(card,f,indent=2)

with open('01_basic/jsontest.json', 'r') as f:
    data = json.load(f)
    print(type(data))
=======
# f = open('01_basic/test.txt','r',encoding='cp949')
# # print(type(f))
# text = f.read()
# print(text)
# f.close()

# with open('01_basic/test.txt','r',encoding='cp949') as f:
#     while True:
#         text = f.readline()
#         if not text:
#             break
#         print(text)

# with open('01_basic/test_w.txt','w',encoding='utf8') as f:
#     f.write('첫줄 입력\n')

import pickle

card=[{'name':'홍길동','address':'광주','tel':'111-2222-3333','email':'hong@naver.com'}, 
       {'name':'김놀부','address':'부산','tel':'111-2222-3333','email':'kim@naver.com'}]

# f = open('01_basic/pickledata.pickle','wb')
# pickle.dump(card,f)
# f.close()

# with open('01_basic/pickledata.pickle','rb') as f:
#     data = pickle.load(f)
#     print(data)

import json

# with open('01_basic/jsontest.json', 'w') as f:
#     json.dump(card,f,indent=2)

with open('01_basic/jsontest.json', 'r') as f:
    data = json.load(f)
    print(type(data))
>>>>>>> origin/master
    print(data)