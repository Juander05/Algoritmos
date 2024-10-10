def fibonacciR(n):
    """
    Args:
        Posición de la serie
    Return:
        Valor de la poición de la serie  
    """
    if n < 3:
        return 1
    else:
        return fibonacciR(n - 1) + fibonacciR(n - 2)

if __name__ == "__main__":

    print(fibonacciR(7)) #13
    print(fibonacciR(10)) #55
    print(fibonacciR(12)) #144
    print(fibonacciR(15)) #610