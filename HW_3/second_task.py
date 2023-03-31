# с помощью данной функции, мы берем число в двоичной системе исчеслений и переводим в обычную.
# сложность: O(n).

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        # создаём нулевую переменную, в которую добавим результат.
        ans = 0

        # проходим по каждому элементу в цикле и находим значение числа.
        while head:
            ans = head.val + 2 * ans
            head = head.next
        return ans
