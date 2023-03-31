# с помощью данной функции, мы находим минимальную разность между
# цифрами бинарного дерева поиска.
# сложность: O(n).

def getMinimumDifference(root):
    """

    Args:
        root (Optional[TreeNode]): binary tree node

    Returns:
        min_dist: minimum difference between nodes 
    """
    stack, visited = [root], [root.val]

    # проходим по дереву, и добавляем все значения в visited.
    while stack:
        curr = stack.pop()
        if curr.left:
            visited.append(curr.left.val)
            stack.append(curr.left)
        if curr.right:
            visited.append(curr.right.val)
            stack.append(curr.right)

    # задаём минимальную дистанцию как бесконечность.
    min_dist = float('Inf')

    # сортируем наш список в порядке возрастания.
    visited.sort()

    # проходясь циклом, находим минимальную разность.
    for i in range(len(visited)-1):
        dist = abs(visited[i+1]-visited[i])
        min_dist = min(min_dist, dist)

    return min_dist
