# Списки и их методы

s = 'Hello'
print(s.upper())

a = [23, 56, 34, 78, 54, 9, 100]
print(a)

a.append('Serega')
print(a)

print(a.count(78))  # Сколько раз встречается в списке
print(a.index(78))  # Узнать индекс числа в списке
print(a.pop(7))  # Удаление из списка по индексу
print(a.sort())
print(a)