#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es>
Fecha   : 26/10/22
Propósito: Resolver una ecuación de segundo grado.
"""

print('Ecuación a x2 + b x + c = 0')
a = int(input('Escribe el valor del coeficiente a: '))
b = int(input('Escribe el valor del coeficiente b: '))
c = int(input('Escribe el valor del coeficiente c: '))
solucion1 = (-b +(b**2 -4*a*c)**(1/2)) /(2*a)
solucion2 = (-b -(b**2 -4*a*c)**(1/2)) /(2*a)
print(f'Las soculciones de la ecucación son {solucion1} y {solucion2}')
