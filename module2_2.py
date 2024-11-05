first = int(input('Введите число больше 10:'))
second = int(input('Введите число,которое делится на 3:'))
third = int(input('Введите целое число:'))
if first != second != third:
    print(0)
elif first == second and second == third:
    print(2)
else: ('Числа не равны между собой')
