# list	mutable 한 순서가 있는 객체 집합	mutable
# set	mutable 한 순서가 없는 고유한 객체 집합	mutable
# dict	key와 value가 맵핑된 객체, 순서 없음	mutable
# bool	참,거짓	immutable
# int	정수	immutable
# float	실수	immutable
# tuple	immutable 한 순서가 있는 객체 집합	immutable
# str	문자열	immutable
# frozenset	immutable한 set	immutable

import copy
a = [1, 2, 3]
print(id(a))
# 2583026479616
a[0] = 5
print(id(a))
# 2583026479616

print('------------------')

a = [1, 2, 3]
b = a  # shallow copy
# b[0]= 5
a
# [5, 2, 3]
b
# [5, 2, 3]
id(a)
# 4396179528
id(b)
# 4396179528

print('------------------')

a = "abc"
b = a
a
# 'abc'
b
# 'abc'
id(a)
# 4387454680
id(b)
# 4387454680
b = "abcd"
a
# 'abc'
b
# 'abcd'
id(a)
# 4387454680
id(b)
# 4396456400

print('------------------')

# 얕은 복사(shallow copy)

# list의 슬라이싱을 통한 새로운 값을 할당해봅니다.
# 아래의 결과와 같이 슬라이싱을 통해서 값을 할당하면 새로운 id가 부여되며, 서로 영향을 받지 않습니다.
a = [1, 2, 3]
b = a[:]
id(a)
4396179528
id(b)
4393788808
a == b
True
a is b
False
b[0] = 5
a
[1, 2, 3]
b
[5, 2, 3]
하지만, 이러한 슬라이싱 또한 얕은 복사에 해당합니다.
리스트안에 리스트 mutable객체 안에 mutable객체인 경우 문제가 됩니다.
id(a) 값과 id(b) 값은 다르게 되었지만, 그 내부의 객체 id(a[0])과 id(b[0])은 같은 주소를 바라보고 있습니다.
a = [[1, 2], [3, 4]]
b = a[:]
id(a)
4395624328
id(b)
4396179592
id(a[0])
4396116040
id(b[0])
4396116040
재할당하는 경우는 문제가 없습니다. 메모리 주소도 변경되었습니다.
a[0] = [8, 9]
a
[[8, 9], [3, 4]]
b
[[1, 2], [3, 4]]
d(a[0])
4393788808
id(b[0])
4396116040
하지만, a[1] 에 값을 변경하면 b[1]도 따라 변경됩니다.
a[1].append(5)
a
[[8, 9], [3, 4, 5]]
b
[[1, 2], [3, 4, 5]]
id(a[1])
4396389896
id(b[1])
4396389896
copy 모듈의 copy 메소드 또한 얕은 복사입니다.
a = [[1, 2], [3, 4]]
b = copy.copy(a)
a[1].append(5)
a
[[1, 2], [3, 4, 5]]
b
[[1, 2], [3, 4, 5]]
