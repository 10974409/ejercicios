#!/usr/bin/env python3
"""
Autor : Jorge Bombardó Lloret <10974409@iespenyagolosa.es>
Fecha   : 10/11/2022
Propósito: Cambiar todas las vocales de una frase por una vocal seleccionada.
"""

frase = 'tengo una hormiguita en la barriga'
vocal = input('Dime una vocal: ')
VOCALES = ()

for i in range(len(frase)):
    if frase[i] in VOCALES:
        frase_nueva.append(vocal)
    else:
        frase_nueva.append(frase[i])


print(f'La frase es ahora: {frase}')