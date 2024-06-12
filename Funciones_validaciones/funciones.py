#Numeros enteros naturales
def Numero_entero (n):
    if type (n) == int and n > 0 and n % 1 == 0:
        return True
    return False
# Primera validación CORRECTA (NO MOVER NADA POR FAVORRRR)

#Los 16 multiplos
def los_16_multiplos (n):
    if Numero_entero(n):
        return [n * i for i in range(16, 0, -1)]
#Segunda validación correcta NO TOCARRRRRRRR

#Suma de listas decimales
def suma_de_listas (lista1, lista2):
    if len(lista1) != len(lista2):
        return print("Las listas son de diferente tamaño, revisa y vuelve a intentarlo")
    else:
        print(lista1 + lista2)
print (suma_de_listas([18, 3, 24], [2, 17, 6]))
