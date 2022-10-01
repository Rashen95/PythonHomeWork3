# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

amount = int(input('Сколько чисел будет в вашем списке?: '))
my_list = []
for i in range(amount):
    my_list.append(float(input(f'Введите {i} элемент списка: ')))
print('Ваш список', my_list)
my_max = my_list[0] - int(my_list[0])
my_min = my_list[0] - int(my_list[0])
for i in range(1, len(my_list)):
    if my_list[i] - int(my_list[i]) > my_max:
        my_max = my_list[i] - int(my_list[i])
    else:
        my_min = my_list[i] - int(my_list[i])
print(round(my_max - my_min, 5))
