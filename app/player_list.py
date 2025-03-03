from __future__ import annotations
from player import Player
from player_node import PlayerNode

class PlayerList:
    """PlayerList object. Implementation of a double-linked list of PlayerNodes"""
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def is_empty(self) -> bool:
        return self._head is None

    @property
    def length(self) -> int:
        return self._length

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail

    def insert_at_head(self, node: PlayerNode) -> None:
        """Add a PlayerNode to the front of the PlayerList"""
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
        """Add a PlayerNode to the back of the list"""
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

    def delete_head(self) -> None:
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

    def delete_node_with_key(self, key: str) -> bool:
        """
        Deletes the first node in the list with a certain key.
        Returns True if found, and False if not found.
        """
        for node in self:
            if node.key == key:
                if node == self._head:
                    self.delete_head()
                    # delete_head() already decrements length
                    return True
                if node == self._tail:
                    self.delete_tail()
                    # delete_head() already decrements length
                    return True
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self._length -= 1
                    return True
        return False

    def display(self, forward: bool = True) -> None:
        """Display the list items in forward or reverse order"""
        if self.is_empty:
            print("Empty list")
            return

        output = ""

        if forward is True:
            # Use the regular iterator
            nodes = self
        elif forward is False:
            # Use the reverse iterator
            nodes = reversed(self)
        else:
            raise TypeError("forward parameter must be a boolean.")

        for node in nodes:
            output += f"{node.key}'{node.name}'->"

        print(output[:-2]) # Remove the final '->' by slicing


    def __iter__(self):
        """Makes PlayerList into a iterable object, using a generator and yield"""
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def __reversed__(self):
        """Makes PlayerList work with Python's built-in reversed() function"""
        current = self._tail
        while current is not None:
            yield current
            current = current.prev