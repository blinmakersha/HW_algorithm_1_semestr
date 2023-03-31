# с помощью данной функции, мы находим периметр всех имеющихся островов на карте.
# сложность: O(m * n).

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # задаем переменную для результата
        perimeter = 0

        # создаем переменные для колонок и рядов
        height, weight = len(grid), len(grid[0])

        # циклами проходим по всем элементам на карте
        for row in range(height):
            for column in range(weight):

                # присваиваем каждому острову периметр 4
                if grid[row][column]:
                    perimeter += 4

                    # если над островом есть еще остров, то вычитаем 2
                    if row and grid[row-1][column]:
                        perimeter -= 2

                    # если слева острова есть еще остров, то вычитаем 2
                    if column and grid[row][column-1]:
                        perimeter -= 2

        return perimeter
