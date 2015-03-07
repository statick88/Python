#!/usr/bin/env python2.7
#!-*- coding:utf-8 -*-
'''
Leer 3 números y leer el mayor de los 3
'''
n1 = int(input("Ingrese el primer número: "))

n2 = int(input("Ingrese el segundo número: "))

n3 = int(input("Ingrese el tercer número: "))

if n1 > n2 and n1 > n3:
    print "el mayor es %d"%n1

elif n2 > n1 and n2 > n3:
    print "el mayor es %d"%n2

elif n3 > n1 and n3 > n2:
    print "el mayor es %d"%n3
else:
    print "2 o más números son iguales"

