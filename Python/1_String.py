import math


print('----------------')

print(','.join(['a', 'b', 'cde']))

print('----------------')

departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)
print(_)
print(arrival)

print('----------------')

print('인덱스형 format')

print("Name: {}, Age: {}".format("철수", 13))

print("Name: {0}, Age: {1}".format("영희", 15))

print("Name: {0}, Age: {1}: {0}의 나이가 {1}".format("민호", 17))

print('키워드형 format')

print("Name: {name}, Age: {age}: {name}의 나이가 {age}".format(age=19, name='재석'))

print('리스트로 넘기고 index로 접근형 format')

pos = [12.5, 35, 90]
print("A의 좌표는 x = {p[0]}, y = {p[1]}, z = {p[2]}".format(p=pos))

print('모듈로 넘겨 활용하는 format')

print('수학에서 파이= {m.pi}'.format(m=math))

print('----------------')

s = "  abc   "
print(s.strip())

print('----------------')

length = len('1234567')
print(length)

print('----------------')
