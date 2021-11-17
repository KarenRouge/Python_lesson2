month_number = (int(input("Введите номер месяца: ")))
if 1 < month_number > 12:
    month_number = (int(input("Вы ввели некорректное число. Введите число от 1 до 12: ")))
month = ["year", "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
k=0
loop_counter = 0
while month_number != month.count(k):
        month.pop(0)
        month_number = month_number - 1
        loop_counter += 1
month_number = month.count(k)
n = 12 - loop_counter
while int(len(month)) > 1:
    month.pop(n)
    n = n - 1
print("Месяц, соответсвующий Вашему числу: ", month)









