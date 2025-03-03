import unittest
from player import Player


class TestPlayerClass(unittest.TestCase):
    """
    Test the basic functions of setting uid and name of Player class
    """
    def test_valid_initialization(self):
        """Test that players can be created with valid inputs"""
        # Test integer UID
        player1 = Player("1", "Amy")
        self.assertEqual(player1.uid, "1")
        self.assertEqual(player1.name, "Amy")

    def test_whitespace_handling(self):
        """Test that whitespace is properly stripped from names"""
        player = Player("  1 ", "Charlie")
        self.assertEqual(player.name, "Charlie")

        player.name = " David Smith "
        self.assertEqual(player.name, "David Smith")

    def test_uid__with_leading_zeroes(self):
        """Test that leading zeroes is properly stripped from uids"""
        player = Player("007", "Charlie")
        self.assertEqual(player.uid, "7")

    def test_invalid_uid(self):
        """Test that players can be created with valid inputs"""
        # Test integer UID
        with self.assertRaises(ValueError):
            Player("not_a_number", "Ben")
        with self.assertRaises(TypeError):
            Player(1, "Ben")
        # Test negative string
        with self.assertRaises(ValueError):
            Player("-10", "Invalid")

    def test_invalid_name(self):
        """Test that invalid names raise appropriate exceptions"""
        # Test empty string
        with self.assertRaises(ValueError):
            Player("1", "")

        # Test whitespace-only string
        with self.assertRaises(ValueError):
            Player("1", "   ")

        # Test non-string type
        with self.assertRaises(ValueError):
            Player("1", 123)

    def test_update_attributes(self):
        """Test updating attributes after initialization"""
        player = Player("1", "Alice")

        # Update UID
        player.uid = "99"
        self.assertEqual(player.uid, "99")

        # Update UID with string
        player.uid = "100"
        self.assertEqual(player.uid, "100")

        # Update name
        player.name = "Max"
        self.assertEqual(player.name, "Max")

    def test_delete_attributes(self):
        """Test deleting attributes"""
        player = Player("1", "Alice")

        # Test deleting name (should set to "Anonymous")
        del player.name
        self.assertEqual(player.name, "Anonymous")

        # Test deleting UID (should raise AttributeError)
        with self.assertRaises(AttributeError):
            del player.uid

    def test_representation(self):
        """Test the string representation of a Player"""
        player = Player("1", "Alice")
        self.assertEqual(repr(player), "Player(uid='1', name='Alice')")


if __name__ == "__main__":
    unittest.main()