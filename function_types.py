def list_shift (lista, valor):
    for i in range (len(lista)):
        lista[i] = lista[i] + valor
def calc_avg (lista):
    sum = 0
    for num in lista:
        suma = num + sum
        promedio = suma / len(lista)
    return promedio
