from token import CIRCUMFLEX
from typing import Any, Optional


class Node:
    """
    A class representing a single node in a double linked list.

    Attributes:
        data (Any): The data stored in the node.
        next (Optional[Node]): The reference to the next node in the list.
        prev (Optional[Node]): The reference to the previous node in the list.
    """

    def __init__(self, data: Any) -> None:
        """
        Initializes a new node with given data.

        Args:
            data (Any): The data for the node.
        """
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoubleLinkedList:
    """
    A class representing a double linked list.
    """

    def __init__(self) -> None:
        """
        Initializes an empty double linked list.
        """
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        """
        Appends a new node with the specified value at the end of the linked list.

        Args:
            value (Any): The value to be added at the end of the list.

        Returns:
            None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node

    def get_element(self, position: int) -> Any:
        """
        Returns the data of the node at the specified position.

        Args:
            position (int): The zero-based index of the node to retrieve.

        Raises:
            IndexError: If the position is out of bounds.

        Returns:
            Any: The data at the specified position.
        """
        if not 0 <= position < self.__len__():
            raise IndexError("Position out of bounds.")

        current_node = self.head
        for _ in range(position):
            current_node = current_node.next
        return current_node.data

    def insertion(self, index: int, value: Any) -> None:
        """
        Inserts a new node with the specified value at the given index.

        Args:
            index (int): The zero-based index where the new node should be inserted.
            value (Any): The value for the new node.

        Raises:
            IndexError: If the index is out of bounds.

        Returns:
            None
        """
        if not 0 <= index <= self.__len__():
            raise IndexError("Index out of bounds.")

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = self.head
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            if current_node.next:
                current_node.next.prev = new_node

            current_node.next = new_node
            new_node.prev = current_node

    def deletion_by_index(self, index):
        """
        Deletes a node at the specified index.

        Args:
            index (int): The zero-based index of the node to delete.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not 0 <= index <= self.__len__():
            raise IndexError("Index out of bounds.")

        current_node = self.head

        if index == 0:
            self.head = self.head.next

            if self.head:
                self.head.prev = None

        else:
            for _ in range(index):
                current_node = current_node.next

            if current_node.prev:
                current_node.prev.next = current_node.next
            if current_node.next:
                current_node.next.prev = current_node.prev

    def __len__(self) -> int:
        """
        Returns the number of nodes in the double linked list.

        Returns:
            int: The number of nodes in the double linked list.
        """
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self) -> str:
        """
        Returns a string representation of the double linked list.

        Returns:
            str: A string showing the nodes in the double link list in order, separated by arrows.
        """
        if not self.head:
            return "[]"

        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(f"[{current_node.data}]")
            current_node = current_node.next

        return "<->".join(nodes)


# Example usage
dll = DoubleLinkedList()

dll.append(2)
dll.append(3)
dll.append(5)
print(dll)  # Output: [2]<->[3]<->[5]
print(dll.head.next.prev.data)  # Output: 2

print(len(dll))  # Output: 3
print(dll.get_element(2))  # Output: 5

dll.insertion(0, 1)
dll.insertion(3, 4)
print(dll)  # Output: [1]->[2]->[3]->[4]->[5]
print(dll.head.next.prev.data)  # Output: 1
print(dll.head.next.next.next.next.prev.data)  # Output: 4


dll.deletion_by_index(0)
dll.deletion_by_index(2)
dll.deletion_by_index(2)

print(dll)  # Output: [2]<->[3]
