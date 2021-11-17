my_list = [7, 6, 4, 4, 3, 2, 2, 2, 1]
your_number = int(input('Введите целое натуральное число'))
i=0
while your_number < my_list[i]:
    i = i + 1
my_list.insert(i, your_number)
print(my_list)