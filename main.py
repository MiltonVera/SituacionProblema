from os import system
import time
from PIL import Image

import utilidades as ut
import estudio_general as eg
import estudio_especifico as ee
import generador_de_problemas as gp

#im = Image.open("tec.jpg")
#im.show()

print(ut.formato("Bienvenido a tu mejor amigo para sacar la mejor calificacion de PISA","BLACK","WHITE",True))

#time.sleep(1)
ut.mecanografiar("Tendras la oportunidad de aprender los temas que vienen en el examen de forma practica")
#time.sleep(2)
print("Al final de cada tema tendras la oportunidad de practicarlo y ver si lo pudiste aprender correctamente")
#time.sleep(2)
print("Cuando te sientas listo/a para realizar el examen PISA te realizaremos un examen final para que puedas comprobar que ya estas preparado para el examen")
#time.sleep(2)
kk = input("Presiona enter para empezar")
#time.sleep(2)
system("cls")
while True:
    print(ut.tabla(["OPCION","NUMERO"],["Estudio General",1,"Estudio especifico",2,"Examen Final",3,"salir del programa",4]))
    opcion = input()
    if(opcion == "1" or opcion == "Estudio general"):
        eg.main()
        pass
    elif(opcion == "2" or opcion == "Estudio especifico"):
        ee.main()
        pass
    elif(opcion == "3" or opcion == "Examen final"):
        pass
    elif(opcion == "4" or opcion == "Salir del programa"):
        print("Hasta la proxima")
        exit()
        




