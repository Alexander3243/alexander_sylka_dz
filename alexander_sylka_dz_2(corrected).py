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

ROMAN_NUMBERS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
                 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC", 100: "C",
                 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M"}

a = "1155"
result = int("365235")  # CCCLXVCCXXXV-365235 LXVCCXXXV-65235 VCCXXXV-5235 CCXXXV-235 XXXV-35 v-5
rome_number = ""
for i in range(len(str(result))):
    if result >= 1000:
        print(int(str(result)[0] + (len(str(result)) - 1) * "0"))
        rome_number += ROMAN_NUMBERS[int(str(result)[0] + (len(str(result)) - 1) * "0")]
        result %= int(str(result)[0] + (len(str(result)) - 1) * "0")
    elif 100 <= result <= 1000:
        rome_number += ROMAN_NUMBERS[100]
        result %= 100
    elif 10 <= result <= 100:
        rome_number += ROMAN_NUMBERS[10]
        result %= 10
    elif 1 <= result <= 10:
        rome_number += ROMAN_NUMBERS[result]

print(rome_number)

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