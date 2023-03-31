# с помощью данной функции, мы можем вычислить кол-во всевозможных ходов для робота.
# разделяем задачу на подзадачи, пользуемся динамическим программированием. сложность: O(m * n).

class Solution:
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # создаем массив размера m * n, для хранения уже вычисленного кол-ва путей с индексами (i, j)
        # где обязательно 0 <= i < m и 0 <= j < n
        # инициализируем массив со значением -1, потому что число путей может быть только целым числом.
        dp = [[0] * n for _ in range(m)]
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        # инициализируем первую строку, первый столбец
        # присвоим значению доступного путя = 1 и препятствию = 0
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1
            else:
                0
            
        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1:
                dp[0][j] = 1
            else:
                0
        
        # если нету препятствий, добавляем доступный путь
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]
