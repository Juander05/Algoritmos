def devolverPalabra(s):
    n = len(s)

    if n <= 0:
        return ""
    
    p = n - 1

    while p >= 0 and s[p] !=" ":
        p = p-1
    return s[p+1:n]

if __name__ == "__main__":

    print(devolverPalabra("hola mundo"))
    print(devolverPalabra("hola"))