#функция проверки введенного числа на корректность, возвращает число с плавающей точкой:
def check_num_input(x):
    while not x.replace('.', '', 1).lstrip('-').isdigit():
        x = input('Некорректный ввод. Введите число: ')
    return float(x)

#функция проверки доступных операций:
def check_action(x):
    while x not in '+-/*':
        x = input('Допускаются только: +, -, *, /. Повторите ввод: ')
    return str(x)

# 4 функции самих операций:
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multy(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print('На 0 делить нельзя!')
        return 'как-нибудь в другой раз.'
    else:
        return a / b

#словарь операций, вызывающий нужную функцию:
actions = {'+': plus, '-': minus, '*': multy, '/': divide}

#ввод значений:
a = check_num_input(input('Введите первое число: '))
d = check_action(input('Введите арифметическую операцию: '))
b = check_num_input(input('Введите второе число: '))

#вывод результата с использованием словаря операций:
print('Результат:', actions[d](a, b))
