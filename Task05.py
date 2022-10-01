# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] '

N = int(input('k = '))
my_list1 = [1, -1]
for i in range(2, N):
    my_list1.append(my_list1[i - 2] - my_list1[i - 1])
my_list1.reverse()
my_list2 = [0, 1, 1]
for i in range(3, N+1):
    my_list2.append(my_list2[i - 2] + my_list2[i - 1])
my_list = my_list1 + my_list2
print(my_list)
