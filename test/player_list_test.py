import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestPlayerClass(unittest.TestCase):
    """
    Test PlayerClass is implemented correctly as a double-linked list of PlayerNodes.
    """
    def test_is_empty(self):
        """Test newly initialised list is empty"""
        player_list = PlayerList()
        self.assertTrue(player_list)
        self.assertEqual(player_list.length, 0)

    def test_insert_at_head_for_empty_list(self):
        """Test function insert_at_head in the case of an empty list"""
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        player_list.insert_at_head(node1)
        # test the keys only because prev and next should have changed from the original node
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.tail.key, node1.key)
        self.assertEqual(player_list.head.next, None)
        self.assertEqual(player_list.head.prev, None)

    def test_insert_at_head_for_single_node_list(self):
        """Test function insert_at_head in the case of a single node list"""
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        player_list.insert_at_head(node1)
        player_list.insert_at_head(node2)
        self.assertEqual(player_list.head.key, node2.key)
        self.assertEqual(player_list.head.next.key, node1.key)
        self.assertEqual(player_list.tail.key, node1.key)

    def test_insert_at_head_for_multiple_node_list(self):
        """Test function insert_at_head in the case of a multiple node list"""
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

    def test_insert_at_tail_for_empty_list(self):
        """Test function insert_at_tail in the case of an empty list"""
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        player_list.insert_at_tail(node1)
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.tail.key, node1.key)
        self.assertEqual(player_list.head.next, None)
        self.assertEqual(player_list.head.prev, None)

    def test_insert_at_tail_for_single_node_list(self):
        """Test function insert_at_tail in the case of a single node list"""
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.head.next.key, node2.key)
        self.assertEqual(player_list.tail.key, node2.key)
        self.assertEqual(player_list.tail.prev.key, node1.key)

    def test_insert_at_tail_for_multiple_node_list(self):
        """Test function insert_at_tail in the case of a multiple node list"""
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

    def test_delete_head(self):
        """Test function delete_at_head deletes first element correctly"""
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

    def test_delete_tail(self):
        """Test function delete_at_head deletes first element correctly"""
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

    def test_delete_node_with_key(self):
        """Test function delete_at_head deletes correctly when given key"""
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

    def test_display_runs(self):
        """Tests the display function runs, but does not test output"""
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglas Adams"))

        player_list.insert_at_tail(node1)
        player_list.insert_at_tail(node2)
        player_list.insert_at_tail(node3)

        player_list.display()
        # Visually inspect printed output. (difficult to test)