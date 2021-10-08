from colorama import*
from time import sleep
from tabulate import tabulate
def formato(texto,color="RESET",fondo="RESET",animacion=False):
    """Colores disponibles de usar
    BLACK
    RED
    GREEN
    YELLOW
    BLUE
    MAGENTA
    CYAN
    WHITE

    Si quieres los valores en su color claro le pones LIGHT al principio y al final le pones _EX. Ejemplo
    LIGHTBLUE_EX

    Ejemplo de uso

    formato("Tu texto","BLUE") Este solo le da color al texto
    formato("Tu texto","BLUE","RED") Este solo le da un color azul al texto y un fondo rojo
    """
    init()
    if(animacion):
        return mecanografiar((eval(f"Fore.{color}") if color != None else "")+(eval(f"Back.{fondo}") if color != None else "")+Style.BRIGHT +texto+Fore.RESET+Back.RESET+Style.RESET_ALL)
    else:
        return (eval(f"Fore.{color}") if color != None else "")+(eval(f"Back.{fondo}") if color != None else "")+Style.BRIGHT +texto+Fore.RESET+Back.RESET+Style.RESET_ALL

def tabla(c,v):
    '''Uso de la funcion tabla
    Para estar esta funcion debes de proporcionar en el primer argumento los titulos de la tabla
    y en el segundo argumento los datos que deben de ir en ella
    
    Un ejemplo del uso de este funcion es
    tabla(["x","y"],[1,2,3,4])
    
    El el primer argumento son los titulos de la tabla
    y vemos como los datos de la lista estan relacionados. El 1 con el 2, el 3 con el 4, etc

    ╒═════╤═════╕
    │   x │   y │
    ╞═════╪═════╡
    │   1 │   2 │
    ├─────┼─────┤
    │   3 │   4 │
    ╘═════╧═════╛
    '''
    tabla = [c]
    try:
        for i in range(0,len(v),2):
            tabla.append([v[i],v[i+1]])
    except IndexError:
        print("Tienes que relacionar un valor con otro")
    
    return print(tabulate(tabla,headers="firstrow",tablefmt="fancy_grid"))

def mecanografiar(texto):
    for palabras in texto.split():
        sleep(0.15)
        print(palabras, end=' ', flush=True)
    print()





















