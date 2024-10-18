def palindromo(x):
    """
    Args:
        Un número entero n, 1 <= n <=10000
    Return:
        True si es palindromo, false si no  
    """

    if x == 0 or x > 10000:
        return False
    
    if x < 10:
        return True
    
    original = x
    inverso = 0
    ultimo = 0

    while x > 0:
        ultimo = x % 10
        inverso = (inverso * 10) + ultimo
        x = x//10
    
    return original==inverso

if __name__ == "__main__":

    print(palindromo(12321)) # False, es palindromo pero es mayor a 10000
    print(palindromo(1234))  # False
    print(palindromo(22))    # True
    print(palindromo(9))     # True
    print(palindromo(1221))  # True
    print(palindromo(3443))  # True
    print(palindromo(9876))  # False
