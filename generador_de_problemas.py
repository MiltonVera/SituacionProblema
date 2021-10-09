import random
import time
import math
import utilidades as ut

def comprobar(respuesta):
    if(respuesta != int(input("Introduce tu respuesta --> "))):
        ut.mecanografiar(f"Respuesta incorrecta, la respuesta correcta es {respuesta}")
    else:
        ut.mecanografiar(f"Felicidades tu respuesta es correcta")


def aritmetica():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        largo = random.randrange(50,100,1)
        ancho = random.randrange(20,70,1)
        respuesta = largo*ancho
        print(f"""Para un concierto de rock se reservo un area de {largo}m de largo y {ancho}m de ancho.
                  Determina cual es la cantidad de personas que caben en el terreno si cada persona ocupa un metro de espacio""")
        comprobar(respuesta)
        time.sleep(1)
        pass
    elif eleccion == 2:
        tablas_largas = random.randrange(1,50,1)
        tablas_cortas = random.randrange(1,50,1)
        ganchos_pequeños = random.randrange(100,400,1)
        ganchos_grandes = random.randrange(5,30,1)
        tornillos = random.randrange(350,700,5)
        cantidades = [tablas_largas/4,tablas_cortas/6,ganchos_pequeños/12,ganchos_grandes/2,tornillos/14]
        respuesta= math.floor(min(cantidades))
        print("""Un carpintero necesita lo siguiente para hacer una estanteria
                 4 tablas largas de madera
                 6 tablas cortas de madera
                 12 ganchos pequeños
                 2 ganchos grandes
                 14 tornillos""")
        print(f"""El carpintero tiene en el almacén {tablas_largas} tablas largas de madera, {tablas_cortas} tablas cortas de 
                  madera, {ganchos_pequeños} ganchos pequeños, {ganchos_grandes} ganchos grandes y {tornillos} tornillos. """)
        print("Determina cuantas estanterias completas puede realizar el carpintero")
        comprobar(respuesta)
        time.sleep(1)
        pass
    elif eleccion == 3:
        cantidad = random.randrange(100,700,5)
        respuesta = cantidad*0.6
        print("""La receta para preparar 100ml de aliño es""")
        ut.tabla(["Ingredientes","Cantidad"],["Aceite para ensalada","60ml","Vinagre","30ml","Salsa de soja","10ml"])
        print(f"""¿Cuantos mililitros de aceite para ensalda necesita para preparar {cantidad}ml de este aliño?""")
        comprobar(respuesta)
        pass
def algebra():

    pass
def geometria():

    pass
def funciones_y_graficas():

    pass
def estadistica_descriptiva():

    pass
def combinatoria_probabilidad():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        years = random.randrange(5,30,1)
        respuesta = largo*ancho
        print(f"""Se emitió un documental sobre terremotos y la frecuencia con que éstos ocurren. El documental incluía un debate sobre la posibilidad de predecir los terremotos. /nUn geólogo afirmó: En los próximos {years} años, hay dos posibilidades por cada 3 de que ocurra un terremoto en la ciudad de Zed. """)
        comprobar(respuesta)
        time.sleep(1)
        pass
    elif eleccion == 2:
        tablas_largas = random.randrange(1,50,1)
        tablas_cortas = random.randrange(1,50,1)
        ganchos_pequeños = random.randrange(100,400,1)
        ganchos_grandes = random.randrange(5,30,1)
        tornillos = random.randrange(350,700,5)
        cantidades = [tablas_largas/4,tablas_cortas/6,ganchos_pequeños/12,ganchos_grandes/2,tornillos/14]
        respuesta= math.floor(min(cantidades))
        print("""Un carpintero necesita lo siguiente para hacer una estanteria
                 4 tablas largas de madera
                 6 tablas cortas de madera
                 12 ganchos pequeños
                 2 ganchos grandes
                 14 tornillos""")
        print(f"""El carpintero tiene en el almacén {tablas_largas} tablas largas de madera, {tablas_cortas} tablas cortas de 
                  madera, {ganchos_pequeños} ganchos pequeños, {ganchos_grandes} ganchos grandes y {tornillos} tornillos. """)
        print("Determina cuantas estanterias completas puede realizar el carpintero")
        comprobar(respuesta)
        time.sleep(1)
        pass
    elif eleccion == 3:
        cantidad = random.randrange(100,700,5)
        respuesta = cantidad*0.6
        print("""La receta para preparar 100ml de aliño es""")
        ut.tabla(["Ingredientes","Cantidad"],["Aceite para ensalada","60ml","Vinagre","30ml","Salsa de soja","10ml"])
        print(f"""¿Cuantos mililitros de aceite para ensalda necesita para preparar {cantidad}ml de este aliño?""")
        comprobar(respuesta)

    pass
