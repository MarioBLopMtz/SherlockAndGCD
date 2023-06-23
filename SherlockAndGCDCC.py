#!/bin/python3

import math
import os
import random
import re
import sys

def solve(a):
    # Función para determinar si existe un subconjunto válido en el arreglo 'a'

    n = len(a)  # Tamaño del arreglo 'a'

    for num in a:  # Iterar sobre cada número en el arreglo 'a'
        if num == 1:
            return "YES"  # Si hay un 1 en el arreglo, automáticamente se considera válido

        for i in range(2, int(num ** 0.5) + 1):
            # Verificar si el número 'num' es divisible por algún número 'i' en el rango de 2 a la raíz cuadrada de 'num'
            if num % i == 0:
                return "NO"  # Si es divisible, el subconjunto no es válido y se devuelve "NO"

    return "YES"  # Si no se encontraron divisores para ningún número, el subconjunto es válido y se devuelve "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Leer el número de casos de prueba

    for t_itr in range(t):
        a_count = int(input().strip())  # Leer el tamaño del arreglo 'a'

        a = list(map(int, input().rstrip().split()))  # Leer los elementos del arreglo 'a'

        result = solve(a)  # Llamar a la función solve para obtener el resultado

        fptr.write(result + '\n')  # Escribir el resultado en el archivo de salida

    fptr.close()
