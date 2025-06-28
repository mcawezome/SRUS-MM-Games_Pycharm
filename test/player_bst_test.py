import unittest
from player_bst import PlayBST
from player import Player

class TestPlayBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayBST()
        # Create test players
        self.player1 = Player("1", "Alice")
        self.player2 = Player("2", "Bob")
        self.player3 = Player("3", "Charlie")
        self.player4 = Player("4", "David")
        self.player5 = Player("5", "Eve")
        self.player6 = Player("6", "Frank")
        self.player7 = Player("7", "Grace")

    def test_insert_and_search(self):
        """Test basic insert and search functionality."""
        self.bst.insert(self.player1)
        self.assertEqual(self.bst.root.player.name, "Alice")
        
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        
        # Test search
        result = self.bst.search("Bob")
        self.assertEqual(result.player.name, "Bob")
        
        result = self.bst.search("Charlie")
        self.assertEqual(result.player.name, "Charlie")
        
        # Test search for non-existent player
        result = self.bst.search("NonExistent")
        self.assertIsNone(result)

    def test_balance_empty_tree(self):
        """Test balancing an empty tree."""
        self.bst.balance()
        self.assertIsNone(self.bst.root)

    def test_balance_single_node(self):
        """Test balancing a tree with single node."""
        self.bst.insert(self.player1)
        self.bst.balance()
        self.assertEqual(self.bst.root.player.name, "Alice")
        self.assertTrue(self.bst.is_balanced())

    def test_balance_unbalanced_tree(self):
        """Test balancing an unbalanced tree."""
        # Create an unbalanced tree (linear structure)
        self.bst.insert(self.player1)  # Alice
        self.bst.insert(self.player2)  # Bob
        self.bst.insert(self.player3)  # Charlie
        self.bst.insert(self.player4)  # David
        self.bst.insert(self.player5)  # Eve
        
        # Before balancing, tree is likely unbalanced
        print("Before balancing:")
        self.bst.display()
        
        # Balance the tree
        self.bst.balance()
        
        print("\nAfter balancing:")
        self.bst.display()
        
        # Verify tree is balanced
        self.assertTrue(self.bst.is_balanced())
        
        # Verify all nodes are still accessible
        self.assertIsNotNone(self.bst.search("Alice"))
        self.assertIsNotNone(self.bst.search("Bob"))
        self.assertIsNotNone(self.bst.search("Charlie"))
        self.assertIsNotNone(self.bst.search("David"))
        self.assertIsNotNone(self.bst.search("Eve"))

    def test_balance_complex_tree(self):
        """Test balancing a more complex unbalanced tree."""
        # Insert in a way that creates an unbalanced tree
        players = [
            Player("1", "A"),
            Player("2", "B"),
            Player("3", "C"),
            Player("4", "D"),
            Player("5", "E"),
            Player("6", "F"),
            Player("7", "G"),
            Player("8", "H"),
            Player("9", "I"),
            Player("10", "J")
        ]
        
        for player in players:
            self.bst.insert(player)
        
        print("Before balancing:")
        self.bst.display()
        
        # Balance the tree
        self.bst.balance()
        
        print("\nAfter balancing:")
        self.bst.display()
        
        # Verify tree is balanced
        self.assertTrue(self.bst.is_balanced())
        
        # Verify all nodes are still accessible
        for player in players:
            result = self.bst.search(player.name)
            self.assertIsNotNone(result)
            self.assertEqual(result.player.name, player.name)

    def test_height_calculation(self):
        """Test height calculation for nodes."""
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        
        # Test height of root
        root_height = self.bst.get_height(self.bst.root)
        self.assertGreaterEqual(root_height, 1)
        
        # Test height of leaf nodes
        if self.bst.root.left:
            left_height = self.bst.get_height(self.bst.root.left)
            self.assertGreaterEqual(left_height, 0)
        
        if self.bst.root.right:
            right_height = self.bst.get_height(self.bst.root.right)
            self.assertGreaterEqual(right_height, 0)

    def test_balance_factor_calculation(self):
        """Test balance factor calculation."""
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        
        # Test balance factor of root
        balance_factor = self.bst.get_balance_factor(self.bst.root)
        self.assertIsInstance(balance_factor, int)

    def test_is_balanced_method(self):
        """Test the is_balanced method."""
        # Empty tree should be balanced
        self.assertTrue(self.bst.is_balanced())
        
        # Single node should be balanced
        self.bst.insert(self.player1)
        self.assertTrue(self.bst.is_balanced())
        
        # Add more nodes and test
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        
        # Before balancing, tree might be unbalanced
        # After balancing, tree should be balanced
        self.bst.balance()
        self.assertTrue(self.bst.is_balanced())

    def test_inorder_traversal_order(self):
        """Test that inorder traversal produces sorted order."""
        # Insert players in random order
        self.bst.insert(self.player3)  # Charlie
        self.bst.insert(self.player1)  # Alice
        self.bst.insert(self.player5)  # Eve
        self.bst.insert(self.player2)  # Bob
        self.bst.insert(self.player4)  # David
        
        # Collect nodes in inorder traversal
        sorted_nodes = []
        self.bst._inorder_traversal(self.bst.root, sorted_nodes)
        
        # Verify they are in sorted order
        names = [node.player.name for node in sorted_nodes]
        self.assertEqual(names, ["Alice", "Bob", "Charlie", "David", "Eve"])

    def test_build_balanced_tree(self):
        """Test the _build_balanced_tree method directly."""
        # Create sorted nodes
        players = [
            Player("1", "A"),
            Player("2", "B"),
            Player("3", "C"),
            Player("4", "D"),
            Player("5", "E")
        ]
        
        nodes = []
        for player in players:
            from player_bnode import PlayerBNode
            nodes.append(PlayerBNode(player))
        
        # Build balanced tree
        root = self.bst._build_balanced_tree(nodes, 0, len(nodes) - 1)
        
        # Verify the tree is balanced
        self.bst.root = root
        self.assertTrue(self.bst.is_balanced())
        
        # Verify all nodes are accessible
        for player in players:
            result = self.bst.search(player.name)
            self.assertIsNotNone(result)
            self.assertEqual(result.player.name, player.name)

if __name__ == '__main__':
    unittest.main()