# Create a node
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

# Create your Singly Linked List


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        runner = self.head
        if self.head == None:
            print("List is empty!")
            return self
        elif runner.next == None:
            self.head = None
            return self
        elif runner.next != None:
            self.head = runner.next
            return self

    def remove_from_back(self):
        runner = self.head
        if runner == None:
            print("List is emptyt!")
            return self
        if runner.next == None:
            runner = None
            return self
        second_to_last = runner
        while(second_to_last.next):
            second_to_last = second_to_last.next
        second_to_last.next == None
        return runner


myList = SList()
myList.add_to_front("are")
myList.add_to_front("linked list")
myList.add_to_back("fun!")
myList.remove_from_back()
myList.print_values()
