print()
# 람다(Lambda)함수
# 단일문으로 표현되는 익명함수
# 코드 상에서 한 번만 사용되는 기능이 있을 때 굳이 함수로 만들지 않고 1회성으로 만들어서 사용


# def square(x):
#     return x**2


# print(square(5))


# # 람다식 변형
# square = lambda x: x**2
# print(type(square))
# print(square(5))


# def add(x, y):
#     return x + y


# print(add(15, 2))
# print()

# add = lambda x, y: x + y

# print(add(15, 2))


# 리스트 구조
# 문자의 길이가 짧은 순서대로 정렬하고 싶음
# def str_len(s):
#     return len(s)


# strings = ["bob", "charles", "alexander3", "teddy"]
# # strings.sort(key=str_len)
# strings.sort()  # 오름차순 정렬 후 출력
# # 괄호안에 바로 람다식 입력 가능
# strings.sort(key=lambda s: len(s))
# print(strings)


# filter, map, reduce : 함수형 프로그래밍

# 리스트를 넘겨받아 짝수만 모아서 새로운 리스트로 반환
list1 = [1, 2, 3, 6, 8, 9]
even_list = []  # 새로운 리스트 even_list = list()


# def even(list1):
#     for i in list1:
#         if i % 2 == 0:
#             even_list.append(i)


# even(list1)
# print(even_list)


# def even(n):
#     return n % 2 == 0


# # filter() : 특정 조건을 가지고 있는 함수를 담음.
# print(list(filter(even, list1)))

# # 람다직접입력
# print(list(filter(lambda n: n % 2 == 0, list1)))


# 리스트를 받아 제곱을 한 숫자로 새로운 리스트 생성
# nums = [1, 2, 3, 6, 8, 10, 11, 12, 13, 14, 15]


# def mul(n):
#     return n**2


# print(list(map(mul, nums)))
# print(list(map(lambda n: n**2, nums)))


# 주어진 리스트에서 3의 배수만 문자열로 변경해서 돌려받기
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_result = []


# str(), int(), float(), bool(), list(),tuple(),dict(),set()
def str_check(nums):
    for i in nums:
        if i % 3 == 0:
            num_result.append(str(i))
        else:
            num_result.append(i)


def str_check(num):
    if num % 3 == 0:
        return str(num)
    else:
        return num


num_result = list(map(str_check, nums))
print(num_result)
num_result = list(map(lambda num: str(num) if num % 3 == 0 else num, nums))

print(num_result)  # [1, 2, '3', 4, 5, '6',..]
print()
