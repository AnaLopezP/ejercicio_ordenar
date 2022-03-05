import random
lista = []

#creamos la tabla aleatoriamente
def crear_lista():
    repe = random.randint(5, 15)
    for i in range(repe):
        num = random.randint(0, 10)
        lista.append(num)
    return lista


#funcion que ordena la lista por insercion dicotomica
def ordenar_lista(lista, i):
    prov = 0
    if i < len(lista):
        prov = lista[i]
        lista.pop(i)
        if prov >= lista[i - 1]:
            lista.insert(i, prov)
        else:
            lista.insert(i - 1, prov)
            if lista[i - 2] >= lista[i - 1] and i > 1:
                ordenar_lista(lista, i - 1)
            else:
                ordenar_lista(lista, i)
    else:
        return lista
    ordenar_lista(lista, i + 1)
    return lista


#codigo principal
crear_lista()
print(lista)
ordenar_lista(lista, 0)
print(lista)