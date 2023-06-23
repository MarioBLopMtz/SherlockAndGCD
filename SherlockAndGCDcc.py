#!/bin/python3

import math
import os
import random
import re
import sys

def solve(a):
    # Ordena el arreglo en orden ascendente
    a.sort()
    
    # Suma los dígitos del primer elemento del arreglo
    sum_digits = sum(int(digit) for digit in str(a[0]))
    
    # Verifica si todos los elementos del arreglo son iguales
    if all(x == a[0] for x in a):
        return "NO"  # Si todos los elementos son iguales, no existe un subconjunto que cumpla las condiciones
    
    # Verifica si algún elemento del arreglo es divisible por la suma de dígitos del primer elemento
    for num in a:
        if num % sum_digits == 0:
            return "NO"  # Si encuentra un elemento divisible, no existe un subconjunto que cumpla las condiciones
    
    return "YES"  # Si no se cumple ninguna de las condiciones anteriores, existe un subconjunto que cumple las condiciones

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Lee el número de casos de prueba

    for t_itr in range(t):
        a_count = int(input().strip())  # Lee el tamaño del arreglo

        a = list(map(int, input().rstrip().split()))  # Lee los elementos del arreglo como una lista de enteros

        result = solve(a)  # Llama a la función solve para resolver el problema

        fptr.write(result + '\n')  # Escribe el resultado en el archivo de salida

    fptr.close()
