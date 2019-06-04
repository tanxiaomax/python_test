
class Node:
    def __init__(self,data):
        self.head = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert_node(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp_node = self.head.next;
            while(self.head.next != None):
                temp_node = temp_node.next
            temp_node.next= Node(data)


    def print_node(self):
        if self.head is None:
            print("The link node is null")
        else:
            print(self.head)
            tempNode = self.next
            while(tempNode is not None):
                print(tempNode.head)
                tempNode = tempNode.next

