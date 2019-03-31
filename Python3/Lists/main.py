# -*- coding: utf-8 -*-


"""
Las LISTAs son arreglos flexibles. Esta clase de "arreglos" contienen variables
que sean deseados y soportan TODOS los tipos de variables. Las LISTAs se indexan
desde una base cero.
"""

LISTA = []

# Agregaremos elementos a la LISTA
LISTA.append(1) # añadimos "1" a la LISTA
LISTA.append(2) # añadimos "2" a la LISTA
LISTA.append(3) # añadimos "3" a la LISTA

print LISTA[0]
print LISTA[1]
print LISTA[3]

# Imprimimos la LISTA utilizando un iterador

for x in LISTA:
    print x
