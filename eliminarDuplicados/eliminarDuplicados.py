def eliminarDuplicados(nums):
    """
    Elimina los elementos duplicados de un arreglo ordenado

    Args:
        A un arreglo ordenado.
    Return:
        El número de elementos unicos en el arreglo
    """


    n = len(nums)
    if n <= 1:
        return n

    unico = 0

    for i in range(1, n):
        if nums[i] != nums[unico]:
            unico += 1
            nums[unico] = nums[i]

    unico = unico + 1

    for j in range(unico, n):
        nums[j] = " "

    return unico


if __name__ =="__main__":
    print(eliminarDuplicados([1, 1, 2, 3, 3, 4])) #4
    print(eliminarDuplicados([5, 5, 5, 6, 7, 7, 8])) #4
    print(eliminarDuplicados([10, 10, 10, 10])) #1
    print(eliminarDuplicados([1, 2, 3, 4, 4, 5, 5, 5])) #5