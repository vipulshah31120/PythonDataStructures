class TreeNode :
    def __init__(self, data) :
        self.data = data                #Data is an element
        self.children = []
        self.parent = None

    def add__child(self, child) :       #Adding a child Node
        child.parent = self
        self.children.append(child)     #We are adding child object to self so, self will become a parent.

    def get_level(self) :               #Printing in hierarchial order
        level = 0
        p = self.parent
        while p :
            level += 1
            p = p.parent
        return level

    def print_tree(self) :
        spaces = '   ' * self.get_level()               #Printing indentation-wise
        prefix = spaces + "|__" if self.parent else ''
        print(prefix + self.data)
        if self.children :
            for child in self.children :
                 child.print_tree()      #Child is also an object of tree node and it has method print_tree()--> It will
                                        #recursively calls the function and print sub-trees.

def build_product_tree() :
    root = TreeNode('Electronics')      #Electronics stored in TreeNode

    laptop  = TreeNode('Laptop')
    laptop.add__child(TreeNode('Mac'))
    laptop.add__child(TreeNode('Lenovo'))
    laptop.add__child(TreeNode('HP'))

    cellphone = TreeNode('Cell Phone')
    cellphone.add__child(TreeNode('Iphone'))
    cellphone.add__child(TreeNode('Google Pixel'))
    cellphone.add__child(TreeNode(' OnePlus'))

    tv = TreeNode('Television')
    tv.add__child(TreeNode('Samsung'))
    tv.add__child(TreeNode('LG'))

    root.add__child(laptop)
    root.add__child(cellphone)
    root.add__child(tv)

    #print(tv.get_leve) --> it will print 1
    return root

if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_level())
    root.print_tree()
    pass