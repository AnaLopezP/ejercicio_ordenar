import random
lista = []

#creamos la tabla aleatoriamente
def crear_lista():
    repe = random.randint(5, 15)
    for i in range(repe):
        num = random.randint(0, 10)
        lista.append(num)
    return lista





crear_lista()
print(lista)