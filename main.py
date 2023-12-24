import numpy as np
import matplotlib.pyplot as plt

a = float(input("1: Линейная функция(y=kx+b), 2: Квадратичная функция(y=ax^2+bx+c), 3:Кубическая функция(y=ax^3+bx^2+cx+d), 4: Гипербола(y=k/x) "))
if a == 1:
    k = float(input("Введите коэффициент k "))
    b = float(input("Введите b "))
    y = lambda x: k * x + b
elif a == 2:
    k = float(input("Введите коэффициент a "))
    b = float(input("Введите коэффициент b "))
    c = float(input("Введите коэффициент c "))
    y = lambda x: k * x ** 2 + b * x + c
elif a == 3:
    k = float(input("Введите коэффициент a "))
    b = float(input("Введите коэффициент b "))
    c = float(input("Введите коэффициент c "))
    d = float(input("Введите коэффициент d "))
    y = lambda x: k * x ** 3 + b * x ** 2 + c * x + d
elif a == 4:
    k = float(input("Введите коэффициент k "))
    y = lambda x: k / x
else:
    print("Выберите предложенное из списка число!")
x = np.linspace(-10, 10, 10000)
plt.plot(x, y(x))
plt.show()
