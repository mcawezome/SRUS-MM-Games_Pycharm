import unittest
from player import Player


class TestPlayerClass(unittest.TestCase):
    """
    Test the basic functions of setting uid and name of Player class
    """
    def setUp(self):
        """Initialize test fixtures before each test method."""
        self.player1 = Player("1", "Amy")
        self.player2 = Player("007", "Charlie")
        self.player3 = Player("1", "Alice")

    def test_valid_initialization(self):
        """Test that players can be created with valid inputs"""
        self.assertEqual(self.player1.uid, "1")
        self.assertEqual(self.player1.name, "Amy")

    def test_whitespace_handling(self):
        """Test that whitespace is properly stripped from names"""
        self.player2.name = " David Smith "
        self.assertEqual(self.player2.name, "David Smith")

    def test_uid_with_leading_zeroes(self):
        """Test that leading zeroes is properly stripped from uids"""
        self.assertEqual(self.player2.uid, "7")

    def test_invalid_uid(self):
        """Test that invalid UIDs raise appropriate exceptions"""
        with self.assertRaises(ValueError):
            Player("not_a_number", "Ben")
        with self.assertRaises(TypeError):
            Player(1, "Ben")
        with self.assertRaises(ValueError):
            Player("-10", "Invalid")

    def test_invalid_name(self):
        """Test that invalid names raise appropriate exceptions"""
        with self.assertRaises(ValueError):
            Player("1", "")
        with self.assertRaises(ValueError):
            Player("1", "   ")
        with self.assertRaises(TypeError):
            Player("1", 123)

    def test_update_attributes(self):
        """Test updating attributes after initialization"""
        # Update UID
        self.player3.uid = "99"
        self.assertEqual(self.player3.uid, "99")

        # Update UID with string
        self.player3.uid = "100"
        self.assertEqual(self.player3.uid, "100")

        # Update name
        self.player3.name = "Max"
        self.assertEqual(self.player3.name, "Max")

    def test_delete_attributes(self):
        """Test deleting attributes"""
        # Test deleting name (should set to "No Name")
        del self.player3.name
        self.assertEqual(self.player3.name, "No Name")

        # Test deleting UID (should raise AttributeError)
        with self.assertRaises(AttributeError):
            del self.player3.uid

    def test_representation(self):
        """Test the string representation of a Player"""
        self.assertEqual(repr(self.player3), "Player(uid='1', name='Alice')")


if __name__ == "__main__":
    unittest.main()