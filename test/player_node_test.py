import unittest
from player_node import PlayerNode
from player import Player


class TestPlayerClass(unittest.TestCase):
    """
    Test the functionality of player node class.
    """

    def setUp(self):
        """Initialize examples used in each test method."""
        self.player = Player("1", "Anthony Albanese")
        self.next_node = PlayerNode(Player("2", "John Howard"))
        self.prev_node = PlayerNode(Player("3", "Bob Hawk"))
        self.node = PlayerNode(self.player)

    def test_initialization_with_player(self):
        """Test node initialization with just a player."""
        self.assertEqual(self.node.player, self.player)
        self.assertIsNone(self.node.next)
        self.assertIsNone(self.node.prev)

    def test_initialization_with_all_parameters(self):
        """Test node initialization with player, next, and prev nodes."""
        node = PlayerNode(self.player, self.next_node, self.prev_node)
        self.assertEqual(node.player, self.player)
        self.assertEqual(node.next, self.next_node)
        self.assertEqual(node.prev, self.prev_node)

    def test_player_property(self):
        """Test that player property returns the correct player."""
        self.assertEqual(self.node.player, self.player)

    def test_next_property(self):
        """Test next node property getter and setter."""
        self.node.next = self.next_node
        self.assertEqual(self.node.next, self.next_node)
        self.node.next = None
        self.assertIsNone(self.node.next)

    def test_invalid_next_type(self):
        with self.assertRaises(TypeError):
            self.node.next = 1  # Test with integer
        with self.assertRaises(TypeError):
            self.node.prev = "hello"  # Test with string

    def test_invalid_prev_type(self):
        with self.assertRaises(TypeError):
            self.node.prev = -1  # Test with integer
        with self.assertRaises(TypeError):
            self.node.prev = "hello#$"  # Test with string

    def test_prev_property(self):
        """Test previous node property getter and setter."""
        self.node.prev = self.prev_node
        self.assertEqual(self.node.prev, self.prev_node)
        self.node.prev = None
        self.assertIsNone(self.node.prev)

    def test_key_property(self):
        """Test that key property returns player's uid."""
        self.assertEqual(self.node.key, "1")

    def test_name_property(self):
        """Test that name property returns player's name."""
        self.assertEqual(self.node.name, "Anthony Albanese")

    def test_repr(self):
        """Test string representation of the node."""
        self.node.next = self.next_node
        self.node.prev = self.prev_node
        expected = "PlayerNode id: 1, next: 2, prev: 3"
        self.assertEqual(repr(self.node), expected)

    def test_invalid_player_type(self):
        """Test that PlayerNode raises TypeError for invalid player type."""
        with self.assertRaises(TypeError):
            PlayerNode("not a player")  # Test with string
        with self.assertRaises(TypeError):
            PlayerNode(None)  # Test with None