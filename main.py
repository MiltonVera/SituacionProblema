from os import system
import time

import estudio_general as eg
import estudio_especifico as ee
import generador_de_problemas as gp
import inicio_de_sesion as login 

print("Bienvenido a tu mejor amigo para sacar la mejor calificacion de PISA")
print()
print()
time.sleep(1)
print("Tendras la oportunidad de aprender los temas que vienen en el examen de forma practica")
time.sleep(2)
print("Al final de cada tema tendras la oportunidad de practicarlo y ver si lo pudiste aprender correctamente")
time.sleep(2)
print("Cuando te sientas listo/a para realizar el examen PISA te realizaremos un examen final para que puedas comprobar que ya estas preparado para el examen")
time.sleep(2)
kk = input("Presiona enter para empezar")
time.sleep(2)
system("cls")
while True:
    print("Selecciona un opción para comenzar")
    print("1.-Estudio general")
    print("2.-Estudio especifico")
    print("3.-Examen Final")
    print("4.-Salir del programa")
    opcion = input()
    if(opcion == "1" or opcion == "Estudio general"):
        pass
    elif(opcion == "2" or opcion == "Estudio especifico"):
        pass
    elif(opcion == "3" or opcion == "Examen final"):
        pass
    elif(opcion == "4" or opcion == "Salir del programa"):
        print("Hasta la proxima")
        exit()
        




