import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestPlayerList(unittest.TestCase):
    """Tests for the PlayerList doubly-linked list implementation."""

    def setUp(self):
        """Initialize test fixtures before each test method."""
        self.player_list = PlayerList()
        self.node1 = PlayerNode(Player("20", "John Smith"))
        self.node2 = PlayerNode(Player("23", "Stephen Curry"))
        self.node3 = PlayerNode(Player("42", "Douglas Adams"))

    def test_new_list_is_empty(self):
        """Tests initialization of an empty list."""
        self.assertTrue(self.player_list.is_empty)
        self.assertEqual(self.player_list.length, 0)

    def test_insert_head_empty_list_sets_head_and_tail(self):
        """Tests insert_at_head on an empty list."""
        self.player_list.insert_at_head(self.node1)
        self.assertEqual(self.player_list.head.key, self.node1.key)
        self.assertEqual(self.player_list.tail.key, self.node1.key)
        self.assertEqual(self.player_list.head.next, None)
        self.assertEqual(self.player_list.head.prev, None)

    def test_insert_head_single_node_updates_pointers(self):
        """Tests insert_at_head on a single-node list."""
        self.player_list.insert_at_head(self.node1)
        self.player_list.insert_at_head(self.node2)
        self.assertEqual(self.player_list.head.key, self.node2.key)
        self.assertEqual(self.player_list.head.next.key, self.node1.key)
        self.assertEqual(self.player_list.tail.key, self.node1.key)

    def test_insert_head_multiple_nodes_maintains_links(self):
        """Tests insert_at_head on a multi-node list."""
        self.player_list.insert_at_head(self.node1)
        self.player_list.insert_at_head(self.node2)
        self.player_list.insert_at_head(self.node3)
        self.assertEqual(self.player_list.head.key, self.node3.key)
        self.assertEqual(self.player_list.head.next.key, self.node2.key)
        self.assertEqual(self.player_list.tail.key, self.node1.key)

    def test_insert_tail_empty_list_sets_head_and_tail(self):
        """Tests insert_at_tail on an empty list."""
        self.player_list.insert_at_tail(self.node1)
        self.assertEqual(self.player_list.head.key, self.node1.key)
        self.assertEqual(self.player_list.tail.key, self.node1.key)
        self.assertEqual(self.player_list.head.next, None)
        self.assertEqual(self.player_list.head.prev, None)

    def test_insert_tail_single_node_updates_pointers(self):
        """Tests insert_at_tail on a single-node list."""
        self.player_list.insert_at_tail(self.node1)
        self.player_list.insert_at_tail(self.node2)
        self.assertEqual(self.player_list.head.key, self.node1.key)
        self.assertEqual(self.player_list.head.next.key, self.node2.key)
        self.assertEqual(self.player_list.tail.key, self.node2.key)
        self.assertEqual(self.player_list.tail.prev.key, self.node1.key)

    def test_insert_tail_multiple_nodes_maintains_links(self):
        """Tests insert_at_tail on a multi-node list."""
        self.player_list.insert_at_tail(self.node1)
        self.player_list.insert_at_tail(self.node2)
        self.assertEqual(self.player_list.head.key, self.node1.key)
        self.assertEqual(self.player_list.head.next.key, self.node2.key)
        self.assertEqual(self.player_list.tail.key, self.node2.key)

        self.player_list.insert_at_tail(self.node3)
        self.assertEqual(self.player_list.head.next.next.key, self.node3.key)
        self.assertEqual(self.player_list.tail.key, self.node3.key)

    def test_delete_head_updates_list_structure(self):
        """Tests delete_head functionality."""
        self.player_list.insert_at_tail(self.node1)
        self.player_list.insert_at_tail(self.node2)
        self.player_list.insert_at_tail(self.node3)

        self.player_list.delete_head()
        self.assertEqual(self.player_list.head.key, self.node2.key)
        self.assertEqual(self.player_list.tail.key, self.node3.key)

        self.player_list.delete_head()
        self.assertEqual(self.player_list.head.key, self.node3.key)
        self.assertEqual(self.player_list.tail.key, self.node3.key)

    def test_delete_tail_updates_list_structure(self):
        """Tests delete_tail functionality."""
        self.player_list.insert_at_head(self.node1)
        self.player_list.insert_at_head(self.node2)
        self.player_list.insert_at_head(self.node3)

        self.player_list.delete_tail()
        self.assertEqual(self.player_list.tail.key, self.node2.key)

        self.player_list.delete_tail()
        self.assertEqual(self.player_list.head.key, self.node3.key)
        self.assertEqual(self.player_list.tail.key, self.node3.key)

    def test_delete_by_key_handles_all_positions(self):
        """Tests delete_node_with_key functionality."""
        self.player_list.insert_at_tail(self.node1)
        self.player_list.insert_at_tail(self.node2)
        self.player_list.insert_at_tail(self.node3)

        self.assertFalse(self.player_list.delete_node_with_key("1"))
        self.assertTrue(self.player_list.delete_node_with_key("23"))
        self.assertEqual(self.player_list.tail.key, self.node3.key)

        self.assertTrue(self.player_list.delete_node_with_key("42"))
        self.assertEqual(self.player_list.tail.key, self.node1.key)

        self.assertTrue(self.player_list.delete_node_with_key("20"))

    def test_display_executes_without_error(self):
        """Tests that display method executes without errors."""
        self.player_list.insert_at_tail(self.node1)
        self.player_list.insert_at_tail(self.node2)
        self.player_list.insert_at_tail(self.node3)

        self.player_list.display(False)
        # Visually inspect printed output. (difficult to test)