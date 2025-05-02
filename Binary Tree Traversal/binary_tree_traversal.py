def pre_order(node):
    output = []
    def pre_traversal(current):
        if current is not None:
            output.append(current.data)
            pre_traversal(current.left)
            pre_traversal(current.right)
    pre_traversal(node)
    return output

def in_order(node):
    output = []
    def in_traversal(current):
        if current is not None:
            in_traversal(current.left)
            output.append(current.data)
            in_traversal(current.right)
    in_traversal(node)
    return output

def post_order(node):
    output = []
    def post_traversal(current):
        if current is not None:
            post_traversal(current.left)
            post_traversal(current.right)
            output.append(current.data)
    post_traversal(node)
    return output
