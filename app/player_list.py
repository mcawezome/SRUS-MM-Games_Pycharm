from __future__ import annotations
from player import Player
from player_node import PlayerNode

class PlayerList:
    # TODO: add docstrings
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
            return
        is_one_node = self._head.prev is None and self._head.next is None
        if is_one_node:
            node.prev = self._head
            node.next = self._head
            self._tail = self._head
            self._head = node
            self._length += 1
            return
        # if more than 1 node
        node.prev = self._head.prev
        node.next = self._head
        self._head = node
        # self._tail does not change.
        self._length += 1
        return