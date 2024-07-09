from funciones import Numero_entero
from funciones import suma_de_listas
from funciones import resta_de_listas
from funciones import multiplicar_listas
from funciones import división_de_listassssss
from funciones import los_16_multiplos


def opciones_ver():
    print("------------------------------------------------------------------")
    print("¡Hola! Por favor escoge una de las opciones siguientes:     |")
    print("1. Saber si un número es entero                                |")
    print("2. Conocer los primeros 16 múltiplos de un número           |")
    print("3. Suma de listas                                              |")
    print("4. Resta de listas                                          |")
    print("5. Multiplicación de listas                                    |")
    print("6. División de listas                                       |")
    print("7. Salir                                                       |")
    print("------------------------------------------------------------------")

def obtener_opciones():
    while True:
        try:
            opcion = int(input("Elija una opción: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Esa opción no está en el menú, elige otra")
        except ValueError:
            print("Elije una opción válida")

def menu_entero():
    while True:
        opciones_ver()
        opción_elegida = obtener_opciones()

        if opción_elegida == 1:
            n = int(input("Coloque un número: "))
            Numero_entero(n)
        elif opción_elegida == 2:
            n = int(input("Digite un número: "))
            los_16_multiplos(n)
        elif opción_elegida == 3:
            lista1 = list(input("Coloque la primera lista ([]): "))
            lista2 = list(input("Coloque la segunda lista ([]): "))
            suma_de_listas(lista1, lista2)
        elif opción_elegida == 4:
            lista1 = list(input("Coloque la primera lista ([]): "))
            lista2 = list(input("Coloque la segunda lista ([]): "))
            resta_de_listas(lista1, lista2)
        elif opción_elegida == 5:
            lista1 = list(input("Coloque la primera lista ([]): "))
            lista2 = list(input("Coloque la segunda lista ([]): "))
            multiplicar_listas(lista1, lista2)
        elif opción_elegida == 6:
            lista1 = list(input("Coloque la primera lista ([]): "))
            lista2 = list(input("Coloque la segunda lista ([]): "))
            división_de_listassssss(lista1, lista2)
        elif opción_elegida == 7:
           print("¡Chau!")
           print("------------------------------------------------------------------")
           break
        else:
            print("Esa no es una opción válida, intenta con otra")

menu_entero()


#LISTOOOOOOOOOOOOOO
