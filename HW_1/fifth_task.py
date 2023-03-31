# эта функция находит k-ый по величине элемент в списке. сложность: O(n).

from heapq import heapify       # импортируем необходимые функции
from heapq import heappop

def findKthLargest(nums, k):        # создаем цикл и умножаем каждый элемент в списке на -1, чтобы в дальнейшем получилось сделать через heappop
    for i in range(len(nums)):
        nums[i] *= -1

    heapify(nums)       # в соответствии с документами heapify() выполняется линейное время, а значит нам подойдет. создаем кучу
    result = 0
    while k > 0:
        result = -heappop(nums)      # heappop дает минимальное число из кучи
        # благодаря отрицанию, мы понимаем что это максимальное значение и сохраняем его в result
        k -= 1
        
    return result

print(findKthLargest([6, 5, 4], 3))
