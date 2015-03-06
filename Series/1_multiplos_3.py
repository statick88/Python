#!/usr/bin/python2.7
#!-*- coding:utf-8 -*-

'''Mostrar los múltiplos de 3 comprendidos entre
   Números 1 y 20 '''

for i in range(30):
    i += 1
    if i%3 ==0:
        print "%d es par"%i
    else:
        print "%d es impar"%i
