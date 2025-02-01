'''
Проверка, начинается ли строка с определённой буквы
Напишите функцию, которая проверяет, начинается ли строка с определённой буквы.
Пример ввода и вывода:
Ввод: "apple", "a"Вывод: True
Ввод: "banana", "b"
Вывод: True
Ввод: "cherry", "a"Вывод: False'''

'''def check(name, symbol):
    if symbol == name[0]:
        return True
    else:
        return False


name = input()
symbol = input()
print(check(name, symbol))
'''

'''Проверка, есть ли в списке заданный элемент
Напишите функцию, которая проверяет, содержится ли определённый элемент в списке.
(Без return — просто выводит результат).
Пример ввода и вывода:
Ввод: [1, 2, 3, 4], 3Вывод: 3 есть в списке
Ввод: [1, 2, 3, 4], 5
Вывод: 5 нет в списке'''

'''def check(list_num, num):
    if num in list_num:
        print(num, 'есть в списке')
    else:
        print(num, 'нет в списке')


list_num = list(input())
num = input()
print(check(list_num, num))'''

'''Подсчёт гласных в строке
Напишите функцию, которая возвращает количество гласных в строке.
Пример ввода и вывода:
Ввод: "hello"Вывод: 2
Ввод: "python"
Вывод: 1'''

'''vowels = 'AaEeIiOoUuYy'
def check(string):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count


s = input()
print(check(s))'''

'''Удаление дубликатов из списка
Напишите функцию, которая удаляет все дубликаты из списка.
(С return).
Пример ввода и вывода:
Ввод: [1, 2, 2, 3, 4, 4, 5]Вывод: [1, 2, 3, 4, 5]'''

'''def new(numbers):
    another_list = []
    for i in numbers:
        if i not in another_list:
            another_list.append(i)
    return another_list


num = list(map(int, input().split()))
print(new(num))
'''

'''Перевёрнута ли строка является палиндромом
Напишите функцию, которая проверяет, является ли строка палиндромом, игнорируя регистр и пробелы.
(С return).
Пример ввода и вывода:
Ввод: "A man a plan a canal Panama"Вывод: True
Ввод: "hello"
Вывод: False'''

'''def check(string):
    new = string.replace(' ', '').lower()
    reversedText = new[::-1]
    if reversedText == new:
        return True
    else:
        return False


s = input()
print(check(s))'''

'''Проверка, есть ли в строке хотя бы одна цифра
Напишите функцию, которая проверяет, есть ли в строке хотя бы одна цифра.
(Без return — просто выводит результат).
Пример ввода и вывода:
Ввод: "hello123"Вывод: В строке есть цифра
Ввод: "hello"
Вывод: В строке нет цифр'''

'''def check(string):
    flag = True
    for i in string:
        if i.isdigit():
            flag = True
            break
        else:
            flag = False
    if flag:
        print('В строке есть цифра')
    else:
        print('В строке нет цифр')


s = input()
print(check(s))'''

'''Подсчёт длины каждого слова в строке
Напишите функцию, которая принимает строку и возвращает список длин каждого слова.
Пример ввода и вывода:
Ввод: "Hello world"Вывод: [5, 5]
Ввод: "Python is fun"
Вывод: [6, 2, 3]'''

'''def check(string):
    count = []
    for i in string.split():
        count.append(len(i))
    return count


s = input()
print(check(s))'''

'''Удаление слов, длина которых меньше заданного числа
Напишите функцию, которая удаляет из списка строк все слова, длина которых меньше заданного числа.
Пример ввода и вывода:
Ввод: ["cat", "elephant", "dog", "tiger"], 4Вывод: ['elephant', 'tiger']'''

'''def check(list_string, num):
    for i in list_string:
        if len(i) < num:
            list_string.remove(i)
    return list_string


s = list(map(str, input().split()))
n = int(input())
print(check(s, n))'''

'''Проверка списка на упорядоченность
Напишите функцию, которая проверяет, является ли список упорядоченным по возрастанию.
Пример ввода и вывода:
Ввод: [1, 2, 3, 4]Вывод: True
Ввод: [1, 3, 2, 4]
Вывод: False'''


'''def check(numbers):
    if numbers == sorted(numbers):
        return True
    else:
        return False


num = list(map(int, input().split()))
print(check(num))'''