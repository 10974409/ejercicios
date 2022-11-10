#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es.es>
Fecha   : 8/11/2022
Propósito: Escribir varias listas de números positivos y consecutivos.
"""

n=int(input('Dime un número positivo: '))

while n <=0:
    print (f'¡Te he pedido un número positivo!')
    n = int(input('Dime un número positivo: '))

for i in range(0, n+1):
    print (i,end = ', ')

print()
for i in range (n,0-1, -1):
    print(i,end=', ')

print()
for i in range (1,n):
    print(i,end=', ')

print()
for i in range (n-1,0, -1):
    print(i,end=', ')

print()
for i in range (0,n+1):
    print(i,end=', ')

for i in range (n-1,0-1,-1):
    print(i,end=', ') 

print()
