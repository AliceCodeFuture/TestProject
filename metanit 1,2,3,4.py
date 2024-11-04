'''
print('Введите год')
year = int(input())
if year % 4 == 0 or (year % 400 == 0 and year % 100 == 0):
    if year % 100 == 0 and year%400!=0:
        print('этот год не является високосным')   #  номер 1
    else:
         print('этот год является високосным')
else:
    print('этот год не является високосным')
 '''


'''
print('введите первое число')
a = int(input())
print('введите второе число')
b = int(input())
if a > b:
    print('Наибольшее число:', a)  #  номер 2
elif a == b:
    print('числа равны:', a)
else:
    print('Наибольшее число:', b)
'''


'''
print('введите первое число')
a = int(input())
print('введите второе число')  #  номер 3
b = int(input())
c = a if a > b else b
print('Наибольшее число:', c)
'''



'''
print('Введите сумму продажи:')
sum = int(input())
if sum <= 5000:
    print('Скидка:', sum * 0.05)
    print('Сумма с учетом скидки :', sum - sum * 0.05)
elif 5000 < sum <= 15000:
    print('Скидка:', sum * 0.12)
    print('Сумма с учетом скидки :', sum - sum * 0.12)  #  номер 4  
elif 15000 < sum <= 25000:
    print('Скидка:', sum * 0.2)
    print('Сумма с учетом скидки :', sum - sum * 0.2)
else:
    print('Скидка:', sum * 0.3)
    print('Сумма с учетом скидки :', sum - sum * 0.3)
'''
