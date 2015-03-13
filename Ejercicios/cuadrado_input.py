#!/usr/bin/env python2.7
#!-*- coding:utf-8 -*-
'''
Ingresar un número y calcular el cuadrado de este
'''
def cuadrado(num):
    num = int(input("Ingrese un primer número: "))
    cuadrado = num*num
    print "El cuadrado de %d es %d"%(num, cuadrado)

cuadrado()
