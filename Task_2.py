numbers = list(input("Введите несколько любых чисел через пробел: ").split())
for i in range(len(numbers)//2):
    print("было", numbers)
    a = 2*i
    b = a+1
    if b < len(numbers):
        numbers[a], numbers[b] = numbers[b], numbers[a]
    print("стало", numbers)




