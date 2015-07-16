# -*- coding: utf-8 -*- 
# copyrigth (c) 2015 Javier Campana <jcampana@cyg.ec>
__author__ = 'Javier'

import clases
continuar = True

while continuar:
    encendido = raw_input("Quiere encender la tv (y/n): ")
    if encendido == 'y':
        encendido = True
    elif encendido == 'n':
        encendido = False
    else:
        print u"no existe esa opción"

    if encendido:
        volumen = int(raw_input("Defina el volumen: "))

    tele = clases.television()

    continuar = raw_input("Desea continuar presione \"y\" o cualquier otra para terminar: ")
    if continuar == 'y':
        continuar = True
    else:
        continuar = False