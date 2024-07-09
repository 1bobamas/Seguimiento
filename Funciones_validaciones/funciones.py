#-------------------------------------Encabezado chido-------------------------------------#

#Numeros enteros naturales
def Numero_entero(n):
    if type(n) == int and n > 0 and n % 1 == 0:
        return True
    return False


# Primera validación CORRECTA (NO MOVER NADA POR FAVORRRR)

#-------------------------------------Separador chido-------------------------------------#

#Los 16 multiplos
def los_16_multiplos(n):
    if Numero_entero(n):
        return [n * i for i in range(16, 0, -1)]

#Segunda validación correcta NO TOCARRRRRRRR

#-------------------------------------Separador chido-------------------------------------#

#Suma de listas decimales
def suma_de_listas(lista1, lista2):
    suma_total = [l1 + l2 for l1, l2 in zip(lista1, lista2)]
    if len(lista1) != len(lista2):
        return print("Las listas son de diferente tamaño, revisa y vuelve a intentarlo")
    else:
        print(suma_total)

# No tocar, lo poco que he hecho ha sido con sudor y lágrimas (ESTA PORQUERIA ESTA ¡MALA! (No sé))

 # Voy a esperar a mi mami para que me ayude con esto xD (Plan cancelado (Creo))
 # ¡¡¡Ajajaja si pude con esto!!!

#-------------------------------------Separador chido-------------------------------------#

#¡¡RESTA!!
def resta_de_listas(lista1, lista2):
    resta_total= [l1 - l2 for l1, l2 in zip(lista1, lista2)]

    if len(lista1) != len(lista2):
        return print("Las listas son de diferente tamaño, revisa y vuelve a intentarlo")
    else:
        print(resta_total)


# Lo mismo que la suma pero le pongo simbolos de restar y pa´fueraaaa

#-------------------------------------Separador chido-------------------------------------#

#Multiplicación
def multiplicar_listas(lista1, lista2):
    producto_total= [l1 * l2 for l1, l2 in zip(lista1, lista2)]

    if len(lista1) != len(lista2):
        return print("Las listas son de diferente tamaño, revisa y vuelve a intentarlo")
    else:
        print(producto_total)


# NO TOCAR NADA POR FAVOR POR QUE CASI QUE NO HAGO ESTO

#-------------------------------------Separador chido-------------------------------------#

# División - Validación de ceros

def validación (lista1, lista2):
    if lista1 == 0 or lista2 == 0:
        return False
    else:
        return True

# División
def división_de_listassssss(lista1, lista2):
    cociente = [l1 / l2 for l1, l2 in zip(lista1, lista2)]

    if len(lista1) != len(lista2):
        return print("Las listas son de diferente tamaño, revisa y vuelve a intentarlo")
    else:
        print(cociente)


#-------------------------------------Separador chido-------------------------------------#

#Diccionario :D

diccionario_resultados = {Numero_entero, los_16_multiplos, suma_de_listas, resta_de_listas, multiplicar_listas, división_de_listassssss}



#-------------------------------------Separador chido-------------------------------------#

# Tamaño de listas :>

#if len(lista1) != len(lista2):
# (Esto lo apliqué a todas las operaciones, asi que creo que aqui sobra y por eso lo pongo como comentario jajajaja)

# QUE LE PASO AL CURSORRRR, SE VE RARISIMO JAJAJAJAJA