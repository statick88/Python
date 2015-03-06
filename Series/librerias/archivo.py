#!/usr/bin/python2
#!-*-coding:utf8-*-

from sys import argv
import serie1, serie2

script, filename = argv

print "Archivo creado %r" %filename

def crear_archivo(filename)

    file = open(filename,"w")
    file.write("La series son creadas en el lenguaje Python")
    serie1.crear_serie()
    serie2.crear_serie()
    file.close

print "terminado"
