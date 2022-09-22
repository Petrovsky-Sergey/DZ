# Списки (List) по индексу (index)

a = [43, 54, 556, 65, 33]
b = ['Рот', 'Кот', 'Собака', 'Шифер', 'Крот', 'Потоп']

print(a[1:4])
print(a[4])
print(a[:3])
print(a[3:])
print(a[::2])

print(b[::2])

# Замена данных по индексу (для списка, доступно)
a[2] = 56
print(a)

# Удаление из списка по индексу
del a[4]
print(a)


