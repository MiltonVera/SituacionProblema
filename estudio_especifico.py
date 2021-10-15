from os import system
import time

import explicador as ex
import generador_de_problemas as gp
import utilidades as ut

def main():
    system("cls")
    print("¿Que tema vas a estudiar?")
    ut.tabla(["Tema","Opcion"],["Aritmetica",1,"Algebra",2,"Geometria",3,"Funciones y Graficas",4,"Estadistica Descriptiva",5,"Combinatoria y Probabilidad",6])
    eleccion = int(input("Elige una opcion"))
    if(eleccion == 1):
        print("Has elegido estudiar Aritmetica")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.aritmetica()
            system("pause")
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Aritmetica",gp.aritmetica())
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Aritmetica",gp.aritmetica())
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 2):
        print("Has elegido estudiar algebra")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.algebra()
            system("pause")
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Algebra",gp.algebra())
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Algebra",gp.algebra())
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 3):
        print("Has elegido estudiar geometria")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.geometria()
            system("pause")
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Geometria",gp.geometria())
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Geometria",gp.geometria())
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion == 4):
        print("Has elegido estudiar funciones y graficas")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.funciones_y_graficas()
            system("pause")
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Funciones y Graficas",gp.funciones_y_graficas())
                continuar = input("¿Quieres otro problema?S/N").upper()
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Funciones y Graficas",gp.funciones_y_graficas())
                continuar = input("¿Quieres otro problema?S/N").upper()
        pass
    elif(eleccion==5):
        print("Has elegido estudiar estadistica descriptiva")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.estadistica_descriptiva()
            system("pause")
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Estadistica Descriptiva",gp.estadistica_descriptiva())
                continuar = input("¿Quieres otro problema?S/N")
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Estadistica Descriptiva",gp.estadistica_descriptiva())
                continuar = input("¿Quieres otro problema?S/N")
        pass
    elif(eleccion==6):
        print("Has elegido estudiar combinatoria y probabilidad")
        time.sleep(1)
        eleccion = input("¿Deseas ver de nuevo la explicación?S/N")
        if(eleccion.upper()=="S"):
            ex.combinatoria_probabilidad()
            system("pause")
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Combinatoria y Probabilidad",gp.combinatoria_probabilidad())
                continuar = input("¿Quieres otro problema?S/N")
        else:
            continuar = None
            while(continuar != "N"):
                ut.mecanografiar("A continuacion un problema")
                time.sleep(2)
                ut.registrar_calificacion("Combinatoria y Probabilidad",gp.combinatoria_probabilidad())
                continuar = input("¿Quieres otro problema?S/N")
        pass

