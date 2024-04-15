class Node:
    def __init__(self, item=0):
        self.key = item
        self.left, self.right = None, None


class Ordenamiento:
    def insert(self, key, root):
        if root is None:
            root = Node(key)
            return root

        if key < root.key:
            root.left = self.insert(key, root.left)
        elif key > root.key:
            root.right = self.insert(key, root.right)

        return root

    def inorder_rec(self, root):
        if root is not None:
            self.inorder_rec(root.left)
            
            self.inorder_rec(root.right)

    def tree_sort(self, arr):
        root = None
        for i in range(len(arr)):
            root = self.insert(arr[i], root)

        self.inorder_rec(root)
