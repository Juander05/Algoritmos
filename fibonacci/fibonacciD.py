def fibonacciD(n, memo={1: 1, 2: 1}):
    """
    Args:
        Posición de la serie
    Return:
        Valor de la poición de la serie  
    """
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacciD(n - 1, memo) + fibonacciD(n - 2, memo)
        return memo[n]

if __name__ == "__main__":

    print(fibonacciD(7)) #13
    print(fibonacciD(10)) #55
    print(fibonacciD(12)) #144
    print(fibonacciD(15)) #610