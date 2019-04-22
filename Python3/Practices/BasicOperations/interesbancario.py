#!/usr/bin/env python

MD = float(input("Ingrese el monto de dinero que depositará "))
TASA = float(input("Ingrese la tasa de interés mensual\
que le cobrarán (en decimales) "))

print("Al final de lmes usted tendrá un total de: ", MD + (MD / TASA ))
