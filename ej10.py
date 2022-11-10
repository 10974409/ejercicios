#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es>
Fecha   : 9/11/2022
Propósito: Calcular el factorial de un número
"""

numero = int(input('Dime un número: '))
factorial=1
for i in range(1,numero+1):
    factorial=factorial*i

print(f'El factorial de {numero} es: {factorial}')