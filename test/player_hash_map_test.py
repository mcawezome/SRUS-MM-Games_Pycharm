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
        with self.assertRaises(ValueError):
            _ = self.hash_map["bad uid"]

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

    def test_resize_behavior(self):
        """Test that the hash map resizes correctly when loading factor is exceeded."""
        initial_size = self.hash_map.SIZE
        players_to_add = int(initial_size * self.hash_map.MAX_LOADING_FACTOR) + 1
        
        # Calculate expected loading factor after adding players
        expected_initial_loading = players_to_add / initial_size
        self.assertGreater(expected_initial_loading, self.hash_map.MAX_LOADING_FACTOR,
                          "Test setup should exceed loading factor")
        
        # Add enough players to trigger resize
        for i in range(players_to_add):
            self.hash_map[str(i)] = f"Player{i}"
        
        # Verify the size has doubled
        self.assertEqual(self.hash_map.SIZE, initial_size * 2)
        
        # Verify loading factor after resize
        expected_final_loading = players_to_add / (initial_size * 2)
        self.assertAlmostEqual(self.hash_map.loading_factor, expected_final_loading, places=3)
        
        # Verify all players are still accessible after resize
        for i in range(players_to_add):
            self.assertEqual(self.hash_map[str(i)], f"Player{i}",
                           f"Player {i} not found after resize")

    def test_loading_factor(self):
        """Test loading factor calculation and threshold."""
        initial_size = self.hash_map.SIZE
        max_players = int(initial_size * self.hash_map.MAX_LOADING_FACTOR)
        
        # Add players up to just below the threshold
        for i in range(max_players):
            self.hash_map[str(i)] = f"Player{i}"
        
        # Verify we haven't resized yet
        self.assertEqual(self.hash_map.SIZE, initial_size)
        
        # Add one more player to trigger resize
        self.hash_map[str(max_players)] = f"Player{max_players}"
        self.assertEqual(self.hash_map.SIZE, initial_size * 2)

    def test_input_validation(self):
        """Test input validation for invalid types and empty values."""
        # Test invalid key types
        with self.assertRaises(TypeError):
            self.hash_map[123] = "Player"
        with self.assertRaises(TypeError):
            self.hash_map[None] = "Player"
        
        # Test invalid value types
        with self.assertRaises(TypeError):
            self.hash_map["1"] = 123
        with self.assertRaises(TypeError):
            self.hash_map["1"] = None
        
        # Test empty strings
        with self.assertRaises(ValueError):
            self.hash_map[""] = "Player"
        with self.assertRaises(ValueError):
            self.hash_map["   "] = "Player"
        with self.assertRaises(ValueError):
            self.hash_map["1"] = ""
        with self.assertRaises(ValueError):
            self.hash_map["1"] = "   "


if __name__ == "__main__":
    unittest.main()