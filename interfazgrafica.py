# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:04:56 2020

@author: Albert López
"""


from const import Const
import pygame

class InterfazGrafica:
    def __init__(self, cj, filas, cols):
        pygame.init()
        self.screen=pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
        pygame.display.set_caption("Lime Rick")
        self.cj=cj
        self.filas=filas
        self.cols=cols
        self.vacio=Const.BLACK
        self.marco=pygame.image.load(Const.ARCHIVO_PARED).convert()
        self.cabeza=pygame.image.load(Const.ARCHIVO_CABEZA).convert()
        self.cabeza_roja=pygame.image.load(Const.ARCHIVO_CABEZA_ROJA).convert()
        self.manzana=pygame.image.load(Const.ARCHIVO_MANZANA).convert()
        self.caja=pygame.image.load(Const.ARCHIVO_CAJA).convert()
        self.cuerpo=pygame.image.load(Const.ARCHIVO_CUERPO).convert()

    def lee_tecla_pulsada(self):
        return pygame.event.wait()
    def dibuja_nivel_actual(self):
        
        mapa=self.cj.nivel_actual
        
        self.screen.fill(self.vacio)
        for i in range(self.filas):
            linea=mapa[i]
            for j in range(self.cols):
                carac=linea[j]
                tam_j=j*Const.TAM_CUADRO
                tam_i=i*Const.TAM_CUADRO
                if carac==Const.CELDA_PARED:
                    self.screen.blit(self.marco,(tam_j,tam_i))
                elif carac==Const.CELDA_CABEZA:
                    self.screen.blit(self.cabeza,(tam_j,tam_i))
                elif carac==Const.CELDA_CABEZA_ROJA:
                    self.screen.blit(self.cabeza_roja,(tam_j,tam_i))
                elif carac==Const.CELDA_MANZANA:
                    self.screen.blit(self.manzana,(tam_j,tam_i))
                elif carac==Const.CELDA_CAJA:
                    self.screen.blit(self.caja,(tam_j,tam_i))
                elif carac==Const.CELDA_CUERPO:
                    self.screen.blit(self.cuerpo,(tam_j,tam_i))

                
        pygame.display.flip()
                
        
            
        
        
    def redibuja(self):
        mapa=self.cj.niveles
        self.screen.fill(self.vacio)
        for i in range(self.filas):
            linea=mapa[i]
            for j in range(self.cols):
                carac=linea[j]
                tam_j=j*Const.TAM_CUADRO
                tam_i=i*Const.TAM_CUADRO
                if carac==Const.CELDA_PARED:
                    self.screen.blit(self.marco,(tam_j,tam_i))
                elif carac==Const.CELDA_CABEZA:
                    self.screen.blit(self.cabeza,(tam_j,tam_i))
                elif carac==Const.CELDA_CABEZA_ROJA:
                    self.screen.blit(self.cabeza_roja,(tam_j,tam_i))
                elif carac==Const.CELDA_MANZANA:
                    self.screen.blit(self.manzana,(tam_j,tam_i))
                elif carac==Const.CELDA_CAJA:
                    self.screen.blit(self.caja,(tam_j,tam_i))
                elif carac==Const.CELDA_CUERPO:
                    self.screen.blit(self.cuerpo,(tam_j,tam_i))

                
        pygame.display.flip()
        
         
        
            
        
        
        
    
        
            
        
                    