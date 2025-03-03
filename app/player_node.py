from __future__ import annotations
from player import Player

class PlayerNode:
    def __init__(self, player: Player, next_node: PlayerNode | None = None, prev_node: PlayerNode | None = None):
        self._player = player
        self._next = next_node
        self._prev = prev_node

    @property
    def player(self) -> Player:
        """Get or set the Player object stored in this node."""
        return self._player

    # No setter for player - making it read-only
    # nodes represent fixed player entities, replace not modify

    @property
    def next(self) -> PlayerNode | None:
        """Get or set the next PlayerNode in the linked structure."""
        return self._next

    @next.setter
    def next(self, value: PlayerNode | None) -> None:
        self._next = value

    @property
    def prev(self) -> PlayerNode | None:
        """Get or set the previous PlayerNode in the linked structure."""
        return self._prev

    @prev.setter
    def prev(self, value: PlayerNode | None) -> None:
        self._prev = value

    @property
    def key(self):
        """Return the uid of the player in a node"""
        return self._player.uid

    def __str__(self):
        """Human-readable string of PlayerNode"""
        return f"PlayerNode id: {self.key}, next: {self._next}, prev:{self._prev}"
        # If we wanted to seamlessly chain __str__ together, the following might be better.
        # return f"{self.key}"