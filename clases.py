# -*- coding: utf-8 -*- 
# copyrigth (c) 2015 Javier Campana <jcampana@cyg.ec>
__author__ = 'Javier'

class television():

    def __init__(self, encendido=False, volumen=5, canal=0):
        self.encendido = encendido
        self.volumen = volumen
        self.canal = canal

    def prender(self):
        if self.encendido == True:
            self.apagar()
        else:
            self.encendido = True

    def apagar(self):
        if self.encendido == False:
            self.prender()
        else:
            self.encendido = False

    def cambiar_canal(self, canal):
        if self.encendido == True:
            self.canal = canal

    def cambiar_volumen(self, volumen):
        if self.encendido == True:
            self.volumen = volumen

    def estado_television(self):
        if self.encendido == True:
            return "Prendida"
        else:
            return "Apagada"


# tele = television(True, 7, 3)
# print "Estado de la television: " + tele.estado_television()
# tele1 = television(False, 5, 2)
# print "Estado de la tele1: " + tele1.estado_television()
# print "Volumen de la tele1: " + str(tele1.volumen)
# print "Canal de la tele1: " + str(tele1.canal)
