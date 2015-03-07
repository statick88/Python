#!/usr/bin/python2.7
#!-*- coding:utf-8 -*-
'''
Calcular e imprimir la suma 1+2+3+4+5+…+50
'''

for i in range(1,51):
    r = i
    print i
    r = r + i
    i +=1
print r
