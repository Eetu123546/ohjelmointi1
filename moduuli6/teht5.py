
def karsii(lista):
    lista2 = lista
    for i in lista:
        if i % 2 != 0:
            lista2.remove(i)
    return lista2

a =[1, 2, 3, 4, 5, 6 ,7]

print(a)

print(karsii(a))