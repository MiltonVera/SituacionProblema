from os import system

import explicador as ex
import generador_de_problemas as gp
import utilidades as ut
import time
def main():
    system("cls")
    print("A continuacion veras cuales son los temas a ver")
    print()
    print("-Aritmetica")
    print("-Algebra")
    print("-Geometria")
    print("-Funciones y Graficas")
    print("-Estadistica descriptiva")
    print("-Combinatoria y Probabilidad")
    time.sleep(4)
    system("cls")

    print("El primer tema a tratar es Aritmetica")
    ex.aritmetica()#Aqui se pondra la explicación de geometría
    ut.registrar_calificacion("Aritmetica",gp.aritmetica())#Se le da al usuario un problema de geometria
    system("pause")
    system("cls")
    print("El siguiente tema a tratar es Algebra")
    ex.algebra()#Aqui se pondra la explicación de geometría
    ut.registrar_calificacion("Algebra",gp.algebra())#Se le da al usuario un problema de geometria
    system("pause")
    system("cls")
    print("El siguiente tema a tratar es Geometría")
    ex.geometria()#Aqui se pondra la explicación de geometría
    ut.registrar_calificacion("Geometria",gp.geometria())#Se le da al usuario un problema de geometria
    system("pause")
    system("cls")
    print("El siguiente tema a tratar es Funciones y graficas")
    ex.funciones_y_graficas()#Aqui se pondra la explicación de funciones y graficas
    ut.registrar_calificacion("Funciones y Graficas",gp.funciones_y_graficas())#Aqui se le da un problema de practica a resolver para el usuario
    system("pause")
    system("cls")
    print("El siguiente tema es estadistica descriptiva")
    ex.estadistica_descriptiva()#Explicación del tema
    ut.registrar_calificacion("Estadistica Descriptiva",gp.estadistica_descriptiva())#Problema a resolver
    system("pause")
    system("cls")
    print("El ultimo tema a tratar es el de combinatoria y probabilidad")
    ex.combinatoria_probabilidad()#Explicación del tema
    ut.registrar_calificacion("Combinatoria y Probabilidad",gp.combinatoria_probabilidad())#Problema a resolver por parte del usuario
    system("pause")
    system("cls")

