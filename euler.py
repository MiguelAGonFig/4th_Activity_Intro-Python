# Programa euler.py, calcula el valor del numero de euler

'''
fabs -> Funcion empleada para utilizar el valor absoluto de la operacion realizada
factorial -> Funcion empleada para calcular un factorial
'''

from math import fabs, factorial

def euler(e):
    it = 3
    n = 2
    m = n + float(1/factorial(2))

    while fabs(n - m) >= e:
        n = m
        m += float(1/factorial(it))
        it += 1

    return m

print("Valor aproximado de la constante de Euler: ", euler(0.000000001))