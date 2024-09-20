def sumarPares(A):
    """
    Suma todos los números pares en una matriz A de tamaño n x n.

    Args:
        A Lista de listas que representa una matriz cuadrada.
    Return:
        Suma de todos los números pares en la matriz.
    """
    suma = 0
    n = len(A) 
    
    for i in range(n):
        for j in range(n):
            if A[i][j] % 2 == 0:
                suma += A[i][j]
                
    return suma

if __name__ == "__main__":
    
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    resultado1 = sumarPares(matriz1)
    print(f"Ejemplo 1 - Suma de pares: {resultado1}") #20

    matriz2 = [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]
    resultado2 = sumarPares(matriz2)
    print(f"Ejemplo 2 - Suma de pares: {resultado2}") #90

    matriz3 = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    resultado3 = sumarPares(matriz3)
    print(f"Ejemplo 3 - Suma de pares: {resultado3}") #0 