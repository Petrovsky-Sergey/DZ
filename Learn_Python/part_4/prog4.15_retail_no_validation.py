# этарограмма вычисляет розличные цены
MARK_UP = 2.5  # процент надбавки
another = 'y  '# переменная управления циклом

# обрабатывать один или несколько товаров
while another == 'y' or another == 'Y':
    # получить оптовую стоимость товара
    wholesale = float(input('Введите оптовую стоимость товара: '))
    
    # вычислить розничную цену
    retail = wholesale * MARK_UP

    # показать розничную цену
    print(f'розничная цена: ${retail:,.2f}')

    # повторить?
    another = input('Есть еще один товар? (Введите y, если да): ')
