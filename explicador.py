import utilidades as ut
import time 
#En esta parte del código colocamos las definiciones de los temas explicando 
def aritmetica():
    ut.formato("Aritmética","RED",animacion=True)
    time.sleep(1)
    ut.formato("""La aritmética estudia los números y las operaciones básicas que se pueden llevar a cabo entre ellos. 
                  Las operaciones matemáticas más comunes son la suma, la resta, la multiplicación y la división.
                  Las operaciones aritméticas se dividen en dos grupos, las directas y las indirectas.
                  Las operaciones directas son la suma o adición, la cual se representa con el signo +
                  La multiplicación, la cual se representa con los signos x o * .
                  La potenciación, la cual consiste en multiplicar un número por sí mismo n cantidad de veces.
                  Las operaciones indirectas son la resta o sustracción, la cual se representa con el signo -
                  La división, la cual representa la división entre un dividendo y un división
                  La radicación, la cual es el proceso inverso a la potenciación
                  La logaritmación, la cual es de igual manera una operación inversa a la potenciación.""","BLACK","WHITE")
    pass
def algebra():
    ut.formato("Álgebra","RED",animacion=True)
    time.sleep(1)
    ut.formato("""El álgebra es una rama de las matemáticas que utiliza no solo números y signos, sino también letras para resolver operaciones. 
                  En otras palabras, el algebra busca hallar el valor numérico de variables desconocidas o incógnitas.
                  Algunos de los conceptos principales del álgebra son:
                    -Expresión algebraica: expresión de números y letras sometidos a operaciones matemáticas. 
                        Las principales expresiones algebraicas son los monomios (expresiones con un sumando) y 
                        polinomios (expresiones con 2 o más sumandos)
                    -Término: combinación de números y símbolos que representan un número
                    -Factor: cada componente de un término
                    -Coeficiente: el factor vinculado con algún monomio o polinomio
                    -Símbolos: representan cantidades
                    -Grado: Suma de los exponentes de las variables
                    -Signos de agrupación: agrupan términos o expresiones algebraicas,
                        por lo general se utilizan los paréntesis, corchetes y llaves
                    -Variable: un símbolo (por lo general letras del alfabeto) que 
                        representa cualquier número o valor de un conjunto dado y que puede cambiar.""","BLACK","WHITE")
    pass
def geometria():
    ut.formato("Geometría","RED",animacion=True)
    time.sleep(1)
    ut.formato("""La geometría elemental se divide en dos partes, geometría plana (estudia la figuras planas, que tienen únicamente dos dimensiones: largo y ancho)
                  y geometría del espacio (estudia las propiedades de los cuerpos geométricos provistos de largo, ancho y altura o profundidad).
                  Algunos de los conceptos básicos de la geometría son los siguientes:
                    -Punto: el objeto fundamental de la geometría, representa una sola posición y no tiene dimensiones
                    -Recta: únicamente cuenta con longitud, es un conjunto infinito de puntos que se extienden en una dimensión en ambas direcciones
                    -Semirrecta: una porción de una recta que cuenta con principio pero no con un fin
                    -Segmento de recta: porción de una recta con principio y fin
                    -Plano: una superficie en dos dimensiones, cuenta con ancho y largo
                    -Polígonos: figuras planas cerradas que está formada por tres o más segmentos 
                        de recta que se unen en sus puntos extremos. Los polígonos reciben sus 
                        nombres por su cantidad de lados, los más comunes son el triángulo (3 lados)
                        , cuadrilátero (4 lados), pentágono (5 lados), entre otros
                    -Vértices: puntos finales de un segmento
                    -Lados: segmentos de recta que unen dos vértices consecutivos de un polígono 
                    -Diagonal: segmento de recta que une dos vértices no consecutivos
                    -Círculos: figura plana que consiste en todos los puntos que están 
                     sobre una curva cerrada y de los puntos interiores de ella, en la
                     cual cada punto sobre la curva tiene la misma distancia al centro del círculo
                    -Radio de un círculo: la distancia entre el centro y un punto de la curva de un círculo
                    -Diámetro: distancia entre dos puntos de la curva que pasa por el centro del círculo
                    -La Circunferencia es la línea curva cerrada y plana cuyos puntos están a la misma
                      distancia (radio) de un punto (centro)""","BLACK","WHITE")
    pass
def funciones_y_graficas():
    ut.formato("Funciones y gráficas","RED",animacion=True)
    time.sleep(1)
    ut.formato("""Una función es una relación entre un conjunto de salida llamado dominio y un conjunto de llegada llamado codominio,
                  tal relación debe cumplir que cada elemento del dominio se debe relacionar una vez con algún elemento del codominio.
                  La forma de relacionar los elementos en una función está dada por una regla llamada criterio de la función.
                  Un gráfico es el conjunto de pares ordenados en una expresión de x, y. Se representan en un plano cartesiano,
                  el cual es intersección perpendicular de un eje x con un eje y (cada eje tiene una métrica)
                  Elementos de un análisis de gráficas: 
                    -Dominio: los números del eje x que abarca una gráfica.
                    -Rango: Los números del eje y que abarca una gráfica.
                    -Intervalos de monotonía: intervalos del eje x donde la
                        función es estrictamente decreciente, constante o
                        estrictamente creciente.""","BLACK","WHITE")
    pass
def estadistica_descriptiva():
    ut.formato("Estadística Descriptiva","RED",animacion=True)
    time.sleep(1)
    ut.formato("La estadística es un campo de las ciencias que permite deducir y evaluar conclusiones acerca de una población a partir de la información que se encuentra al alcance. La estadística se usa en la recolección, selección, clasificación, interpretación y análisis de datos para la deducción de conclusiones confiables. \nLa estadística descriptiva consiste en resumir, analizar, interpretar y describir datos numéricos mediante el uso de representaciones gráficas como lo son los gráficos (de diferentes tipos) y tablas. \nAlgunos de los elementos básicos de la estadística son los siguientes: \n-Población: Es el conjunto de todos los elementos que presentan una característica común determinada, observable y medible. La población pueden ser personas, grupos u objetos. \n-Muestra: Es un subconjunto de la población, el cual debe presentar el mismo comportamiento y características de la población. \n-Variable: es una característica que se observa en una población o muestra. Las variables se dividen en dos categorías, cuantitativas y cualitativas. Las variables cuantitativas (continuas o discretas) son aquellas que toman valores numéricos y las variables cualitativas (nominal u ordinal) son aquellas que describen cualidades. \n-Obtención de datos: para poder llevar a cabo un análisis estadístico es muy importante contar con los datos necesarios y que además sean confiables, por esa razón existen varios métodos de recolección de datos. Algunos de los métodos de recolección de datos son los siguientes: muestreo Aleatorio simple, muestreo sistemático, muestreo estratificado y muestreo por conglomerado.","BLACK","WHITE")
    pass
def combinatoria_probabilidad():
    ut.formato("Combinatoria probabilidad","RED",animacion=True)
    time.sleep(1)
    ut.formato("La combinatoria estudia las ordenaciones y agrupación de un determinado número de objetos o elementos. La combinatoria puede resultar útil al momento de calcular posibles sucesos que resulten favorables, para después poder aplicar la regla de laplace. La regla de laplace es un método que permite calcular el determinante de una matriz de dimensión 3x3. \nLos conceptos básicos de esta área de las matemáticas son los siguientes: \n-Variaciones: Se pueden visualizar como tener un conjunto con m objetos, tomar de este todos los subconjuntos de n objetos y después ordenarlos de todas las maneras posibles cada subconjunto. La fórmula para calcular las variaciones es Vmn=mm-n \n-Permutaciones: distintas maneras en las que es posible ordenar los elementos de m (cada objeto del conjunto). La fórmula para calcular las permutaciones es Pm = m \n-Combinaciones: m elementos tomados de n en n a todas las agrupaciones posibles que pueden hacerse con los m elementos, de forma que no se consideran todos los elementos, no se repiten los elementos y el orden no importa. La fórmula para calcular las combinaciones es Cmn=VmnPn","BLACK","WHITE")
    pass