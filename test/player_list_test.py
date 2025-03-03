import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestPlayerList(unittest.TestCase):
    """Tests for the PlayerList doubly-linked list implementation."""

    def test_new_list_is_empty(self):
        """Tests initialization of an empty list."""
        player_list = PlayerList()
        self.assertTrue(player_list)
        self.assertEqual(player_list.length, 0)

    def test_insert_head_empty_list_sets_head_and_tail(self):
        """Tests insert_at_head on an empty list.
        
        Verifies head and tail pointers are set correctly.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        player_list.insert_at_head(node1)
        # test the keys only because prev and next should have changed from the original node
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.tail.key, node1.key)
        self.assertEqual(player_list.head.next, None)
        self.assertEqual(player_list.head.prev, None)

    def test_insert_head_single_node_updates_pointers(self):
        """Tests insert_at_head on a single-node list.
        
        Verifies node connections and head/tail pointers are updated.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        player_list.insert_at_head(node1)
        player_list.insert_at_head(node2)
        self.assertEqual(player_list.head.key, node2.key)
        self.assertEqual(player_list.head.next.key, node1.key)
        self.assertEqual(player_list.tail.key, node1.key)

    def test_insert_head_multiple_nodes_maintains_links(self):
        """Tests insert_at_head on a multi-node list.
        
        Verifies node connections and head/tail pointers are updated.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))
        player_list.insert_at_head(node1)
        player_list.insert_at_head(node2)
        player_list.insert_at_head(node3)
        self.assertEqual(player_list.head.key, node3.key)
        self.assertEqual(player_list.head.next.key, node2.key)

        self.assertEqual(player_list.tail.key, node1.key)

    def test_insert_tail_empty_list_sets_head_and_tail(self):
        """Tests insert_at_tail on an empty list.
        
        Verifies head and tail pointers are set correctly.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        player_list.insert_at_tail(node1)
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.tail.key, node1.key)
        self.assertEqual(player_list.head.next, None)
        self.assertEqual(player_list.head.prev, None)

    def test_insert_tail_single_node_updates_pointers(self):
        """Tests insert_at_tail on a single-node list.
        
        Verifies node connections and head/tail pointers are updated.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.head.next.key, node2.key)
        self.assertEqual(player_list.tail.key, node2.key)
        self.assertEqual(player_list.tail.prev.key, node1.key)

    def test_insert_tail_multiple_nodes_maintains_links(self):
        """Tests insert_at_tail on a multi-node list.
        
        Verifies node connections and head/tail pointers are updated.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))
        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)

        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.head.next.key, node2.key)
        self.assertEqual(player_list.tail.key, node2.key)

        player_list.insert_at_tail(node3)
        self.assertEqual(player_list.head.next.next.key, node3.key)
        self.assertEqual(player_list.tail.key, node3.key)

    def test_delete_head_updates_list_structure(self):
        """Tests delete_head functionality.
        
        Verifies head pointer updates and node connections after deletion.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))

        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)
        player_list.insert_at_tail(node3)

        player_list.delete_head()

        self.assertEqual(player_list.head.key, node2.key)
        self.assertEqual(player_list.tail.key, node3.key)
        player_list.delete_head()
        self.assertEqual(player_list.head.key, node3.key)
        self.assertEqual(player_list.tail.key, node3.key)

    def test_delete_tail_updates_list_structure(self):
        """Tests delete_tail functionality.
        
        Verifies tail pointer updates and node connections after deletion.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))

        player_list.insert_at_head(node1)
        player_list.insert_at_head(node2)
        player_list.insert_at_head(node3)

        player_list.delete_tail()
        self.assertEqual(player_list.tail.key, node2.key)

        player_list.delete_tail()
        self.assertEqual(player_list.head.key, node3.key)
        self.assertEqual(player_list.tail.key, node3.key)

    def test_delete_by_key_handles_all_positions(self):
        """Tests delete_node_with_key functionality.
        
        Verifies successful deletion of existing keys and handling of non-existent keys.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))

        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)
        player_list.insert_at_tail(node3)

        self.assertFalse(player_list.delete_node_with_key("1"))
        self.assertTrue(player_list.delete_node_with_key("23"))
        self.assertEqual(player_list.tail.key, node3.key)

        self.assertTrue(player_list.delete_node_with_key("42"))
        self.assertEqual(player_list.tail.key, node1.key)

        self.assertTrue(player_list.delete_node_with_key("20"))

    def test_display_executes_without_error(self):
        """Tests that display method executes without errors.
        
        Note:
            Visual inspection of output required for full verification.
        """
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))

        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)
        player_list.insert_at_tail(node3)

        player_list.display(False)
        # Visually inspect printed output. (difficult to test)