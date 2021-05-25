# 리스트는 순서가 있는 수정가능한 객체의 집합

a = [1, 2, 3, 4, 5]
b = list()

print(a)
print(b)

b.append(5)
print(b)

print([1, 2, 3] + [3, 2, 1])
print(set([1, 2, 3] + [3, 2, 1]))

print(list("와우"))
