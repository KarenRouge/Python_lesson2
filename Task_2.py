numbers = list(map(str, input("Введите несколько любых чисел через пробел: ").split()))
print(numbers)
k = 0
for i in range(k+1):
    print("было", numbers)
    numbers[k], numbers[i] = numbers[i], numbers[k]
    print("стало", numbers)
    k = k + 2
    






