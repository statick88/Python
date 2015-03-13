#!/usr/bin/env python2.7
#!-*- coding:utf-8 -*-
'''
Ingresar un número y calcular el cuadrado de este
'''
def main():
    print "Se calcularán cuadrados de números"

    n1 = input("Ingrese un número: ")
    n2 = input("Ingrese otro número entero: ")

    for x in range(n1, n2):
        print x*x

    print "Es todo por ahora"

main()
