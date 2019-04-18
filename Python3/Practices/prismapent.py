#!/usr/bin/env python

PER = float(input("Ingrese el perímetro"))
APO = float(input("Ingrese el apotema del pentágono"))
ALT = float(input("Ingrese la altura del pentágono"))

print("El área de la base es: ", (PER*APO)/2)
print("El área lateral es: ", PER * ALT)
print("El área total es: ", 2 * (PER*APO)/2 + (PER*ALT))
print("El volumen es: ", ((PER*APO)/2) * ALT)
