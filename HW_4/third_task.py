# с помощью данной функции, мы находим число из последовательности Трибоначчи.
# сложность: O(n2).

def tribonacci(n):
    """

    Args:
        n (int): the number we need to find in tribonacci sequence

    Returns:
        trib[n]: the number, result
    """

    # создаем словарь в котором будем хранить под каждым значением результат.
    trib = {}
    trib[0], trib[1], trib[2] = 0, 1, 1
    for i in range(3, n+1):
        trib[i] = trib[i-1] + trib[i-2] + trib[i-3]
    return trib[n]


print(tribonacci(5))
