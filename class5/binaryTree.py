class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.right = Node(100)
root.left.right.left = Node(-2)


def dfs(node:Node):
    if not node:
        return

    # print(node.value) # Preorder (VLR)
    dfs(node.left)
    # print(node.value) # Inorder (LVR)
    dfs(node.right)
    print(node.value) # Postorder (LRV)

# dfs(root)

def bfs(root:Node):
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        print(node.value)

# bfs(root)

def countBFS(root:Node):
    queue = [root]
    count = 0

    while queue:
        node = queue.pop(0)
        count += 1
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return count

# print(countBFS(root))


def countDFS(node:Node):
    if not node:
        return 0

    leftNum = countDFS(node.left)
    rightNum = countDFS(node.right)

    return leftNum + rightNum + 1

print(countDFS(root))