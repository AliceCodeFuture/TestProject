'''
1

n=int(input())
count=0
for x in range(1,n):
    count+=x
    print(x)

    if count>100:
        print('сумма чисел больше 100 =', (count))
        break
print('работа цикла завершена')
'''


'''
2

sum_count=0
while sum_count>=0:
    n = int(input('введите число: '))
    if n==0:
        print('0!')
        print('Сумма введенных чисел: ',sum_count)
        break
    else:
        sum_count+=n
print('цикл завершен')
'''


'''
3

n=int(input())
for x in range(1,11):
    print(f'{n}*{x}={n*x}')

вариант 2
 
n=int(input())
count=0
while count<=9:
    count+=1
    print(f'{n}*{count}={n * count}')
'''

'''
4

a,b=int(input()),int(input())
print((-b)/a)
'''
