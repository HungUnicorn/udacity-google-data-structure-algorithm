"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
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

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None

        counter = 1
        current = self.head

        while current and counter <= position:
            if position == counter:
                return current
            counter += 1
            current = current.next
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        previous = self.head

        if position > 1:
            while current and counter < position:
                previous = current
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

        previous.next = new_element
        new_element.next = current

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None

        while value != current.value and current.next:
            previous = current
            current = current.next

        if previous:
            previous.next = current.next
        else:
            self.head = current.next
