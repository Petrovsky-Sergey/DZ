# res = 1
# for i in range(1, 4):
#     res *= i
# print(res)
#
# res = 1
# for i in range(1, 5):
#     res *= i
# print(res)
#
# res = 1
# for i in range(1, 6):
#     res *= i
# print(res)


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(factorial(3))
print(factorial(5))
