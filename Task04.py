# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число в десятичной системе исчисления: '))
my_bin = ''
while number > 0:
    my_bin = str(number % 2) + my_bin
    number = number // 2
print(my_bin)
