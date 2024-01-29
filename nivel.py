# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:23:33 2020

@author: Albert López
"""
import pygame
from const import Const
from cabeza import Cabeza
from celda import Celda
from datosniveles import DatosNiveles

class Nivel():
    
    def __init__(self, fils, cols, datos_mapa,nivel,cont):
      
       self.fils=fils
       self.cols=cols
       self.datos_mapa=datos_mapa
       self.cabeza=pygame.image.load(Const.ARCHIVO_CABEZA).convert()
       self.celda=[]
       self.nivel=nivel
       self.cont=cont
       self.paso=""
  
    def inicializar(self):
        mapa=self.datos_mapa
        x=0
        y=0 
        for fila in mapa:
            for cuadrado in fila:
                if cuadrado==Const.CELDA_PARED:
                    self.celda.append(Celda(y,x,Const.CELDA_PARED,self.datos_mapa))
                elif cuadrado==Const.CELDA_VACIA:
                    self.celda.append(Celda(y,x,Const.CELDA_VACIA,self.datos_mapa))
                elif cuadrado==Const.CELDA_CABEZA:
                    self.celda.append(Celda(y,x,Const.CELDA_CABEZA,self.datos_mapa))
                elif cuadrado==Const.CELDA_CABEZA_ROJA:
                    self.celda.append(Celda(y,x,Const.CELDA_CABEZA,self.datos_mapa))
                elif cuadrado==Const.CELDA_MANZANA:
                    self.celda.append(Celda(y,x,Const.CELDA_MANZANA,self.datos_mapa))
                elif cuadrado==Const.CELDA_CAJA:
                    self.celda.append(Celda(y,x,Const.CELDA_CAJA,self.datos_mapa))
                elif cuadrado==Const.CELDA_CUERPO:
                    self.celda.append(Celda(y,x,Const.CELDA_CUERPO,self.datos_mapa))
                x+=1
            x=0
            y+=1
        
                   
            
    def mueve_cabeza(self,df,dc):
        self.df=df
        self.dc=dc
        mapa=self.datos_mapa
        mapa_fin=self.datos_mapa
        lista=""
        cabeza=Celda(0,0,Const.CELDA_VACIA,self.datos_mapa)
        for celda in self.celda:
            if celda.tipo==Const.CELDA_CABEZA:
                cabeza=celda
        if cabeza.intenta_pasar(self.df, self.dc,)==Const.PASO_OK:
            self.paso=0
            coord_ini=Cabeza(cabeza.fila,cabeza.col)
            coord_fin=Cabeza(cabeza.fila,cabeza.col)
            coord_fin.actualiza_pos(self.df,self.dc)
            mapa_fin=[]
            a=20
            b=20
            celdas=self.celda
            for elem in celdas:
                if coord_fin.fila==elem.fila and coord_fin.col==elem.col and Const.CELDA_CAJA==elem.tipo:
                    a=coord_fin.fila
                    b=coord_fin.col
                    if self.df==-1:
                        a-=1
                    elif self.df==1:
                        a+=1
                    elif self.dc==-1:
                        b-=1
                    elif self.dc==1:
                        b+=1
            suelo=False
            while suelo==False:
                muro=Const.CELDA_PARED
                for elem in self.celda:
                    if elem.col==b and elem.fila==a+1 and elem.tipo==Const.CELDA_VACIA:
                        a+=1
                        suelo=False
                    else:
                        suelo=True
            x=0
            y=0
        
            for linea in mapa:
                for cuadrado in linea:
                    if y==coord_ini.fila and x==coord_ini.col:
                        lista+=Const.CELDA_CUERPO
                    elif y==coord_fin.fila and x==coord_fin.col and self.cont!=2:
                        lista+=Const.CELDA_CABEZA
                    elif y==coord_fin.fila and x==coord_fin.col and self.cont==2 and self.df==-1:
                        lista+=Const.CELDA_CABEZA_ROJA
                    elif y==coord_fin.fila and x==coord_fin.col and self.cont==2 and self.df!=-1:
                        lista+=Const.CELDA_CABEZA
                    elif y==a and x==b:
                        lista+=Const.CELDA_CAJA
                    else:
                        lista+=cuadrado
                    x+=1
                x=0
                y+=1       
                mapa_fin.append(lista)
                lista=""
        elif Celda(cabeza.fila,cabeza.col,Const.CELDA_CABEZA,self.datos_mapa).intenta_pasar(self.df, self.dc)==Const.PASO_FIN_NIVEL:
            self.paso=0
            self.nivel+=1
            if self.nivel!=12:
                mapa_fin=DatosNiveles.MAPAS[self.nivel]
        else:
            self.paso=1
        

        
        self.datos_mapa=mapa_fin
    
    def gravedad(self):
        tipo=Const.CELDA_PARED
        for elem in self.celda:
            if elem.tipo==Const.CELDA_CABEZA:
                cabeza=elem
        for elem in self.celda:
            if elem.col==cabeza.col and elem.fila==cabeza.fila+1:
                tipo=elem.tipo
        if tipo==Const.CELDA_VACIA:
            return True
        else:
            return False
    
   
            


        
                    
            
        
            
        
        
        
        

       