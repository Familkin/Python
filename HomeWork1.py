# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input("Введи номер дня недели:"))
# if a == 6 or a == 7:
#     print("Да")
# else:
#     print("Нет")


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введи x:"))
y = int(input("Введи y:"))

if x==0 or y == 0:
    print("Значения не могут быть нулевыми")
elif x > 0 and y > 0:
    print(1)
elif x>0 and y <0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x<0 and y>0:
    print(4)





    # Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
    # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

    # Пример:

    # - A (3,6); B (2,1) -> 5,09
    # - A (7,-5); B (1,-1) -> 7,21
