class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_afternode(self, data, prev_node):

        if not prev_node:
            print("sorry we can't insert without prev_data")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


llist = Linkedlist()
llist.append("a")
llist.append("b")
llist.print_list()
