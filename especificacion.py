import random
lista = []

#hacemos la funcion que crea la lista aleatoriamente
def crear_lista():
    repe = random.randint(5, 15)
    for i in range(repe):
        num = random.randint(0, 10)
        lista.append(num)
    return lista

#hacemos una funcion que separa un segmento
def segmentos(lista, i):
    if lista[i] >= lista[i + 1]:
        segmento.append(lista[i])
        segmentos(lista, i + 1)
    else:
        segmento.append(lista[i])
    return segmento


#codigo principal
crear_lista()
print(lista)
segmento = []
segmento = segmentos(lista, 0)
print(segmento)            