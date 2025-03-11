import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestPlayerList(unittest.TestCase):
    """Tests for the PlayerList doubly-linked list implementation."""

    def setUp(self):
        """Initialize test fixtures before each test method."""
        self.list = PlayerList()
        self.node1 = PlayerNode(Player("1", "Alpha"))
        self.node2 = PlayerNode(Player("2", "Beta"))
        self.node3 = PlayerNode(Player("3", "Charlie"))

    def test_empty_list(self):
        self.assertTrue(self.list.is_empty)
        self.assertEqual(self.list.length, 0)

    def test_insert_and_delete(self):
        # Test insert
        self.list.insert_at_head(self.node1)
        self.assertEqual(self.list.head.key, "1")
        self.assertEqual(self.list.length, 1)

        self.list.insert_at_tail(self.node2)
        self.assertEqual(self.list.tail.key, "2")
        self.assertEqual(self.list.length, 2)

        # Test delete
        self.list.delete_head()
        self.assertEqual(self.list.head.key, "2")
        self.assertEqual(self.list.length, 1)

        self.list.delete_tail()
        self.assertTrue(self.list.is_empty)
        self.assertEqual(self.list.length, 0)

    def test_find_and_delete_by_key(self):
        self.list.insert_at_tail(self.node1)
        self.list.insert_at_tail(self.node2)
        self.list.insert_at_tail(self.node3)

        # Find existing node
        node = self.list.find_node_with_key("2")
        self.assertEqual(node.key, "2")

        # Delete middle node
        self.assertTrue(self.list.delete_node_with_key("2"))
        self.assertEqual(self.list.length, 2)

        # Try to delete non-existent node
        self.assertFalse(self.list.delete_node_with_key("999"))

    def test_iteration(self):
        self.list.insert_at_tail(self.node1)
        self.list.insert_at_tail(self.node2)
        self.list.insert_at_tail(self.node3)

        # Forward iteration
        keys = [node.key for node in self.list]
        self.assertEqual(keys, ["1", "2", "3"])

        # Reverse iteration
        keys = [node.key for node in reversed(self.list)]
        self.assertEqual(keys, ["3", "2", "1"])

if __name__ == "__main__":
    unittest.main()