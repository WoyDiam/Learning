# імпорт необхідних функцій і константи pi з бібліотеки math
from math import (
    pi, cos, sin, sqrt, e
)


# функція, яка приймає два значення типу int або float і повертає float
def equation(x_variable: int, t_variable: int) -> float:
    return round(
        (
                ((9 * pi * t_variable) + (10 * cos(x_variable))) / (sqrt(t_variable) - abs(sin(t_variable))
                                                                    ) * e ** x_variable), 2
    )


with open('../ex_2/answers.txt', 'r') as file:
    str_file = file.read()  # Read the content of the file into a string
    int_file = int(str_file.strip())  # Convert the string to an integer


# first_numer, second_numer = map(int, input().split())  # map ( type, variable.split())
print(equation(int_file, 1))  # print() тому як функція повертає значення, але нічого не виводить
