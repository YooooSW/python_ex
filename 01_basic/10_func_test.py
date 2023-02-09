
# def add(a,b):
#     return a+b

# def add1():
#     a = input('a=')
#     b = input('b=')
#     print(a+b)
#     return

# def add2():
#     a = input('a=')
#     b = input('b=')
#     print(a+b)
#     return a+b

# def add(a,b):
#     a = a + b
#     print('in', a)
#     return a

# a=7
# b=3
# print('out',add(a,b))
# print('out',a,b)

# def add(a,b):
#     a[0] = b
#     print('in', a)
#     return a

# a = [1,2,3]
# b = [4,5,6]
# print('out',add(a,b))
# print('out',a,b)

# def test(t):
#     print(x)
#     t = 20
#     print('in:', t)

# x = 10
# test(x)
# print('out:', x)

# 176p 5-8
# def f():
#     s = 'I love London'
#     print(s)

# s='I love Paris'
# f()
# print(s)

# 178p 5-9
# def f():
#     global s
#     s = 'I love London'
#     print(s)

# s = 'I love Paris'
# f()
# print(s)

#180p 재귀함수 5-11
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(int(input('Input Number for Factorial Calculation'))))

#디폴트인수
# def add(a,b=3):
#     return a+b

# print(add(2))

def add(**a):
    print(a)
