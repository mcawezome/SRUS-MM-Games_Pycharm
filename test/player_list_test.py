import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class TestPlayerClass(unittest.TestCase):
    """
    Test PlayerClass is implemented correctly as a double-linked list of PlayerNodes.
    """
    def test_is_empty(self):
        player_list = PlayerList()
        self.assertTrue(player_list)
        self.assertEqual(player_list.length, 0)

    def test_insert_at_head_for_empty_list(self):
        """"""
        player_list = PlayerList()
        player = Player("20", "John Smith")
        node1 = PlayerNode(player)
        player_list.insert_at_head(node1)
        # test the keys because prev and next should have changed in the node
        self.assertEqual(player_list.head.key, node1.key)
        self.assertEqual(player_list.head.next, None)
        self.assertEqual(player_list.head.prev, None)

    def test_insert_at_head_for_single_node_list(self):
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        player_list.insert_at_head(node1)
        player_list.insert_at_head(node2)
        self.assertEqual(player_list.head.key, node2.key)
        self.assertEqual(player_list.head.next.key, node1.key)
        self.assertEqual(player_list.head.prev.key, node1.key)

    def test_insert_at_head_for_multiple_node_list(self):
        player_list = PlayerList()
        node1 = PlayerNode(Player("20", "John Smith"))
        node2 = PlayerNode(Player("23", "Stephen Curry"))
        node3 = PlayerNode(Player("42", "Douglad Adams"))
        player_list.insert_at_head(node1)
        player_list.insert_at_head(node2)
        player_list.insert_at_head(node3)
        self.assertEqual(player_list.head.key, node3.key)
        self.assertEqual(player_list.head.next.key, node2.key)
        self.assertEqual(player_list.head.prev.key, node1.key)
