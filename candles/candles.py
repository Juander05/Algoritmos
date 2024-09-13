def candles(a: list[int]) -> int:
    """
    Args:
        a (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """

    masAlta = 0
    total = 0

    for i in range (len(a)):
        if a[i] > masAlta:
            masAlta = a[i]
            total = 1
        elif a[i] == masAlta:
                total+=1
    return total
    

if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1