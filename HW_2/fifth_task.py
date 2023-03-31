# данная функция возвращает кол-во периодов плавного спуска цен.
# сложность: O(n).

def getDescentPeriods(prices):

    # создадим список равный длине списка цен. 
    dp = [1] * len(prices)

    # пройдем циклом и найдем самый длинный плавно убывающий подмассив.
    for i in range(1, len(prices)):
        if prices[i] == prices[i-1] - 1:
            dp[i] = 1 + dp[i-1]

    # возвращаем сумму нашего списка dp    
    return sum(dp)

print(getDescentPeriods([3,2,1,4]))
