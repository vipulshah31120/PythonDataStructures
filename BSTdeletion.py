class BinarySearchTreenode :
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data) :
        if data == self.data :              #Removing duplicate elements
            return

        if data < self.data :
                                            #add data in left subtree
            if self.left :
                self.left.add_child(data)
            else :                          #if left tree is empty
                self.left = BinarySearchTreenode(data)
        else :
                                            #add data in right subtree
            if self.right :
                self.right.add_child(data)
            else :                          #if left tree is empty
                self.right = BinarySearchTreenode(data)

    def in_order_traversal(self) :          #returning them in a specific order
        elements = []
        if self.left :                      #visit left tree
            elements += self.left.in_order_traversal() #recursive method
        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right :
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self) :
        if self.right is None :
            return self.data
        return self.right.find_max()

    def find_min(self) :
        if self.left is None :
            return self.data
        return self.left.find_min()

    def delete(self, val) :
        if val < self.data :
            if self.left :
                self.left.delete(val)
        elif val >  self.data :
            if self.right :
                self.right.delete(val)
        else :
            if self.left is None and self.right is None :
                return None
            if self.left is None :
                return self.right
            if self.right is None :
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements) :
    print('Building tree with these elements: ', elements)
    root = BinarySearchTreenode(elements[0])

    for i in range (1, len(elements)) :
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print('After deleting: ', numbers_tree.in_order_traversal())