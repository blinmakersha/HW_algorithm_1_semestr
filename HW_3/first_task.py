# с помощью данной функции, мы вясняем является ли связный список палиндромом.
# сложность: O(n).

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # создаём пустую строку, в которую добавим все елементы списка.
        palindrome = ''

        # циклом проходим по каждому элементу и добавляем в строку.
        while head:
            palindrome += str(head.val)
            head = head.next

        # если все элементы строки читаются одинаково слева-направо и
        # справа-налево, то список является палиндромом.
        return palindrome == palindrome[::-1]
