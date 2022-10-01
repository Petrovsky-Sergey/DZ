# Игра "Порази цель"
import turtle

# именованные константы
SCREEN_WIDTH = 600  # ширина экрана
SCREEN_HEIGTH = 600  # высота экрана
TARGET_LLEFT_X = 100  # левая нижняя координата Х цели
TARGET_LLEFT_Y = 250  # левая нижняя координата Y цели
TARGET_WIDTH = 25  # ширина цели
FORCE_FACTOR = 30  # фактор произвольной силы
PROJECTILE_SPEED = 1  # скорость анимации снаряда
NORTH = 90  # угол северного направлени
SOUTH = 270  # угол южного направления
EAST = 0  # угол восточного направления
WEST = 180  # угол западного направления

# настроить окно
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGTH)

# настроить цель
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# центрировать черепаху
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# получить угол и силу выстрела от пользователя
angle = float(input('Введите угол выстрела снаряда: '))
force = float(input('Введите пусковую силу (1-10): '))

# расчитать растояние
distance = force * FORCE_FACTOR

# задать направление
turtle.setheading(angle)

# запустить снаряд
turtle.pendown()
turtle.forward(distance)

# снаряд поразил цель?
if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Цель поражена!')
else:
    print('Вы промахнулись.')
