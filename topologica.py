tareas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
restricciones = [(1, 2), (2, 4), (3, 4), (5, 8), (7, 9), (9, 4), (3, 1)]
completadas = []

#esta funcion mira que tareas tienen restricciones y cuantos son, y los añade a una lista auxiliar
def precedentes(t):
    retorno = []
    for j in range(len(restricciones)):
        res = restricciones[j]
        if t == res[1]:
            retorno.append(res[0])
    return retorno



#codigo principal
while len(completadas) < len(tareas):
    for i in range(len(tareas)):
        t = tareas[i]
        prec = precedentes(t)
        if t not in completadas:
            if len(prec) == 0:
                completadas.append(t)
            elif ejecutadas(prec) == True:
                completadas.append(t)
print(completadas)