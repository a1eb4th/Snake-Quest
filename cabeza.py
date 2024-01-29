# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:35:48 2020

@author: Albert López
"""
from const import Const
from celda import Celda
class Cabeza():
    def __init__(self, fila, col):
        self.fila=fila
        self.col=col
        
        
    
    def actualiza_pos(self, df, dc):
        self.df=df
        self.dc=dc
        Coord_x=self.col
        Coord_y=self.fila
        if self.df==-1:
            Coord_y-=1
        elif self.df==1:
            Coord_y+=1
        elif self.dc==-1:
            Coord_x-=1
        elif self.dc==1:
            Coord_x+=1
        self.fila=Coord_y
        self.col=Coord_x
    
    
        
        

            