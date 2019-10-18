class BinarySearchNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __traverse__(self):
        pass

    def insert(self, value):
        new_node = BinarySearchNode(value)

        if not self.root:
            self.root = new_node
            return self

        current_node = self.root

        while(True):
            if(value < current_node.value):

                if not current_node.left_node:
                    current_node.left_node = new_node
                    return self

                current_node = current_node.left_node
            else:
                if not current_node.right_node:
                    current_node.right_node = new_node
                    return self

                current_node = current_node.right_node

    def lookup(self, value):
        if not self.root:
            return False

        current_node = self.root

        while(current_node):
            if(value < current_node.value):
                current_node = current_node.left_node
            elif value > current_node.value:
                current_node = current_node.right_node
            else:
                return current_node.value

        return False
