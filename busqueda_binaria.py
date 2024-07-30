
lista = [4,1,2,6,8,10,3,5,7,9]
lista.sort()
print(lista)

numero = int(input("Introduce el número a buscar: "))

def busqueda_binaria(numero):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        
        puntero = (inicio + fin) // 2
        
        if numero == lista[puntero]:
            return puntero
        elif numero > lista[puntero]:
            inicio = puntero + 1
        else:
            fin = puntero - 1
    return None

resultado = busqueda_binaria(numero)

if resultado is None:
    print(f"El numero {numero} no se encontro")
else:
    print(f"El numero {numero} está en la posición {resultado}")
