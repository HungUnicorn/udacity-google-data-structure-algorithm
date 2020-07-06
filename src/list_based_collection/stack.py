class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList"""
        if self.head:
            current = self.head
            self.head = new_element
            new_element.next = current
        else:
            self.head = new_element

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        to_delete = self.head

        if to_delete:
            self.head = to_delete.next
            to_delete.next = None
            return to_delete


class Stack:
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()
