# эта программа сравнивает строковые значения оператором <
# получить от пользователя два имени
name1 = input('Введите фамилию и имя: ')
name2 = input('Введите еще дну фамилию и имя: ')

# показать имена в алфавитном порядке
print('Вот имена, ранжированные по алфавиту: ')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)