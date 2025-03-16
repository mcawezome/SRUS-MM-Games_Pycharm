from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class PlayerHashMap:
    """A hash map implementation for storing and managing Player objects.

    The hash map uses chaining with linked lists to handle collisions.
    Each bucket in the hash map contains a PlayerList.

    Attributes:
        SIZE (int): The number of buckets in the hash map.
        hashmap (list[PlayerList]): The list of buckets containing PlayerLists.
    """

    def __init__(self) -> None:
        """Initialize an empty PlayerHashMap with a fixed number of buckets."""
        self.SIZE = 10
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str | Player) -> int:
        """Calculate the bucket index for a given key.

        Args:
            key: Either a player ID string or a Player object.

        Returns:
            int: The bucket index where the key should be stored.
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash(key) % self.SIZE

    def __len__(self) -> int:
        """Return the total number of players in the hash map.

        Returns:
            int: Total count of players across all buckets.
        """
        total = 0
        for player_list in self.hashmap:
            total += len(player_list)
        return total

    def __setitem__(self, key, value) -> None:
        """Add or update a player in the hash map.

        Args:
            key (str): The player ID.
            value (str): The player name.
        """
        player_list = self.hashmap[self.get_index(key)]
        result = player_list.find_node_with_key(key)
        player_node = PlayerNode(Player(key, value))
        if result is not None:
            # We need to update name.
            # The below implementation creates a new node and replaces the node with old name.
            # This allows us to keep name read-only in Player class.
            index = player_list.find_index_with_key(key)
            player_list.delete_node_with_key(key)
            player_list.insert_at_position(player_node, index)
        else:
            player_list.insert_at_tail(player_node)

    def __getitem__(self, key):
        """Retrieve a player's name by their ID.

        Args:
            key (str): The player ID to look up.

        Returns:
            str: The player's name.

        Raises:
            KeyError: If no player is found with the given key.
        """
        player_list = self.hashmap[self.get_index(key)]
        result = player_list.find_node_with_key(key)
        if result is None:
            raise KeyError(f"No player found with key: {key}")
        return result.player.name

    def __delitem__(self, key):
        """Remove a player from the hash map.

        Args:
            key (str): The player ID to remove.

        Raises:
            KeyError: If no player is found with the given key.
        """
        player_list = self.hashmap[self.get_index(key)]
        if not player_list.delete_node_with_key(key):
            raise KeyError(f"No player found with key: {key}")

    def display(self) -> None:
        """Print the contents of the hash map to the console.

        Displays non-empty buckets with their index and contents.
        """
        for index, player_list in enumerate(self.hashmap):
            if player_list.is_empty is False:
                print(f"{index=}, {player_list=!r}")
