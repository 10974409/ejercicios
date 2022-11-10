#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es>
Fecha   : 9/11/2022
Propósito: Saber cuál número es el mayor, menor y la media.
"""

numeros=int(input('¿Cuántos valores vas a introducir?: '))
minimo = 1000000000000000
maximo = 0
suma = 0
media = 0
for i in range (1, numeros+1):
    num = int(input(f'Dime el número {i}: '))
    suma+= num
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
media = suma / numeros

print(f'El número más pequeño de los introducidos es: {minimo}')
print(f'El número más grande de los introducidos es: {maximo}')
print(f'La media de los números introducidos es: {media}')