# эта программа преобразует скорости от 60
# до 130 км/ч (с шагом в 10км) в mph

START_SPEED = 60  # начальная скорость
END_SPEED = 201  # конечная скорость
INCREMENT = 10  # приращивание скорости
CONVERSION_FACTOR = 0.6214  # коэффициент пересчета

# напечатать заголовки таблицы
print('KMH\t MPH')
print('----------')

# напечатать скорости
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t {mph:.1f}')
#