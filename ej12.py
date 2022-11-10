#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es>
Fecha   : 10/11/2022
Propósito: Dibujar un rectángulo con asteriscos dando los datos de la anchura y la altura.
"""

anchura = int(input('Anchura del rectángulo : '))
altura = int(input('Altura del rectángulo: '))

for i in range(altura):
    for j in range(anchura):
        print('*',end='')
    print()
