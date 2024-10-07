class Node:
    def __init__(self, head):
        self.data = head
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def get_element(self, position):
        length = self.__len__()
        if length == 0 or position > length:
            raise ValueError

        current_node = self.head

        for index in range(length):
            if index == position:
                return current_node.data
            current_node = current_node.next

        raise IndexError

    def insertion(self, index, value):
        length = self.__len__()
        new_node = Node(value)
        current_node = self.head

        if length == 0 or index > length:
            raise ValueError

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        if index == length:
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node

        position = 0

        while current_node != None and index != position + 1:
            current_node = current_node.next
            position += 1

        if current_node is not None:
            new_node = Node(value)
            new_node.next = current_node.next
            current_node.next = new_node

    def __len__(self):
        if self.head:
            count = 1
            current_node = self.head

            while current_node.next is not None:
                count += 1
                current_node = current_node.next
            return count
        raise ValueError

    def __str__(self):
        if self.head:
            current_node = self.head
            text = f"[{current_node.data}]"

            while current_node.next is not None:
                text += f"->[{current_node.next.data}]"
                current_node = current_node.next
            return text

        raise ValueError


list = LinkedList()
list.head = Node(2)
list.append(3)
list.append(5)
print(list)
print(len(list))
print(list.get_element(2))
list.insertion(0, 4)
print(list)
