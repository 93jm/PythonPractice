def func(test):
    helper = 9

    def func2(test):
        return helper * test

    return func2(test)


func(7)


# def decorator1(func):
#     def wrapper():
#         print('decorator1')
#         func()
#     return wrapper


# def decorator2(func):
#     def wrapper():
#         print('decorator2')
#         func()
#     return wrapper

# # 데코레이터를 여러 개 지정


# @decorator1
# @decorator2
# def hello():
#     print('hello')


# hello()


# def what_is_my_full_name(**kwargs):
#     result = kwargs
#     print(result)
#     for i in result:
#         if i == 'last_name'():
#             print(i)


# what_is_my_full_name(first_name='우성', last_name='정')
# def get_occurrence_count(my_list):
#     result_dict = {}
#     for i in my_list:
#         if i not in result_dict.keys():
#             result_dict[i] = 1
#         else:
#             result_dict[i] += 1
#     return result_dict


# get_occurrence_count(["one", 2, 3, 2, "one"])


# testdic = {
#     '이름': '이정민',
#     '나이': 29,
#     '성별': '남자',
#     '성격': '굿'
# }

# for i in testdic.values():
#     print(i)

# for i, j in testdic.items():
#     print(f'{i}는 {j}에요')
