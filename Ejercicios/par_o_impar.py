#!/usr/bin/env python2.7
#!-*- coding:utf-8 -*-
'''
Crear un programa que lea un número e indique si es par o no
'''
num = int(input("Ingrese un número: "))

if num%2 == 0:
    print "%d es par"%num
else:
    print "%d es impar"%num
