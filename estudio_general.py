from os import system
import generador_de_problemas as gp
import time
def main():
    system("cls")
    print("A continuacion veras cuales son los temas a ver")
    print()
    print("-Geometria")
    print("-Funciones y Graficas")
    print("-Estadistica descriptiva")
    print("-Combinatoria y Probabilidad")
    time.sleep(4)
    system("cls")
    print("Empezaremos con Geometría")
    #Aqui se pondra la explicación de geometría
    gp.geometria()#Se le da al usuario un problema de geometria
    print("El siguiente tema a tratar es Funciones y graficas")
    #Aqui se pondra la explicación de funciones y graficas
    gp.funciones_y_graficas#Aqui se le da un problema de practica a resolver para el usuario
    print("El siguiente tema es estadistica descriptiva")
    #Explicación del tema
    gp.estadistica_descriptiva()#Problema a resolver
    print("El ultimo tema a tratar es el de combinatoria y probabilidad")
    #Explicación del tema
    gp.combinatoria_probabilidad()#Problema a resolver por parte del usuario

