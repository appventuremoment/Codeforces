from math import *

pi = 3.14159265359

def gcd(x, y) :
 
    if abs(y) < 1e-4 :
        return x
    else :
        return gcd(y, fmod(x, y))

def min_area_of_polygon(Ax, Ay, Bx, By, Cx, Cy):
    a = sqrt((Bx - Cx) * (Bx - Cx) +
        (By - Cy) * (By - Cy))
    b = sqrt((Ax - Cx) * (Ax - Cx) +
        (Ay - Cy) * (Ay - Cy))
    c = sqrt((Ax - Bx) * (Ax - Bx) +
        (Ay - By) * (Ay - By)) 

    semiperimeter = (a + b + c) / 2

    area_triangle = sqrt(semiperimeter *
                    (semiperimeter - a) *
                    (semiperimeter - b) *
                    (semiperimeter - c))

    Radius = (a * b * c) / (4 * area_triangle)

    Angle_A = acos((b * b + c * c - a * a) / (2 * b * c))
    Angle_B = acos((a * a + c * c - b * b) / (2 * a * c))
    Angle_C = acos((b * b + a * a - c * c) / (2 * b * a))

    n = pi / gcd(gcd(Angle_A, Angle_B), Angle_C)

    area = (n * Radius * Radius *
        sin((2 * pi) / n)) / 2

    return area

inp = []
for i in range(3):
    x, y = list(map(float, input().split(' ')))
    inp.append((x, y))

Ax, Ay = inp[0]
Bx, By = inp[1]
Cx, Cy = inp[2]

print(round(min_area_of_polygon(Ax, Ay, Bx, By, Cx, Cy), 6)) 