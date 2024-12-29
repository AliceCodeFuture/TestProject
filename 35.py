'''4. Удаление всех цифр из строки
Задача: Напишите программу, которая удаляет из строки все цифры.
Пример ввода:
Введите строку: H3ll0 W0rld
Пример вывода:
Результат: Hll Wrld'''
'''
string = input('Введите строку: ')
for i in string:
    if i.isdigit():
        string = string.replace(i, '')
print('Результат:', string)
'''

'''
5. Подсчёт гласных и согласных
Задача: Напишите программу, которая подсчитывает количество гласных и согласных букв в строке.
Пример ввода:
Введите строку: Hello World

Пример вывода:
Гласных: 3
Согласных: 7'''
'''
string = input('Введите строку: ').lower()
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'
countV = 0
countC = 0
for i in string:
    if i in vowels:
        countV += 1
    elif i in consonants:
        countC += 1
print('Гласных:', countV)
print('Согласных:', countC)'''

''' 6. Инверсия регистра символов
Задача: Напишите программу, которая меняет регистр всех символов в строке (верхний регистр становится нижним, и наоборот).
Пример ввода:
Введите строку: Hello World!

Пример вывода:
Результат: hELLO wORLD!'''
'''
string = input('Введите строку: ')
newString = string.swapcase()
print('Результат:', newString)'''
'''
string = input('Введите строку: ')
for i in string:
    if i == i.lower():
        string = string.replace(i, i.upper())
    else:
        string = string.replace(i, i.lower())
print(string)
'''
'''
string = input('Введите строку: ')
new_s = ""
for char in string:
    if char.islower():
        new_s += char.upper()
    elif char.isupper():
        new_s += char.lower()
    else:
        new_s += char
print("Результат:", new_s)
'''

'''7. Удаление лишних пробелов
Задача: Напишите программу, которая удаляет лишние пробелы из строки (оставляет только один пробел между словами).
Пример ввода:
Введите строку:  Hello   world   from   Python  
Пример вывода:
Результат: Hello world from Python'''
'''
string = input('Введите строку: ')
newString = ' '.join(string.split())
print(newString)'''
