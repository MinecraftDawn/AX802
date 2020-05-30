from Tree import Node

root = Node(100)

node = Node(5)
root.childs.append(node)
node = Node(80)
root.childs.append(node)

print(root.value)
print(root.childs[0].value)
print(root.childs[1].value)