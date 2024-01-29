# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:54:58 2020

@author: Albert López
"""
from const import Const


class Celda():
    def __init__(self, fila,col,tipo,nivel):
        self.fila=fila
        self.col=col
        self.tipo=tipo
        self.nivel=nivel
        
    
    def intenta_pasar(self,df,dc):
        self.df=df
        self.dc=dc
        mapa=self.nivel
        Coord_x=0
        Coord_y=0
        if self.df==-1:
            Coord_y=-1

        elif self.df==1:
            Coord_y=1

        elif self.dc==-1:
            Coord_x=-1

        elif self.dc==1:
            Coord_x=1

        res=0
        x=0
        y=0
        t=Coord_x+Coord_x

        for fila in mapa:
            for cuadrado in fila:
                if x==self.col+Coord_x and y==self.fila+Coord_y and cuadrado==Const.CELDA_PARED:
                    res=1
                elif x==self.col+Coord_x and y==self.fila+Coord_y and cuadrado==Const.CELDA_CUERPO:
                    res=1
                elif x==self.col+Coord_x and y==self.fila+Coord_y and cuadrado==Const.CELDA_CAJA: 
                    linea=mapa[self.fila+Coord_y]
                    if linea[self.col+t]==Const.CELDA_PARED or linea[self.col+t]==Const.CELDA_CAJA or linea[self.col+t]==Const.CELDA_MANZANA or linea[self.col+t]==Const.CELDA_CUERPO:
                        res=1
                    else: 
                        res=0
                elif x==self.col+Coord_x and y==self.fila+Coord_y and cuadrado==Const.CELDA_MANZANA:
                        res=2



                x+=1
            x=0
            y+=1

        if res==1:
            return Const.PASO_IMPOSIBLE
            print("Imposible")
        elif res==2:
            return Const.PASO_FIN_NIVEL
        elif res==0:
            return Const.PASO_OK