print('введите первое число')
num_1 = input()
if num_1.isdigit():
    num_1 = int(num_1)
else:
    print('некорректный ввод')

print('введите арифметическую операцию: +, -, *, /')
action = input()
if action not in '+-*/':
    print('некорректный ввод')

print('введите второе число')
num_2 = input()
if num_2.isdigit():
    num_2 = int(num_2)
else:
    print('некорректный ввод')

if action == '+':
    print('результат:', num_1 + num_2)
elif action == '-':
    print('результат:', num_1 - num_2)
elif action == '*':
    print('результат:', num_1 * num_2)
elif action == '/' and num_2 != 0:
    print('результат:', num_1 / num_2)
elif action == '/' and num_2 == 0:
    print('на 0 делить нельзя!')