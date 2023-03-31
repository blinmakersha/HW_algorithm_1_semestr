# с помощью данной функции, мы находим оптимальные по цене билеты в города А и Б.
# сложность: O(n log n).

def twoCitySchedCost(costs):
    """
    Returns:
        res: the sum of prices for the tickets
    """

    # сортируем списки в списке costs, через разницу первого и второго элемента.
    costs.sort(key=lambda x: x[0]-x[1])

    # делим нацело длину списка costs.
    half = len(costs) // 2
    res = 0

    # через цикл добавляем самые оптимальные по цене билеты.
    for el in costs:
        half -= 1
        if half < 0:
            res += el[1]
        else:
            res += el[0]
    return res


print(twoCitySchedCost([[259, 770], [448, 54],
                        [926, 667], [184, 139],
                        [840, 118], [577, 469]]))
