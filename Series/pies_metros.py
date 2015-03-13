#!/usr/bin/env python2.7
#-*- coding:utf-8-*-
'''
Dada una cantidad expresada en pies, y otra en metros. Determinar
la suma pero convertida a pulgadas, yardas, metros, a millas por separado.
Considere las siguientes equivalencias:

    1 milla = 1609 metros
    1 pulgada = 0.0254 metros
    1 yarda = 3 pies
    1 pie = 12 pulgadas
'''

cantidad_pies = int(raw_input("Ingrese la cantidad en pies: "))

cantidad_metros = int(raw_input("Ingrese la cantidad en metros: "))

pulgadas = (cantidad_pies * 12) + (cantidad_metros/0.0225)
yardas = (cantidad_pies/3) + (cantidad_metros*1.09361)
metros = (cantidad_pies*0.3045) + cantidad_metros
millas = (cantidad_pies*0.00019) + (cantidad_metros * 0.00062)

print "La suma en pulgadas es: %d"%pulgadas

print "La suma en yardas es: %d"%yardas

print "La suma metros es: %d"%metros

print "La suma en millas es: %d"%millas

