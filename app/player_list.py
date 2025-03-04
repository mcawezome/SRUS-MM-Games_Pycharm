from __future__ import annotations
from player import Player
from player_node import PlayerNode

class PlayerList:
    """A doubly-linked list implementation for managing PlayerNodes.

    The list maintains head and tail pointers and tracks its length.
    """
    def __init__(self) -> None:
        self._head = None
        self._length = 0

    @property
    def is_empty(self) -> bool:
        """Checks if the list contains no nodes.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self._head is None

    @property
    def length(self) -> int:
        """Gets the number of nodes in the list.

        Returns:
            int: The current length of the list.
        """
        return self._length

    @property
    def head(self) -> PlayerNode | None:
        """Gets the first node in the list.

        Returns:
            PlayerNode or None: The head node, or None if list is empty.
        """
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        """Gets the last node in the list.

        Returns:
            PlayerNode or None: The tail node, or None if list is empty.
        """
        return self._tail

    def insert_at_head(self, node: PlayerNode) -> None:
        """Inserts a PlayerNode at the front of the list.

        Args:
            node: The PlayerNode to insert.
        """
        # We are passing nodes rather than values
        # because then input is already sanitised by Player's descriptors.
        if self.is_empty:
            self._head = node
            self._tail = node
            node.next = None  # Ensure node's pointers are set correctly
            node.prev = None
            self._length += 1
            return

        node.next = self._head
        node.prev = None
        self._head.prev = node  # update old head's prev to point to the new node
        self._head = node
        self._length += 1

    def insert_at_tail(self, node: PlayerNode) -> None:
        """Inserts a PlayerNode at the end of the list.

        Args:
            node: The PlayerNode to insert.
        """
        if self.is_empty:
            # For an empty list, new node becomes both head and tail.
            self._head = node
            self._tail = node
            node.next = None  # Ensure node's pointers are set correctly
            node.prev = None
            self._length += 1
            return

        node.prev = self._tail
        node.next = None
        self._tail.next = node
        self._tail = node
        self._length += 1

    def insert_at_position(self, node: PlayerNode, position: int) -> None:
        """Inserts a PlayerNode at a specific position in the list.

        Args:
            node: The PlayerNode to insert.
            position: The position to insert the node at.
        """
        if position < 0 or position > self.length:
            raise IndexError("Invalid position")
        if position == 0:
            self.insert_at_head(node)
            return
        if position == self.length:
            self.insert_at_tail(node)
            return
        current = self._head
        for _ in range(position - 1):
            current = current.next
        node.next = current.next
        node.prev = current
        current.next.prev = node

    def delete_head(self) -> None:
        """Removes the first node in the list.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty:
            raise IndexError("Cannot delete a node from an empty list")
        if self.length == 1:
            self._head = None
            self._tail = None
            self._length -= 1
            return
        # Update the head pointer to the next node.
        new_head = self._head.next
        new_head.prev = None  # New head's prev must be None.
        self._head = new_head
        self._length -= 1

    def delete_tail(self) -> None:
        """Removes the last node in the list.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty:
            raise IndexError("Cannot delete a node from an empty list")
        if self.length == 1:
            self._head = None
            self._tail = None
            self._length -= 1
            return

        # Update the tail pointer to the previous node.
        new_tail = self._tail.prev
        new_tail.next = None
        self._tail = new_tail
        self._length -= 1

    def find_node_with_key(self, key: str) -> PlayerNode | None:
        """Finds the first node with the specified key.

        Args:
            key: The key to search for.

        Returns:
            PlayerNode or None: The first node with the specified key, or None if not found.
        """
        for node in self:
            if node.key == key:
                return node
        return None


    def delete_node_with_key(self, key: str) -> bool:
        """Deletes the first node with the specified key.

        Args:
            key: The key to search for and delete.

        Returns:
            bool: True if a node was found and deleted, False otherwise.
        """
        node = self.find_node_with_key(key)
        if node is not None:
            if node == self._head:
                self.delete_head()
                # delete_head() already decrements length
                return True
            if node == self._tail:
                self.delete_tail()
                # delete_tail() already decrements length
                return True
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                self._length -= 1
                return True
        return False

    def display(self, forward: bool = True) -> None:
        """Prints the list contents to console.

        Args:
            forward: If True, prints from head to tail; if False, tail to head.
        """
        nodes = list(self if forward else reversed(self))
        if not nodes:
            print("Empty list")
            return

        output = " -> ".join(f"{node.key}'{node.name}'" for node in nodes)
        print(output)


    def __iter__(self):
        """Implements forward iteration through the list.

        Yields:
            PlayerNode: Each node in the list from head to tail.
        """
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def __reversed__(self):
        """Implements reverse iteration through the list.

        Yields:
            PlayerNode: Each node in the list from tail to head.
        """
        current = self._tail
        while current is not None:
            yield current
            current = current.prev