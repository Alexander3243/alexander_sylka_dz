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