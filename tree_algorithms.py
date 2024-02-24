class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Знаходимо найбільше значення у дереві
def search_max(root):
    if root.right:
        return search_max(root.right)
    return root

# Знаходити мінімальне значення у дереві
def search_min(root):
    if root.left:
        return search_min(root.left)
    return root

# Знаходимо суму значень у дереві
def sum_tree(root):
    if root:
        return root.val + sum_tree(root.left) + sum_tree(root.right)
    return 0


# Додаємо набір значень для тестування
root = Node(5)
root = insert(root, 3)
root = insert(root, 10)
root = insert(root, 4)
root = insert(root, 9)
root = insert(root, 2)
root = insert(root, 15)

print(root)

print(f"Найбільше значення у дереві: {search_max(root).val}")
print(f"Найменше значення у дереві: {search_min(root).val}")
print(f"Сума значень у дереві: {sum_tree(root)}")