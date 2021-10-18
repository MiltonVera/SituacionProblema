import platform
from os import system

import time
from PIL import Image
instalar = int(input("¿Deseas que el programa te instale las librerias? 1/0"))

if(instalar == 1):
    sistema = platform.system()
    if(sistema == "Windows"):
        system("python -m pip install matplotlib")
        system("python -m pip install tabulate")
        system("python -m pip install colorama")
        system("python -m pip install pillow")
    else:
        system("python3 -m pip install matplotlib")
        system("python3 -m pip install tabulate")
        system("python3 -m pip install colorama")
        system("python3 -m pip install pillow")
import utilidades as ut
import estudio_general as eg
import estudio_especifico as ee
import generador_de_problemas as gp
import examen_final as ex


ut.formato("Bienvenido a tu mejor amigo para sacar la mejor calificación de PISA","BLACK","WHITE",True)
ut.mecanografiar("Tendrás la oportunidad de aprender los temas que vienen en el examen de forma práctica")

print("Al final de cada tema tendrás la oportunidad de practicarlo y ver si lo pudiste aprender correctamente")
print("Cuando te sientas listo/a para realizar el examen PISA te realizaremos un examen final para que puedas comprobar que ya estas preparado para el examen")

ut.pausa()
ut.clear()
while True:
    ut.clear()
    print(ut.tabla(["OPCIÓN","NÚMERO"],["Estudio General",1,"Estudio específico",2,"Examen Final",3,"Ver registro",4,"Borrar Registro",5,"Salir del programa",6]))
    opcion = input()
    if(opcion == "1" or opcion == "Estudio general"): #Manda llamar el estudio_general.py
        eg.main()
        pass
    elif(opcion == "2" or opcion == "Estudio específico"): #Manda llamar el estudio_especifico.py
        ee.main()
        pass
    elif(opcion == "3" or opcion == "Examen final"): #Manda llamar el examen_final.py
        ex.main()
        pass
    elif opcion == "4" or opcion == "Ver Calificaciones":  #Lee el archivo calificaciones.txt la cual tiene las calificaciones que registro el usuario
        ut.mecanografiar("A continuación se mostraran tus calificaciones")
        ut.tabla(["Materia","Calificación"],ut.dict_a_list(ut.leer_calificaciones()))
        ut.pausa()
        pass
    elif opcion == "5" or opcion == "Borrar Registro": #de utilidades, manda llamar la función borrar_registro, la cual borra el archivo de texto
        ut.borrar_registro()
        ut.mecanografiar("Registro borrado correctamente")
        ut.pausa()
    elif(opcion == "6" or opcion == "Salir del programa"): #Termina el programa
        print("Hasta la próxima")
        exit()


        




