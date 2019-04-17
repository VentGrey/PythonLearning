#!/usr/bin/env python

import math


def dist_calc(x1: float, x2: float, y1: float, y2: float):
    D = math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
    return D




X1 = float(input("Ingrese el valor de X1: "))
Y1 = float(input("Ingrese el valor de Y1: "))
X2 = float(input("Ingrese el valor de X2: "))
Y2 = float(input("Ingrese el valor de Y2: "))
X3 = float(input("Ingrese el valor de X3: "))
Y3 = float(input("Ingrese el valor de Y3: "))

perim = dist_calc(X1,X2,Y1,Y2) + dist_calc(X2,Y2,X3,Y3) + dist_calc(X3,Y3,X1,Y1)
areatot = area(X1,X2,Y1,Y2,X3,Y3)
print(perim)
print((1/2) * abs(X1 * (Y2 - Y3) + X2 * (Y3 - Y1) + X3 * (Y1 - Y2)))
