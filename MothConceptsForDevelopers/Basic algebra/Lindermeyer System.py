import turtle

# Функция за прилагане на L-система
def apply_rule(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(rules.get(symbol, symbol) for symbol in result)
    return result

# Функция за рисуване на L-система
def draw_l_system(commands, angle, length):
    stack = []
    for command in commands:
        if command == 'F':  # Напред
            turtle.forward(length)
        elif command == '+':  # Завой на дясно
            turtle.left(angle)
        elif command == '-':  # Завой на ляво
            turtle.right(angle)

# Основни параметри на L-системата
axiom = "F"  # Начален низ
rules = {  # Правила за заместване
    "F": "F+F-F-F+F"
}
iterations = 4  # Колко пъти да се приложат правилата
angle = 90  # Ъгъл на завой
length = 5  # Дължина на линията

# Настройка на чертежа с Turtle
turtle.speed(0)  # Ускорява рисуването
turtle.penup()
turtle.setpos(-200, 100)
turtle.pendown()

# Приложи правилата за заместване
commands = apply_rule(axiom, rules, iterations)

# Начало на рисуването
draw_l_system(commands, angle, length)

# Завършване на чертежа
turtle.done()
