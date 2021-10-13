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
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        mililitros_anil = random.randrange(110,250,10)
        mililitros = mililitros_anil/100
        resp = mililitros*60
        respuesta = math.floor(resp)
        print("Para preparar 100 ml de anil para una ensalada, se necesitan 60 ml de aceite para ensalada, 30 ml de vinagre y 10 ml de salsa de soja.")
        print(f"¿Cuántos mililitros (ml) de aceite para ensalada necesitas para preparar {mililitros_anil} ml de aliño? (redondea tu respuesta a enteros)")
        comprobar(respuesta)
        pass

    elif eleccion == 2:
        num_periodicos = random.randrange(250,500,5)
        periodicos_extra = num_periodicos - 240
        resp = round(((240*0.2) + (periodicos_extra*0.4)),2)
        respuesta = resp
        print("""En Alemania, una empresa de periódicos quiere contratar vendedores. En sus anuncios, muestran como se le pagará a sus vendedores, lo que dicen los anuncios es lo siguiente: 
                “Pagamos: 0,20 Euros por periódico para los primeros 240 ejemplares que vendas en una semana, más 0,40 Euros por cada periódico adicional vendido.”""")
        print(f"Si Juanito vendió {num_periodicos} ejemplares la semana pasada, ¿Cuánto dinero le tienen que pagar a Juanito? (redondea tu respuesta a 2 decimales)")
        comprobar(respuesta)
        pass

    elif eleccion == 3:
        pasos_min = random.randrange(70,100,10)
        constante = random.randrange(100,150,10)
        resp = pasos_min / constante
        respuesta  = round(resp,2)
        print(f"""Pedro caminó por un camino enlodado y fue dejando huellas por todo el camino, la longitud del paso 
                  es la  es la distancia entre los extremos posteriores de dos huellas consecutivas. 
                  En el caso de los hombres, la fórmula n/p = {constante}, da una relación aproximada entre 
                  n (número de pasos por minuto) y P (longitud de los pasos en metros).""")
        print(f"Si Pedro da {pasos_min} pasos por minuto ¿Cuál es la longitud de sus pasos? Aplique la fórmula y redondee a 2 decimales.")
        comprobar(respuesta)
        pass

def geometria():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        diametro = random.randrange(20,50,10)
        radio = diametro/2
        area_pizza = 3.1416*(radio^2)
        area_rebanada = area_pizza/8
        respuesta = round(area_rebanada,2)
        print(f"Una pizzería vende pizzas con un diámetro de {diametro} cm y cada pizza tiene 8 rebanadas.")
        print("¿Cuántos centímetros cuadrados tiene cada rebanada de pizza? (Redondea tu respuesta a 2 decimales)")
        comprobar(respuesta)
        pass

    elif eleccion == 2:
        altura =  random.randrange(140,160,5)
        diametro =  random.randrange(120,140,10)
        altura_centro = (diametro/2) + (altura-diametro)
        respuesta = altura_centro
        print(f"Una noria tiene un diámetro exterior de {diametro} metros y el su punto más alto se encuentra a {altura} metros del suelo")
        print("¿A qué altura se encuentra el centro de la noria con respecto al suelo?")
        comprobar(respuesta)
        pass

    elif eleccion == 3:
        personas_por_min = 24
        min = random.randrange(20,40,2)
        respuesta = personas_por_min * min
        print("""Una puerta giratoria consta de tres hojas que giran dentro de un espacio circular. 
                 El diámetro del círculo es de 2 metros y las 3 hojas de la puerta dividen el espacio
                 en tres sectores iguales.""")
        print(f"""Si la puerta da 4 vueltas por minuto y en cada sector hay espacio para 2 personas, 
                  ¿Cuál es el número máximo de personas que pueden entrar en el edificio por la puerta
                  en {min} minutos?""")
        comprobar(respuesta)
        pass

def funciones_y_graficas():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        pass
    elif eleccion == 2:
        pass
    elif eleccion == 3:
        pass

def estadistica_descriptiva():
    eleccion = random.choice([1,2])
    if eleccion == 1:
        examen_5 = random.randrange(70,100,10)
        media = ((60*4)+examen_5)/5
        respuesta = round(media,2)
        print(f"""En el colegio de Mariana, los exámenes se puntúan del 0 al 100 y todos tienen el mismo peso en la calificación final. 
                  Si en sus primeros 4 exámenes la media de calificación de Mariana es de 60 puntos y en su 5 examen obtiene un {examen_5}.""")
        print("¿Cuál será la media de calificaciones de Mariana después de los 5 exámenes? (Redondea a 2 decimales)")
        comprobar(respuesta)
        pass

    elif eleccion == 2:
        estatura_nueva = random.randrange(110,150,10)
        media = ((130*24) + estatura_nueva) / 25
        respuesta = round(media,2)
        print(f"""En una clase hay 25 chicas. En su clase de educación física les piden calcular
                  su estatura media pero ese día faltó una chica a la clase. La estatura media de las 24 chicas es de 130 cm. 
                  Al siguiente dia miden a la chica que faltó y su estatura es de {estatura_nueva} cm. """)
        print("¿Cuál es la estatura media de la clase? (Redondea a 2 decimales")
        comprobar(respuesta)
        pass

def combinatoria_probabilidad():
    #eleccion = random.choice([1,2,3])
    eleccion = 1
    if eleccion == 1:
        years = random.randrange(5,30,1)
        #respuesta = largo*ancho
        print(f"""Se emitió un documental sobre terremotos y la frecuencia con que éstos ocurren.
                  El documental incluía un debate sobre la posibilidad de predecir los terremotos.
                  Un geólogo afirmó: En los próximos {years} años, hay dos posibilidades por cada 3
                  de que ocurra un terremoto en la ciudad de Zed. """)
        #comprobar(respuesta)
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
