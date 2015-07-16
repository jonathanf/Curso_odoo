# -*- coding: utf-8 -*-
#    Copyright (C) 2015  Jonathan Finlay <jfinlay@riseup.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Defino mi función
def calculadora(a, b, op, resultado = 0):
    if op == '+':
        resultado = a + b
    elif op == '-':
        resultado = a - b
    elif op == '*':
        resultado = a * b
    elif op == '/':
        # Capturo el error ZeroDivisionError
        try:
            resultado = a / b
        except ZeroDivisionError:
            print "No puedo dividir para 0 (cero)"
    else:
        print "No existe esa opcion!!!"
    return resultado

def imprimir(mensaje):
    print mensaje.upper()

# Este es el programa principal
imprimir("######   mi programa  ######")
imprimir("#     calculadora 2.0      #")
imprimir("############################")

a = float(raw_input("Primer numero: "))
b = float(raw_input("Segundo numero: "))

op = raw_input("Quiere hacer todas las operaciones (y/n): ")

if op != 'y' and op != 'n':
    print "Error opcion invalida (y/n)"
elif op == 'y':
    imprimir("suma: " + str(calculadora(a, b, '+')))
    imprimir("resta: " + str(calculadora(a, b, '-')))
    imprimir("multi: " + str(calculadora(a, b, '*')))
    imprimir("divi: " + str(calculadora(a, b, '/')))
else:
    print "Chao..."
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: