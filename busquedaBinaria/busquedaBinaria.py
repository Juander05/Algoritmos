# Implementación de la búsqueda binaria en Python
def busquedaBinaria(A, e):
    """
    Busca un elemento en un arreglo ordenado, regresa el indice si lo encuentra y -1 si no.

    Args:
        A un arreglo ordenado.
    Return:
        El indice del elemento en el arreglo si se encontro y -1 si no se encuentra.
    """
    n = len(A)

    if n == 1:
        if A[0] == e:
            return 0
        else:
            return -1
    
    m = n // 2 

    if A[m] == e:
        return m
    if A[m] < e:
        resultado = busquedaBinaria(A[m + 1:], e)
        if resultado != -1:
            return m + 1 + resultado
        else:
            return -1
    else:
        return busquedaBinaria(A[:m], e)
    
if __name__ == "__main__":

    print(busquedaBinaria([1, 3, 5, 7, 9, 11], 7)) #3
    print(busquedaBinaria([2, 4, 6, 8, 10, 12, 14], 5)) #-1
    print(busquedaBinaria([10, 20, 30, 40, 50], 50)) #4