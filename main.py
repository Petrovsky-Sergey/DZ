# x = 48
# print(x % 4 != 0)
#
# a = 5
# b = 6
# print(a > 0 and b < 9)
#
# a = 57
# print(a % 10 == 7)
#
# a = 'Hello'
# print((a + ' ') * 5)
#
# s = input()
# print('Вы ввели', len(s), 'символов')
# print('я' in s)


# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, ' color of rainbow is ', color, sep='')
#     i += 1


# str = 'ABCDEFGHIJK'
# print(str[:])  # весь список
# print(str[::2])  # нечетные по порядку элементы
# print(str[1::2])  # четные по порядку элементы
# print(str[::-1])  # все элементы в обратном порядке
# print(str[5:])  # все элементы начиная с шестого
# print(str[:5])  # все элементы не доходя до шестого
# print(str[-2:1:-1])  # все элементы от предпоследнего до третьего в обратном порядке


# A_SCORE = 90
# B_SCORE = 80
# C_SCORE = 70
# D_SCORE = 60
# score = int(input('Введите свои баллы: '))
# if score >= A_SCORE:
#     print('Ваш уровень - А')
# elif score >= B_SCORE:
#     print('Ваш уровень - В')
# elif score >= C_SCORE:
#     print('Ваш уровень - С')
# elif score >= D_SCORE:
#     print('Ваш уровень - D')
# else:
#     print('Ваш уровень - F')


number = int(input())
if number == 1:
    print('Один')
elif number == 2:
    print('Два')
elif number == 3:
    print('Три')
else:
    print('Неизвестное')
