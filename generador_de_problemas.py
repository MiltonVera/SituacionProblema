import random
import time
import math
import utilidades as ut
import matplotlib.pyplot as plt
from os import system

def comprobar(respuesta):
    if(respuesta != int(input("Introduce tu respuesta --> "))):
        ut.mecanografiar(f"Respuesta incorrecta, la respuesta correcta es {respuesta}")
        return 0
    else:
        ut.mecanografiar(f"Felicidades tu respuesta es correcta")
        return 100


def aritmetica():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        largo = random.randrange(50,100,1)
        ancho = random.randrange(20,70,1)
        respuesta = largo*ancho
        print(f"""Para un concierto de rock se reservo un area de {largo}m de largo y {ancho}m de ancho.
                  Determina cual es la cantidad de personas que caben en el terreno si cada persona ocupa un metro de espacio""")
        return comprobar(respuesta)
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
        return comprobar(respuesta)
        time.sleep(1)
        pass
    elif eleccion == 3:
        cantidad = random.randrange(100,700,5)
        respuesta = cantidad*0.6
        print("""La receta para preparar 100ml de aliño es""")
        ut.tabla(["Ingredientes","Cantidad"],["Aceite para ensalada","60ml","Vinagre","30ml","Salsa de soja","10ml"])
        print(f"""¿Cuantos mililitros de aceite para ensalda necesita para preparar {cantidad}ml de este aliño?""")
        return comprobar(respuesta)
        pass
    elif eleccion == 4:
        c1 = random.randrange(40000,100000,100)
        c2 = random.randrange(40000,100000,100)
        c3 = random.randrange(40000,100000,100)
        c4 = random.randrange(40000,100000,100)
        c5 = random.randrange(40000,100000,100)
        respuesta = (c1+c2+c3+c4+c5)*.2
        print(f"Una empresa cobra el 20% sobre los ingresos mensulaes de 5 negocios, los ingresos de este mes de las franquicias son {c1},{c2},{c3},{c4}, y {c5}.")
        print("¿Cuánto recibió la empresa en total este mes?")
        comprobar(respuesta)
        pass

def algebra():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        ml = random.randrange(50,200,1)
        respuesta = ml*.2
        print(f"Se tienen {ml} mililitros de un químico con una concentración de 30% de ácido.")
        print("¿Cuántos mililitros se deben de añadir para subir su concentración de ácido al 50%?")
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
        return comprobar(respuesta)
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
        return comprobar(respuesta)
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
        return comprobar(respuesta)
        pass

    elif eleccion == 2:
        altura =  random.randrange(140,160,5)
        diametro =  random.randrange(120,140,10)
        altura_centro = (diametro/2) + (altura-diametro)
        respuesta = altura_centro
        print(f"Una noria tiene un diámetro exterior de {diametro} metros y el su punto más alto se encuentra a {altura} metros del suelo")
        print("¿A qué altura se encuentra el centro de la noria con respecto al suelo?")
        return comprobar(respuesta)
        pass

    elif eleccion == 3:
        personas_por_min = 24
        mints = random.randrange(20,40,2)
        respuesta = personas_por_min * mints
        print("""Una puerta giratoria consta de tres hojas que giran dentro de un espacio circular. 
                 El diámetro del círculo es de 2 metros y las 3 hojas de la puerta dividen el espacio
                 en tres sectores iguales.""")
        print(f"""Si la puerta da 4 vueltas por minuto y en cada sector hay espacio para 2 personas, 
                  ¿Cuál es el número máximo de personas que pueden entrar en el edificio por la puerta
                  en {mints} minutos?""")
        return comprobar(respuesta)
        pass
    elif eleccion == 4:
        ancho = random.randrange(20,50,5)
        largo = random.randrange(60,100,5)
        respuesta = (ancho*3)+(largo*3)
        print(f"Se tiene un terreno de {ancho} metros de ancho por {largo} metros de largo, y se quiere poner una cerca alrededor, pero también se quiere dividir en 4 partes iguales desde el centro")
        print("¿Cuántos metros de cerca se necesitan?")
        comprobar(respuesta)
        pass

def funciones_y_graficas():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        robos1 = random.randrange(300,500,10)
        robos2 = random.randrange(600,800,10)
        respuesta = 1
        print("Un presentador de TV mostro el siguiente gráfico y dijo:") 
        ut.graficar(["Año 1988","Año 1999"],[robos1,robos2],tipo="bar")
        ut.mecanografiar("El gráfico muestra que hay un enorme aumento del numero de robos comparando 1988 con 1999")
        ut.mecanografiar("Si estas de acuerdo con el presentador introduce 1, si no introduce 2")
        return comprobar(respuesta)
        pass
    elif eleccion == 2:
        multiplicador = random.randrange(1,6,1)
        x = [x*multiplicador for x in range(10)]
        y = [i**2 for i in x]
        respuesta = 1
        print("""Un coche acelera a velocidad a velocidad acelerada, 
                 a continuacion se te mostrara una grafica y deberas
                 indicar si la grafica va de acorde con el movimiento del
                 vehiculo""")
        ut.graficar(x,y)
        print("Para de cir que si escribe 1 para decir que no escribe 0")
        return comprobar(respuesta)
    elif eleccion == 3:
        print("""A continuacion se te mostraran 4 graficas,
                 despues de verla tienes que definir cual es
                 la logaritmica""")
        system("pause")
        respuesta = 4
        fig, axs = plt.subplots(2,2)
        x = [x for x in range(1,10)]

        y = []
        y.append([i**4 for i in x])
        y.append([i for i in x])
        y.append([10 for i in x])
        y.append([math.log(i,10) for i in x])

        axs[0,0].plot(x,y[0])
        axs[0,0].set_title("Grafica 1")
        axs[0,1].plot(x,y[1])
        axs[0,1].set_title("Grafica 2")
        axs[1,0].plot(x,y[2])
        axs[1,0].set_title("Grafica 3")
        axs[1,1].plot(x,y[3])
        axs[1,1].set_title("Grafica 4")

        plt.show()

        print("Selecciona la opcion correspondiente a la grafica logaritmica")
        ut.tabla(["Grafica","Opcion"],["Grafica 1",1,"Grafica 2",2,"Grafica 3",3,"Grafica 4",4])
        return comprobar(respuesta)
        

def estadistica_descriptiva():
    eleccion = random.choice([1,2])
    if eleccion == 1:
        examen_5 = random.randrange(70,100,10)
        media = ((60*4)+examen_5)/5
        respuesta = round(media,2)
        print(f"""En el colegio de Mariana, los exámenes se puntúan del 0 al 100 y todos tienen el mismo peso en la calificación final. 
                  Si en sus primeros 4 exámenes la media de calificación de Mariana es de 60 puntos y en su 5 examen obtiene un {examen_5}.""")
        print("¿Cuál será la media de calificaciones de Mariana después de los 5 exámenes? (Redondea a 2 decimales)")
        return comprobar(respuesta)
        pass

    elif eleccion == 2:
        estatura_nueva = random.randrange(110,150,10)
        media = ((130*24) + estatura_nueva) / 25
        respuesta = round(media,2)
        print(f"""En una clase hay 25 chicas. En su clase de educación física les piden calcular
                  su estatura media pero ese día faltó una chica a la clase. La estatura media de las 24 chicas es de 130 cm. 
                  Al siguiente dia miden a la chica que faltó y su estatura es de {estatura_nueva} cm. """)
        print("¿Cuál es la estatura media de la clase? (Redondea a 2 decimales")
        return comprobar(respuesta)
        pass
    elif eleccion == 3:
        final = random.randrange(50,80,5)
        respuesta = 0
        while ((final*4)+respuesta)/5!=60:
            respuesta = respuesta+5
        print(f"Raúl lleva un promedio de {final} en 4 exámenes, pero todavía le falta hacer un quinto examen")
        print("¿Cuánto necesita sacar en para tener 6 cerrado de promedio final?")
        comprobar(respuesta)
        pass

def combinatoria_probabilidad():
    eleccion = random.choice([1,2,3])
    if eleccion == 1:
        years = random.randrange(5,30,1)
        respuesta = math.floor((2/3)*years)
        print(f"""Se emitió un documental sobre terremotos y la frecuencia con que éstos ocurren. 
                  El documental incluía un debate sobre la posibilidad de predecir los terremotos.
                  Un geólogo afirmó: En los próximos {years} años, hay dos posibilidades por cada 
                  3 de que ocurra un terremoto en la ciudad de Zed. """)
        print("¿En qué año a partir de ahora habrá un terremoto en la Ciudad de Zed?")
        comprobar(respuesta)
        time.sleep(1)

    elif eleccion == 2:
            playeras = random.randrange(3,15,1)
            pantalones = random.randrange(1,5,1)
            respuesta = math.floor(((math.factorial(playeras))/math.factorial(playeras-1))*((math.factorial(pantalones))/math.factorial(pantalones-1)))
            print(f"En un armario hay {playeras} playeras y {pantalones} pantalones.") 
            print("¿De cuántas formas nos podemos vestir?")
            comprobar(respuesta)
            time.sleep(1)
            pass

    elif eleccion == 3:
        panel = random.randrange(2,8,1)
        cifras = random.randrange(2,5,1)
        respuesta = panel**cifras
        print(f"Hay un panel con {panel} números, y la contraseña es de {cifras} cifras.")
        print("¿Cuántas contraseñas distintas se pueden crear si los números se pueden repetir?")
        comprobar(respuesta)
        time.sleep(1)
        pass