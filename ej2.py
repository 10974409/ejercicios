#!/usr/bin/env python3
"""
Autor : Jorge Bombardo LLoret <10974409@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de segundos a minutos
"""

print('Convertidor de segundos a minutos')
segundos = int(input('Escribe los segundos: '))
minutos = segundos//60
segundos_restantes = segundos % 60
print(f'{segundos} segundos son {minutos} minutos y {segundos_restantes} segundos')