#!/usr/bin/env python

import math


X1 = float(input("Ingrese el valor de X1"))
Y1 = float(input("Ingrese el valor de Y1"))
X2 = float(input("Ingrese el valor de X2"))
Y2 = float(input("Ingrese el valor de Y2"))
X3 = float(input("Ingrese el valor de X3"))
Y3 = float(input("Ingrese el valor de Y3"))


def distance_calculator(x1: float, x2: float, y1: float, y2: float):
    D = math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
