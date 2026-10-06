class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def evaluate(root):
    if root.left is None and root.right is None:
        return int(root.data)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.data == '+':
        return left + right
    elif root.data == '-':
        return left - right
    elif root.data == '*':
        return left * right
    elif root.data == '/':
        return left / right


# Create expression tree
root = Node('+')

root.left = Node('*')
root.right = Node('-')

root.left.left = Node('3')
root.left.right = Node('4')

root.right.left = Node('8')
root.right.right = Node('2')

print("Expression: (3 * 4) + (8 - 2)")
print("Result:", evaluate(root))
