#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es>
Fecha   : 7/11/2022
Propósito: Escribir una lista de números
"""

n=int(input('Dime un número: '))

if n>=0:
    for i in range (0,n+1):
        print(i,end=", ")
else:
    for i in range (0,n-1,-1):
        print(i,end=", ")

print()