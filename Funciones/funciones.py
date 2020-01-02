#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""--- Manejo de funciones---"""

## -- Una funcion es una secuencia de comandos que realizan un computo
# --- se utiliza el keyword def, se le asigna un nombre  y si va a recibir algun valor

## se define las librerias en este caso una libreria de grafics
import turtle
""" Aqui estamos definiendo una funcion"""
def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)
    turtle.mainloop()

def make_square(dave):
    length = int(raw_input('Tamanio del cuadrado: '))
    for i in range(4):
        make_line_and_turn(dave, length)
def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

"""Con este if definimos a partir de donde iniciar a ejecutar nuestroo script"""

if __name__ == '__main__':
    main()