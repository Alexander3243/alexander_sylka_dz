def is_triangle(side):
    a = side[0]
    b = side[1]
    c = side[2]

    if a + b >= c and a + c >= b and b + c >= a and 0 not in side:
        return a, b, c
    return False


def triangle(area):
    if is_triangle(area):
        a, b, c = is_triangle(area)
        p = (a + b + c) / 2
        s = pow(p * (p - a) * (p - b) * (p - c), 0.5)
        return '%.2f' % s
    return "triangle does not exist"


def circle(area):
    r_circle = area[0]
    PI = 3.14
    s = PI * r_circle ** 2
    return '%.2f' % s


def rectangle(area):
    side1 = area[0]
    side2 = area[1]
    s = side1 * side2
    return '%.2f' % s


figure = input()
numbers = list(map(int, input().split()))

if figure == "triangle":
    print(triangle(numbers))
elif figure == "circle":
    print(circle(numbers))
elif figure == "rectangle":
    print(rectangle(numbers))
else:
    print("Enter the correct name figure")
