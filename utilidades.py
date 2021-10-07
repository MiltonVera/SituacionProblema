from colorama import*
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
    return (eval(f"Fore.{color}") if color != None else "")+(eval(f"Back.{fondo}") if color != None else "")+texto+Fore.RESET+Back.RESET














