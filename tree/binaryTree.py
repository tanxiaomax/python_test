class node:
    def __init__(self,data):
        self.parent = None
        self.data = data
        self.lchild = None
        self.rchild = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self,data):
        new_node = node(data)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            if current_node.data <= new_node.data:
                if current_node.lchild is None:
                    current_node.lchild = new_node
                else:
                    while(current_node is None):
                        parent_node = current_node
                        if current_node.data <= new_node.data:
                            current_node = current_node.lchild
                        else:
                            current_node= current_node.rchild
                        new_node.parent = parent_node
                    current_node = new_node


            else:
                if current_node.rchild is None:
                    current_node.rchild = new_node
                else:
                    while (current_node is None):
                        parent_node = current_node
                        if current_node.data <= new_node.data:
                            current_node = current_node.lchild
                        else:
                            current_node = current_node.rchild
                        new_node.parent = parent_node
                    current_node = new_node






    def inorder(self,node):
        if not node.lchild is None:
            self.inorder(self.root.lchild)
        print(node.data)

        if not node.rchild is None:
            self.inorder(node.rchild)







test_data = [1,3,6,2,3,5,6]

bt = BinaryTree()
for i in test_data:
    bt.insert_node(i)
print(bt.root.lchild.data)
print(bt.inorder(bt.root))







