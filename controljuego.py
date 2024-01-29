# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:00:50 2020

@author: Albert López
"""

from interfazgrafica import InterfazGrafica
from nivel import Nivel
from const import Const
from datosniveles import DatosNiveles
from const import Const
import pygame

class ControlJuego():
    def __init__(self):
        """
        Constructor.  Declara  e  inicializa  los  atributos  previamente  especificados.
        """
        self.niveles=[]
        self.nivel_actual=DatosNiveles.MAPAS
        self.gui=InterfazGrafica(self,Const.NIVEL_FILAS, Const.NIVEL_COLUMNAS)
    def partida(self):
        """
        Bucle principal del juego, se encarga de cargar el nivel:
        1. Lo inicializa.2. Mientras la cabeza se mueva:2.1Redibuja el nivel actual.2.2Gestiona la entrada de datos del teclado, moviendo la serpiente en la dirección deseada, o reiniciando el nivel si se ha pulsado la tecla R.
        """
        pygame.init()
        RUNNING=True
        a=0

        self.nivel_actual=self.nivel_actual[a]
        self.gui.dibuja_nivel_actual()
        self.niveles=self.nivel_actual
        reloj=pygame.time.Clock()
        cont=0
        while  RUNNING:
            nivel=Nivel(Const.NIVEL_FILAS,Const.NIVEL_COLUMNAS,self.niveles,a,cont)
            nivel.inicializar()
            #Eventos
            reloj.tick(30)
           
            if nivel.gravedad():
                nivel.mueve_cabeza(1,0)
                self.niveles=nivel.datos_mapa
                a=nivel.nivel
                self.nivel_actual=DatosNiveles.MAPAS[a]
                self.gui.redibuja()
            else:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        RUNNING=False
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_r:
                            self.niveles=self.nivel_actual
                            self.gui.redibuja()
                            nivel.paso=0
                            cont=0
                        
                        else:
                            if cont==3:
                                if event.key==pygame.K_LEFT:
                                    nivel.mueve_cabeza(0,-1)
                                    if nivel.paso==0:
                                        cont=0
                                    elif nivel.paso==1:
                                        const=3
                                elif event.key==pygame.K_RIGHT:
                                    nivel.mueve_cabeza(0,1)
                                    if nivel.paso==0:
                                        cont=0
                                    elif nivel.paso==1:
                                        const=3
                            else:
                                if event.key==pygame.K_UP:
                                    nivel.mueve_cabeza(-1,0)
                                    cont+=1
                                elif event.key==pygame.K_LEFT:
                                    nivel.mueve_cabeza(0,-1)
                                    cont=0
                                elif event.key==pygame.K_RIGHT:
                                    nivel.mueve_cabeza(0,1)
                                    cont=0
                        
                            self.niveles=nivel.datos_mapa
                            a=nivel.nivel
                            if a==12:
                                fin=pygame.image.load(Const.ARCHIVO_FINPARTIDA).convert()
                                self.gui.screen.fill(Const.BLACK)
                                self.gui.screen.blit(fin,(65,0))
                                pygame.display.flip()
                                while RUNNING:
                                    for event in pygame.event.get():
                                        if event.type==pygame.QUIT:
                                            RUNNING=False
                            else:
                                self.nivel_actual=DatosNiveles.MAPAS[a]
                                self.gui.redibuja()
                    
                    
        
            
    
            
                
                
                    