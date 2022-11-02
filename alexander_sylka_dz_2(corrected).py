"""
11.Перевірити, чи є в послідовності дублікати.
"""
sequence = [1, 35, 6, 7, 8, 14, 53, 3, 2]

if len(sequence) == len(set(sequence)):
    print("Дубликатов нет")
else:
    print("Ecть дубликаты")

"""
14. Напишіть програму, яка запропонує користувачеві ввести десяткове число у межах від 1 до 10. Програма повинна
вивести версію римського числа. Програма має враховувати ситуацію, якщо введене число є за межами діапазону від 1 до 10.
"""
# Римские числа в которых должно быть верхнее подчеркивание, будут отображаться как числа с апострофом
#Вариант 1
arabic = input()
n_arabic = int(arabic)
rome = ""

ROMAN_NUMBERS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
                 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC", 100: "C",
                 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M",
                 2000: "MM", 3000: "MMM", 4000: "MV'", 5000: "V'", 6000: "V'M", 7000: "V'MM", 8000: "V'MMM",
                 9000: "MX'", 10000: "X'", 20000: "X'X'", 30000: "X'X'X'", 40000: "X'L'", 50000: "L'", 60000: "L'X'",
                 70000: "L'X'X'", 80000: "L'X'X'X'", 90000: "X'C'", 100000: "C'", 200000: "C'C'", 300000: "C'C'C'",
                 400000: "C'D'", 500000: "D'", 600000: "D'C'", 700000: "D'C'C'", 800000: "D'C'C'C'", 900000: "C'M'",
                 1000000: "M'"}

for i in range(len(arabic)):
    if int(arabic) == 1000000:
        rome += ROMAN_NUMBERS[int(arabic)]
        arabic = arabic[1:]
    elif 100000 <= int(arabic) < 1000000:
        rome += ROMAN_NUMBERS[int(arabic[0]) * 100000]
        arabic = arabic[1:]
    elif 10000 <= int(arabic) < 100000:
        rome += ROMAN_NUMBERS[int(arabic[0]) * 10000]
        arabic = arabic[1:]
    elif 1000 <= int(arabic) < 10000:
        rome += ROMAN_NUMBERS[int(arabic[0]) * 1000]
        arabic = arabic[1:]
    elif 100 <= int(arabic) < 1000:
        rome += ROMAN_NUMBERS[int(arabic[0]) * 100]
        arabic = arabic[1:]
    elif 10 <= int(arabic) < 100:
        rome += ROMAN_NUMBERS[int(arabic[0]) * 10]
        arabic = arabic[1:]
    elif 1 <= int(arabic) < 10:
        rome += ROMAN_NUMBERS[int(arabic)]

print(rome)


#Вариант 2
arabic = int(input())

ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
dozens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands = ["", "M", "MM", "MMM", "MV'", "V'", "V'M", "V'MM", "V'MMM", "MX'"]
dozens_thousands = ["", "X'", "X'X'", "X'X'X'", "X'L'", "L'", "L'X'", "L'X'X'", "L'X'X'X'", "X'C'"]
hundreds_thousands = ["", "C'", "C'C'", "C'C'C'", "C'D'", "D'", "D'C'", "D'C'C'", "D'C'C'C'", "C'M'"]
million = ["", "M'"]

m = million[arabic // 1000000]
h_t = hundreds_thousands[arabic // 100000 % 10]
d_t = dozens_thousands[arabic // 10000 % 10]
t = thousands[arabic // 1000 % 10]
h = hundreds[arabic // 100 % 10]
d = dozens[arabic // 10 % 10]
o = ones[arabic % 10]

print(m + h_t + d_t + t + h + d + o)


"""
22. Дано натуральне число n (1 ≤ n ≤ 9999), що визначає вартість товару в копійках.
Подайте вартість у гривнях і копійках. Якщо у результаті виходить 0 копійок, то замість цього значення
необхідно записати порожній рядок.
"""

n = int(input())

if n % 100 == 0:
    print(f"Стоимость: {int(n / 100)} грн")
else:
    print(f"Стоимость: {int(n / 100)} грн, {int(n % 100)} коп")

"""
23. Дано трицифрове ціле число. Визначити суму першої і останньої цифр числа і порівняти її із
значенням другої цифри числа. Відповідно вивести повідомлення: >, < і =.
"""

number = input()

n1 = int(number[0])
n2 = int(number[1])
n3 = int(number[2])

if n1 + n3 > n2:
    print(">")
elif n1 + n3 < n2:
    print("<")
elif n1 + n3 == n2:
    print("=")

"""
31. Є список будь-яких чисел. Зробити словник в якому будуть два ключі "+" і "-" , значенням ключа "+" - сума
всіх додатніх елементів , "-" - від'ємних
"""

#Вариант 1
list_numbers = [-1, 433, 6, 7, -10, -134, 6, 1]

positive_numbers = 0
negative_numbers = 0

for i in list_numbers:
    if i > 0:
        positive_numbers += i
    else:
        negative_numbers += i

dict_numbers = {"+": positive_numbers, "-": negative_numbers}

#Вариант 2
list_numbers = [-1, 433, 6, 7, -10, -134, 6, 1]

dict_numbers = {"+": sum(list(filter(lambda x: x > 0, list_numbers))),
                "-": sum(list(filter(lambda x: x < 0, list_numbers)))}