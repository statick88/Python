#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
'''
Crear un programa que lea 2 números y que escriba
el mayor de los 2
'''
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 > n2:
    print "El mayor es %d"%n1
elif n2 > n1:
    print "El mayor es %d"%n2
else:
    print "Son iguales"
