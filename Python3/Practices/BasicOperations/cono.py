#!/usr/bin/env python

PI:float = 3.1415

RAD = float(input("Ingrese el radio del cono "))
ALT = float(input("Ingrese la altura del cono "))
GEN = float(input("Ingrese la generatriz del cono "))

print("El área de la base del cono es: ", PI * (RAD ** 2))
print("El área lateral es: ", PI * RAD * GEN)
print("El área total es: ", (PI * (RAD ** 2)) +  (PI * RAD * GEN))
print("El volumen del cono es: ", (1/3) * (PI * (RAD ** 2)) * ALT)
