from os import system
import time

import explicador as ex
import generador_de_problemas as gp
import utilidades as ut

def main():
    system("cls")
    print("¿Que tema vas a estudiar?")  #Le muestra al usuario las opciones que desea estudiar
    ut.tabla(["Tema","Opcion"],["Aritmetica",1,"Algebra",2,"Geometria",3,"Funciones y Graficas",4,"Estadistica Descriptiva",5,"Combinatoria y Probabilidad",6])
    eleccion = int(input("Elige una opcion"))

    if(eleccion == 1): #Opción aritmética 
        print("Has elegido estudiar Aritmetica")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"): #del explicador.py manda llamar la funcion aritmetica
            ex.aritmetica()
            ut.pausa()
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Aritmetica",gp.aritmetica()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Aritmetica",gp.aritmetica()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 2):#Opción algebra
        print("Has elegido estudiar algebra")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"): #del explicador.py manda llamar la funcion algebra
            ex.algebra()
            ut.pausa()
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Algebra",gp.algebra())#del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Algebra",gp.algebra()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 3):#Opción geometría
        print("Has elegido estudiar geometria")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):#del explicador.py manda llamar la funcion geometria
            ex.geometria()
            ut.pausa()
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Geometria",gp.geometria()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Geometria",gp.geometria()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 4): #Opción funciones y graficas
        print("Has elegido estudiar funciones y graficas")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"): #del explicador.py manda llamar la funcion funciones_y_graficas
            ex.funciones_y_graficas()
            ut.pausa()
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Funciones y Graficas",gp.funciones_y_graficas()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Funciones y Graficas",gp.funciones_y_graficas()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion==5):#Opción estadística descriptiva 
        print("Has elegido estudiar estadistica descriptiva")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"): #del explicador.py manda llamar la funcion estadistica_descriptiva
            ex.estadistica_descriptiva()
            ut.pausa()
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Estadistica Descriptiva",gp.estadistica_descriptiva()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N")
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Estadistica Descriptiva",gp.estadistica_descriptiva()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N")
        pass
    elif(eleccion==6): #Opción combinatoria y probabilidad
        print("Has elegido estudiar combinatoria y probabilidad")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"): #del explicador.py manda llamar la funcion combinatoria_probabilidad
            ex.combinatoria_probabilidad()
            ut.pausa()
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Combinatoria y Probabilidad",gp.combinatoria_probabilidad()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N")
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Combinatoria y Probabilidad",gp.combinatoria_probabilidad()) #del generador_de_problemas.py manda a llamar la función que genera problemas de esa área de matemáticas y guarda la calificación en el archivo de texto calificaciones.txt
                continuar = input("¿Quieres otro problema?S/N")
        pass

