#!/usr/bin/env python3
# -*- coding: latin-1 -*-

"""--- Factorial de un numero( Manejo de strings)---"""

## -- Esta funcion hace uso del manejo de funciones recursivas
# --- en el cual  la funcion se ejecuta y se manda a llamar a si misma
# --- tantas veces sea necesario y se cumpla la condicion del if

def facto(numero):
    if numero == 0:
        return 1
    return numero*facto(numero-1)




if __name__ == '__main__':
    print ("Bienvenido al calculo de factorial")
    numero = int(input("Ingresa un numero a calcular ___:"))
    print ("El valor de su resultado es:  " + str(facto(numero)))
