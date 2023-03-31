# с помощью данной функции, мы находим среднее значение цифр на каждом уровне бинарного дерева.
# сложность: O(n)2.

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # исключаем нулевое дерево
        if not root:
            return 0
        root_work = [root]
        res = [root.val]

        # создаем цикл который будет проходить по уровням
        while root_work:
            size = len(root_work)
            l = []

            # создаем вложенный цикл для вычисления значений на каждом уровне
            while size:
                curr = root_work.pop(0)
                size -= 1
                if curr.left:
                    root_work.append(curr.left)
                    l += [curr.left.val]
                if curr.right:
                    root_work.append(curr.right)
                    l += [curr.right.val]

            # добавляем значение результата каждого уровня
            if l:
                avg = sum(l) / len(l)
                res.append(avg)

        return res
