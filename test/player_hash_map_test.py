import unittest
from player_hash_map import PlayerHashMap
from player import Player


class TestPlayerHashMap(unittest.TestCase):
    """Tests for PlayerHashMap implementation."""

    def setUp(self):
        """Initialize test fixtures before each test."""
        self.hash_map = PlayerHashMap()
        # Add some initial test data
        self.hash_map["1"] = "Alpha"
        self.hash_map["2"] = "Beta"
        self.hash_map["3"] = "Charlie"

    def test_add_and_get_player(self):
        """Test adding and retrieving players."""
        # Test getting existing players
        self.assertEqual(self.hash_map["1"], "Alpha")
        self.assertEqual(self.hash_map["2"], "Beta")
        
        # Test adding new player
        self.hash_map["4"] = "David"
        self.assertEqual(self.hash_map["4"], "David")

    def test_update_player(self):
        """Test updating existing player names."""
        self.hash_map["1"] = "Alpha Updated"
        self.assertEqual(self.hash_map["1"], "Alpha Updated")

    def test_delete_player(self):
        """Test deleting players."""
        # Delete existing player
        del self.hash_map["1"]
        with self.assertRaises(KeyError):
            _ = self.hash_map["1"]

        # Try to delete non-existent player
        with self.assertRaises(KeyError):
            del self.hash_map["999"]

    def test_length(self):
        """Test length calculation."""
        self.assertEqual(len(self.hash_map), 3)
        
        # Add player
        self.hash_map["4"] = "David"
        self.assertEqual(len(self.hash_map), 4)
        
        # Delete player
        del self.hash_map["4"]
        self.assertEqual(len(self.hash_map), 3)

    def test_get_index(self):
        """Test index calculation for keys."""
        # Test with string key
        index = self.hash_map.get_index("1")
        self.assertIsInstance(index, int)
        self.assertTrue(0 <= index < self.hash_map.SIZE)

        # Test with Player object
        player = Player("1", "Test")
        index = self.hash_map.get_index(player)
        self.assertIsInstance(index, int)
        self.assertTrue(0 <= index < self.hash_map.SIZE)

    def test_key_errors(self):
        """Test error handling for invalid keys."""
        with self.assertRaises(KeyError):
            _ = self.hash_map["non_existent"]

    def test_display(self):
        """Test that display method executes without errors."""
        try:
            self.hash_map.display()
        except Exception as e:
            self.fail(f"display() raised {type(e)} unexpectedly!")

    def test_empty_hash_map(self):
        """Test operations on empty hash map."""
        empty_map = PlayerHashMap()
        self.assertEqual(len(empty_map), 0)
        
        with self.assertRaises(KeyError):
            _ = empty_map["1"]

    def test_collision_handling(self):
        """Test handling of hash collisions."""
        # Add multiple players that might hash to same index
        for i in range(20):  # More than SIZE to force collisions
            self.hash_map[str(i)] = f"Player{i}"
            
        # Verify all players are still accessible
        for i in range(20):
            self.assertEqual(self.hash_map[str(i)], f"Player{i}")


if __name__ == "__main__":
    unittest.main()