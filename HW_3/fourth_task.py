# импортируем модуль, который возвращает новый объект из итерируемой последовательности.
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # исключаем пустой grid
        if not grid:
            return 0

        # создаем необходимые переменные
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def search(r, c):
            
            # создаем пустую очередь
            q = deque()
            
            # добавляем в посещенные точку
            visited.add((r, c))
            
            # добавляем в очередь точку
            q.append((r, c))

            # циклом проходим по очереди
            while q:
                row, col = q.pop()
                
                # выбираем точки, которые будем проверять на наличие островов
                directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # используем цикл для нахождения островов
                for dr, dc in directs:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        # применим рекурсию, чтобы проверить все точки
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    search(r, c)
                    islands += 1
        return islands
