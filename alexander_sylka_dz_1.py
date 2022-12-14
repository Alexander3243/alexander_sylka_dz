"""
1. Дані два цілих числа. Виведіть значення найменшого.
"""

a = int(input())
b = int(input())

if a > b:
    print(b)
else:
    print(a)

"""
2. Задано дві клітинки шахівниці. Якщо вони пофарбовані в один колір, виведіть слово YES, а якщо в різні кольори - то NO. 
Програма отримує на вхід чотири числа від 1 до 8 кожне, що задають номер стовпця та номер рядка спочатку для першої 
клітини, потім для другої клітини.
"""

column_1 = int(input())
line_1 = int(input())
column_2 = int(input())
line_2 = int(input())

if column_1 % 2 == 0 and line_1 % 2 != 0 or column_1 % 2 != 0 and line_1 % 2 == 0:
    cell_1 = "white"
else:
    cell_1 = "black"

if column_2 % 2 == 0 and line_2 % 2 != 0 or column_2 % 2 != 0 and line_2 % 2 == 0:
    cell_2 = "white"
else:
    cell_2 = "black"

if cell_1 == cell_2:
    print("YES")
else:
    print("NO")

"""
3. Якщо вводиться температура в градусах за шкалою Цельсія, вона переводиться в температуру за шкалою Фаренгейта. 
Або навпаки: температура за Фаренгейтом переводиться в температуру за Цельсієм.
"""

# Так как мы не знаем какой тип температуры будет вводится, то на вход принимаем строку с буквой в конце.
# С - цельсий, F - фаренгейт

t = input()

if t[-1] == 'F':
    t = int(t[0:-1])
    print(round(5 / 9 * (t - 32), 2))
elif t[-1] == 'C':
    t = int(t[0:-1])
    print(round(9 / 5 * t + 32, 2))

"""
4. Зі списку випадкових чисел,визначити та вивести на екран непарні числа.
"""

# cписок чисел принимается в виде строки например: 2019834579083574
# непарными числами считаем те числа, которых в списке будет меньше 2-х

nums = [int(i) for i in input()]

for i in nums:
    if nums.count(i) < 2:
        print(i)

"""
5. Вводиться ціле число, що означає код символу за таблицею ASCII. 
Визначити, це код англійської літери або будь-який інший символ.
"""
num = int(input())

if num in range(65, 91) or num in range(97, 123):
    print("Буква:", chr(num))
else:
    print("Символ:", chr(num))

"""
6. Вводяться два цілих числа. Перевірити чи ділиться перше на друге. 
Вивести на екран повідомлення про це, а також залишок (якщо він є) та приватне (у будь-якому випадку).
"""

# немного непонятно условие, будем считать, что первое число должно делится на второе без остатка
num1 = int(input())
num2 = int(input())

if num1 % num2 == 0:
    print("num1 делится на num2 без остатка")
    print("частное =", num1 / num2)
elif num1 % num2 != 0:
    print("остаток от деления num1 на num2 =", num1 % num2)
    print("частное =", num1 / num2)

"""
7. По черзі вводиться 5 цифр, вивести їхню суму (скориставшись for)
"""
result = int()

for i in range(5):
    result += int(input())

print(result)

"""
8. Дано два цілих числа A і B. 
Виведіть усі числа від A до B включно, в порядку зростання, якщо A < B, або в порядку убування інакше.
"""

A = int(input())
B = int(input())

if A < B:
    while A <= B:
        print(A)
        A += 1
elif A > B:
    while A >= B:
        print(A)
        A -= 1

"""
9. Циклом for вивести ромб:
                    *
                   * *
                  * * *
                 * * * *
                * * * * *
               * * * * * *
              * * * * * * *
             * * * * * * * *
            * * * * * * * * *
             * * * * * * * *
              * * * * * * *
               * * * * * *
                * * * * *
                 * * * *
                  * * *
                   * *
                    *
"""

a = 1
b = 9

for i in range(7):
    if a != 9:
        print(" " * b + " *" * a + " " * b)
        a += 1
        b -= 1

for i in range(8):
    if a != 0:
        print(" " * b + " *" * a + " " * b)
        a -= 1
        b += 1

"""
10. Порахувати суму числового ряду від 0 до 14 включно. Наприклад, 0+1+2+3+…+14
"""

print(sum(i for i in range(15)))

"""
11. Перемножити всі парні значення в діапазоні від 0 до 436
"""

for i in range(437):
    if i % 2 == 0:
        print(i)

"""
12. Задається випадкове речове число. Визначте максимальну цифру цього числа. Приклад виконання: 56.457 -> 7
"""

print(max(input()))

"""
13. Факторіалом числа n називається число 𝑛! = 1∙2∙3∙…∙𝑛. 
Створіть програму, яка обчислює фактор введеного користувачем числа. (Цикл!)
"""

num = int(input())

i = 1
factorial = 1

while i <= num:
    factorial *= i
    i += 1

print(factorial)

"""
14. Використовуючи вкладені цикли та функції print('*', end=''), print(' ', end='') та print() 
виведіть на екран прямокутний трикутник.
"""

for i in range(1, 10):
    print('*' * i)

"""
15. Користувач робить внесок у розмірі N $ строком на роки під 11.5% річних (кожний рік розмір його вкладу 
збільшується на 11,5%. Ці гроші додаються до суми вкладу, і на них наступного року також будуть відсотки). 
Написати програму , де користувач вводить аргументи a та years, і порахувати суму, яка буде на рахунку 
користувача через роки.
"""

contribution = float(input())
years = int(input())

for i in range(3):
    contribution *= 1.15

print(round(contribution, 2))

"""
16. Користувач запроваджує рік. Визначити він високосний чи ні.
"""

year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print("Високосный год")
elif year % 400 == 0 and year % 100 == 0:
    print("Високосный год")
elif year % 100 == 0:
    print("Невисокосный год ")
else:
    print("Невисокосный год ")

"""
17. Напишіть програму, яка запитує три цілі числа a, b і x і виводить True, якщо x лежить між a і b, інакше - False.
"""

a = int(input())
b = int(input())
x = int(input())

if a >= x >= b or a <= x <= b:
    print(True)
else:
    print(False)

"""
18. Дано чотири дійсні числа: x1, y1, x2, y2. обчисліть відстань між точкою (x1, y1) та (x2, y2). 
Вважайте чотири дійсні числа та виведіть результат роботи цієї функції.
"""

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

result = ((y1 - x1) ** 2 + (y2 - x2) ** 2) ** 0.5

print(result)
