from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    if root is None:
        return []
    result = []
    nodes_to_visit = deque()
    nodes_to_visit.append(root)
    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()
        result.append(current_node.value)
        if current_node.left is not None:
            nodes_to_visit.append(current_node.left)
        if current_node.right is not None:
            nodes_to_visit.append(current_node.right)
    return result