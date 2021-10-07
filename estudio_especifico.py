from os import system
import time

import explicador as ex
import generador_de_problemas as gp

def main():
    system("cls")
    print("¿Que tema vas a estudiar?")
    print("1.-Aritmetica")
    print("2.-Algebra")
    print("3.-Geometria")
    print("4.-Funciones y Graficas")
    print("5.-Estadistica descriptiva")
    print("6.-Combinatoria y Probabilidad")
    eleccion = int(input())
    if(eleccion == 1):
        print("Has elegido estudiar Aritmetica")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.aritmetica()
            continuar = None
            while(continuar != "N"):
                gp.aritmetica()
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                gp.aritmetica()
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    if(eleccion == 2):
        print("Has elegido estudiar algebra")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.algebra()
            continuar = None
            while(continuar != "N"):
                gp.algebra()
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                gp.algebra()
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass

    elif(eleccion == 3):
        print("Has elegido estudiar geometria")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.geometria()
            continuar = None
            while(continuar != "N"):
                gp.geometria()
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                gp.geometria()
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 4):
        print("Has elegido estudiar funciones y graficas")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.funciones_y_graficas()
            continuar = None
            while(continuar != "N"):
                gp.funciones_y_graficas()
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                gp.funciones_y_graficas()
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion==5):
        print("Has elegido estudiar estadistica descriptiva")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.estadistica_descriptiva()
            continuar = None
            while(continuar != "N"):
                gp.estadistica_descriptiva()
                continuar = input("¿Quieres otro problema?S/N")
        else:
            continuar = None
            while(continuar != "N"):
                gp.estadistica_descriptiva()
                continuar = input("¿Quieres otro problema?S/N")
        pass
    elif(eleccion==6):
        print("Has elegido estudiar combinatoria y probabilidad")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.combinatoria_probabilidad()
            continuar = None
            while(continuar != "N"):
                gp.combinatoria_probabilidad()
                continuar = input("¿Quieres otro problema?S/N")
        else:
            continuar = None
            while(continuar != "N"):
                gp.combinatoria_probabilidad()
                continuar = input("¿Quieres otro problema?S/N")
        pass

