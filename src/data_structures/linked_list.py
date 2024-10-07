from typing import Any, Optional


class Node:
    """
    A class representing a single node in a linked list.

    Attributes:
        data (Any): The data stored in the node.
        next (Optional[Node]): The reference to the next node in the list.
    """

    def __init__(self, data: Any) -> None:
        """
        Initializes a new node with given data.

        Args:
            data (Any): The data for the node.
        """
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self) -> None:
        """
        Initializes an empty linked list.
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
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def __len__(self) -> int:
        """
        Returns the number of nodes in the linked list.

        Returns:
            int: The number of nodes in the list.
        """
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string showing the nodes in the list in order, separated by arrows.
        """
        if not self.head:
            return "[]"

        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(f"[{current_node.data}]")
            current_node = current_node.next

        return "->".join(nodes)


# Example usage
ll = LinkedList()
ll.append(2)
ll.append(3)
ll.append(5)
print(ll)  # Output: [2]->[3]->[5]

print(len(ll))  # Output: 3
print(ll.get_element(2))  # Output: 5

ll.insertion(0, 1)
ll.insertion(3, 4)
print(ll)  # Output: [1]->[2]->[3]->[4]->[5]
