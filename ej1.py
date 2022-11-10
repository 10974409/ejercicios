#!/usr/bin/env python3
"""
Autor : Jorge Bombardo LLoret <10974409@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de grados Celsius a Fahrenheit
"""

print('Convertidor de grados Celsius a Fahrenheit')
gradosC = float(input('Escribe una temperatura en grados Celsius: '))
gradosF = 1.8*gradosC + 32
print(f'{gradosC} ºC son {gradosF} ºF')