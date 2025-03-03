from __future__ import annotations
from player import Player


class PlayerNode:
    """A node in a doubly-linked list structure containing player information.

    Args:
        player: The Player object stored in this node.
        next_node: Reference to the next PlayerNode, if any.
        prev_node: Reference to the previous PlayerNode, if any.
    """

    def __init__(self, player: Player, next_node: PlayerNode | None = None, prev_node: PlayerNode | None = None):
        self._player = player
        self._next = next_node
        self._prev = prev_node

    @property
    def player(self) -> Player:
        """Gets the Player object stored in this node.

        Returns:
            The Player object.
        """
        return self._player

    # No setter for player - making it read-only
    # nodes represent fixed player entities, replace not modify

    @property
    def next(self) -> PlayerNode | None:
        """Gets the next PlayerNode in the linked structure.

        Returns:
            The next PlayerNode or None if no next node exists.
        """
        return self._next

    @next.setter
    def next(self, value: PlayerNode | None) -> None:
        """Sets the next PlayerNode in the linked structure.

        Args:
            value: The PlayerNode to set as next, or None to clear the reference.
        """
        self._next = value

    @property
    def prev(self) -> PlayerNode | None:
        """Gets the previous PlayerNode in the linked structure.

        Returns:
            The previous PlayerNode or None if no previous node exists.
        """
        return self._prev

    @prev.setter
    def prev(self, value: PlayerNode | None) -> None:
        """Sets the previous PlayerNode in the linked structure.

        Args:
            value: The PlayerNode to set as previous, or None to clear the reference.
        """
        self._prev = value

    @property
    def key(self):
        """Gets the unique identifier of the player in this node.

        Returns:
            The player's uid.
        """
        return self._player.uid

    @property
    def name(self):
        """Gets the name of the player in this node.

        Returns:
            The player's name.
        """
        return self._player.name

    def __repr__(self):
        """Returns a string representation of the PlayerNode.

        Returns:
            A string showing the node's key and its connections.
        """
        # repr is clear enough, no need for __str__
        next_key = self._next.key if self._next else "None"
        prev_key = self._prev.key if self._prev else "None"
        return f"PlayerNode id: {self.key}, next: {next_key}, prev: {prev_key}"