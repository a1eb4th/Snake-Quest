# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:06:19 2020

@author: Albert López
"""

class Const:
    
    #Ancho de la ventana de la aplicación
    SCREEN_WIDTH=700
    
    #Alto de la ventana de la aplicación
    SCREEN_HEIGHT=560
    
    #Tamaño de cada una de las celdas que conforman la ventana de la aplicación
    TAM_CUADRO=35
    
    #Número de columnas del recinto de Celdas contenidas en un Nivel
    NIVEL_COLUMNAS = 19
    
    #Número de filas del recinto de Celdas contenidas en un Nivel
    NIVEL_FILAS = 15
    
    #Color negro
    BLACK = (0, 0, 0)
    
    #Número de cabezas de altura que la serpiente puede subir sobre sí misma.
    MAX_ALTURA=3
    
    #Nombre del archivo en el que está la imagen de la cabeza de la serpiente
    ARCHIVO_CABEZA = "./imagenes/cabeza.png"
    
    #Nombre del archivo en el que está la imagen de la cabeza roja de la serpiente
    ARCHIVO_CABEZA_ROJA = "/imagenes/cabezaroja.png"
    
    #Nombre del archivo en el que está la imagen de la cabeza roja de la serpiente
    ARCHIVO_CABEZA_ROJA = "./imagenes/cabezaroja.png"
    
    #Nombre del archivo en el que está la imagen del cuerpo de la serpiente
    ARCHIVO_CUERPO = "./imagenes/cuerpo.png"
    
    #Nombre del archivo en el que está la imagen de la caja
    ARCHIVO_CAJA = "./imagenes/caja.png"
    
    #Nombre del archivo en el que está la imagen de la manzana
    ARCHIVO_MANZANA = "./imagenes/manzana.png"
    
    #Nombre del archivo en el que está la imagen de la pared
    ARCHIVO_PARED = "./imagenes/pared.png"
    
    #Nombre del archivo en el que está la imagen del fin de la partida
    ARCHIVO_FINPARTIDA = "./imagenes/finPartida.png"

    """Caracter que en el mapa de caracteres de Nivel (ver DatosNiveles) indica
       la situación de la cabeza de la serpiente.
       Este valor también se usa para definir el tipo de una Celda."""
    CELDA_CABEZA = 'O'
    
    #Caracter que define una Celda como parte del cuerpo de la serpiente.
    CELDA_CUERPO = 'X'
    
    """Caracter que en el mapa de caracteres de Nivel (ver DatosNiveles) indica
       la situación de una celda vacía."""
    CELDA_VACIA = ' '
    
    """Caracter que en el mapa de caracteres de @link Nivel (ver DatosNiveles) indica
       la situación de una pared.
       Este valor también se usa para definir el tipo de una Celda."""
    CELDA_PARED = '#'
    
    """Caracter que en el mapa de caracteres de Nivel (ver DatosNiveles) indica
       la situación de la manzana.
       Este valor también se usa para definir el tipo de una link Celda."""
    CELDA_MANZANA = 'M'
    
    """ Caracter que en el mapa de caracteres de Nivel (ver DatosNiveles) indica
       la situación de una caja.
       Este valor también se usa para definir el tipo de una Celda."""
    CELDA_CAJA = 'K'

    CELDA_CABEZA_ROJA= 'U'
    
    """Valor que define como exitoso el intento de paso hacia una casilla (porque no habían
       obstáculos, o éstos se han podido empujar hacia la casilla contigua)."""
    PASO_OK = 0
    
    """Valor que define como fallido el intento de paso hacia una casilla (porque habían obstáculos
       que no han podido moverse)"""
    PASO_IMPOSIBLE = 1
    
    """Valor que informa de que el intento de paso hacia una casilla ha resultado ser el fin del
       nivel (la cabeza ha cogido la manzana)."""
    PASO_FIN_NIVEL = 2
    
    TECLA_R="r"
    
    TECLA_DERECHA="right"
    
    TECLA_IZQUIERDA="left"
    
    TECLA_ARRIBA="up"