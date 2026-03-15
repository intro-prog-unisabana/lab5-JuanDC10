def list_shift (lista, valor):
    for i in range (len(lista)):
        lista[i] = lista[i] + valor
def calc_avg(lista):
    suma = 0
    for num in lista:
        suma = suma + num
    promedio = suma / len(lista)
    return promedio
def print_normalized(lista):
    print(lista)
