#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
''' Obtener (a-b)(a+b) '''

print "Ingrese los valores de a y b"
a = int(raw_input("Ingrese el valor de a: "))
b = int(raw_input("Ingrese el valor de b: "))

r =((a+b)*(a-b))
print "(%d - %d)(%d + %d)=%d"%(a, b, a, b, r)
