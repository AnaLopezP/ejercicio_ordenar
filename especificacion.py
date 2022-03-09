import random
lista = []

#hacemos la funcion que crea la lista aleatoriamente
def crear_lista():
    repe = random.randint(5, 20)
    for i in range(repe):
        num = random.randint(0, 20)
        if num not in lista:
            lista.append(num)
    return lista

#hacemos una funcion que separa un segmento
def segmentos(lista, i):
    segmento = []
    segmento.append(lista[i])
    while (len(lista) > 1) and (lista[i] >= lista[i + 1]):
        segmento.append(lista[i + 1])
        lista.pop(i + 1)
    lista.pop(i)
    return segmento

#funcion que hace una lista con todos los segmentos de la lista
def seg_lista(lista, grupoSegmentos):
    while len(lista) > 1:
        segmento = []
        segmento = segmentos(lista, 0)
        print(segmento)
        grupoSegmentos.append(segmento)
        print(" Esta es la lista que queda " + str(lista))
    return grupoSegmentos

#funcion que pasa el elemento mas grande del segmento al final de este
def ordenar_seg(segmento):
    num = segmento.pop(0)
    segmento.append(num)
    return segmento

#codigo principal
crear_lista()
print(lista)
grupoSegmentos = []
grupoSegmentos = seg_lista(lista, grupoSegmentos)
print(grupoSegmentos)
while len(grupoSegmentos) > 0:
    segmento = grupoSegmentos.pop(0)
    segmento = ordenar_seg(segmento)
    print(segmento)





