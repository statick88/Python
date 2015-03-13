#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
'''Dos atletas recorren la misma distancia y se registra sus tiempos
   se desea saber el tiempo total utilizado por ambos atletas en horas,
   minutos y segundos '''

m1 = int(raw_input("Ingrese el tiempo en minutos del 1er Atleta: "))
s1 = int(raw_input("Ingrese el tiempo en segundos del primer Atleta: "))


m2 = int(raw_input("Ingrese el tiempo en minutos del 1er Atleta: "))
s2 = int(raw_input("Ingrese el tiempo en segundos del primer Atleta: "))

m = m1+m2
s = s1+s2
h=0

if s>=60:
    m = m+1
    s = s-60
    if m>=60:
        h=h+1
        m=m-60
if m>=60:
    h=h+1
    m=m-60

print "La hora recorrida es: %d"%h
print "Los minutos recorridos son: %d"%m
print "Los segundos recorridos son: %s"%s
