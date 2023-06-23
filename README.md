# SherlockAndGCD

Descripción del problema: Sherlock está atascado mientras resuelve un problema. Se le proporciona un arreglo A = {a1, a2, ..., an}, y desea saber si existe un subconjunto de este arreglo que cumpla con las siguientes condiciones:

  - B es un subconjunto no vacío.
  - No existe un entero x (x < 1) que divida a todos los elementos de B.
  - No hay elementos en B que sean iguales entre sí.

Solución del problema: Para resolver este problema, debemos verificar todas las posibles combinaciones de subconjuntos del arreglo dado y verificar si cumplen con las condiciones mencionadas.

Intrucciones de ejecución de solución:
  1. Abrir el link (https://www.hackerrank.com/challenges/sherlock-and-gcd/problem?isFullScreen=true).
  2. Abrir el archivo SherlockAndGCDSC.py y copiarlo.
  3. Sustituir el contenido de la consola que hay en la página con el que copiamos del archivo.
  4. Correr el código.

Ejemplos de valores de entrada y salidas esperadas: 
  Entrada:
    3
    3
    1 2 3
    2
    2 4
    3
    5 5 5
  Salida: 
    YES
    NO
    NO
