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

    def search(self, val) :
        if self.data == val :
            return True

        if val < self.data :                        #Value might be in left subtree
            if self.left :
                return self.left.search(val)
            else :
                return False

        if val > self.data :                        #Value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements) :
    root = BinarySearchTreenode(elements[0])
    for i in range (1, len(elements)) :
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 9]      #Return in the for of set
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))

