import unittest
from player_bst import PlayBST
from player import Player

class TestPlayBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayBST()
        self.bst.insert(Player("John", "1234567890"))
        self.bst.insert(Player("Jane", "0987654321"))
        self.bst.insert(Player("Jim", "1111111111"))

    def test_insert(self):
        self.bst.insert(Player("John", "1234567890"))
        self.assertEqual(self.bst.root.player.name, "John")
        self.assertEqual(self.bst.root.player.id, "1234567890")

    def test_search(self):
        self.assertEqual(self.bst.search("John").player.name, "John")
        self.assertEqual(self.bst.search("Jane").player.name, "Jane")