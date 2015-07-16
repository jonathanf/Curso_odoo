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

# Este programa muestra el uso del bucle for

#Recibo los datos del usuarios
n = raw_input("Numero de veces: ")
mensaje = raw_input("Mensaje: ")

#Transformo a entero el Numero de veces
n = int(n)

for i in range(n):
    print "Repeticion: %s mensaje: %s" % (i + 1, mensaje)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: