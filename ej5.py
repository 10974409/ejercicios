#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es.es>
Fecha   : 31/10/22
Propósito: Cáculo del área del triángulo o círculo
"""

print('Cálculo de áreas - Elige una figura geométrica:')
print('a) Triángulo')
print('b) Círculo')
figura=input('¿Qué figura quieres calcular (Escribe T o C)? ').upper()
if figura=='T': 
    base=float(input('Escribe la base: '))
    altura=float(input('Escribe la altura: '))
    area=base*altura/2
    print(f'Un triángulo de base {base} y altura {altura} tiene un área de {area}')
elif figura =='C':
    radio=float(input('Escribe el radio: '))
    area=3.14*radio**2
    print(f'Un círculo de radio {radio} tiene un área de {area}')
else:
    print('No es un cícrulo es un triángulo')
