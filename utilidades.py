from colorama import*
from tabulate import tabulate
def formato(texto,color="RESET",fondo="RESET"):
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
    return (eval(f"Fore.{color}") if color != None else "")+(eval(f"Back.{fondo}") if color != None else "")+Style.BRIGHT +texto+Fore.RESET+Back.RESET+Style.RESET_ALL

def tabla(c,v):
    tabla = [c]
    try:
        for i in range(0,len(v),2):
            tabla.append([v[i],v[i+1]])
    except IndexError:
        print("Tienes que relacionar un valor con otro")
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
    return print(tabulate(tabla,headers="firstrow",tablefmt="fancy_grid"))





















