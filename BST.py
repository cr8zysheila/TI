class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        insertPosition = self.root
        while insertPosition:
            if insertPosition.value == new_val:
                return
            elif new_val > insertPosition.value:
                if insertPosition.right:
                    insertPosition = insertPosition.right
                else:
                    insertPosition.right = Node(new_val)
                    return
            else:
                if insertPosition.left:
                    insertPosition = insertPosition.left
                else:
                    insertPosition.left = Node(new_val)
                    return
        

    def search(self, find_val):
        result = self.BSTSearch(self.root, find_val)
        return True if result != None else False
    
    def BSTSearch(self, start, find_val):
        if start == None or start.value == find_val:
            return start
        elif find_val > start.value:
            return self.BSTSearch(start.right, find_val)
        else:
            return self.BSTSearch(start.left, find_val)
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)