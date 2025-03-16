from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class PlayerHashMap:
    """A hash map implementation for storing and managing Player objects.

    The hash map uses chaining with linked lists to handle collisions.
    Each bucket in the hash map contains a PlayerList.

    Attributes:
        SIZE (int): The number of buckets in the hash map.
        MAX_LOADING_FACTOR (float): Maximum ratio of items to buckets before resizing.
        hashmap (list[PlayerList]): The list of buckets containing PlayerLists.
    """

    def __init__(self) -> None:
        """Initialize an empty PlayerHashMap with a fixed number of buckets."""
        self.SIZE = 10
        self.MAX_LOADING_FACTOR = 0.7
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]
        self._resizing = False  # Flag to prevent recursive resizing

    @property
    def loading_factor(self) -> float:
        """Calculate the current load factor of the hash map.

        Returns:
            float: Ratio of total items to bucket count, rounded to 3 decimal places.
        """
        return round(float(len(self) / self.SIZE), 3) # Loading factor to 3 d.p.

    @property
    def is_loading_factor_exceeded(self) -> bool:
        """Check if the current loading factor exceeds the maximum allowed.

        Returns:
            bool: True if the loading factor is exceeded, False otherwise.
        """
        return self.loading_factor > self.MAX_LOADING_FACTOR

    def resize(self) -> None:
        """Double the size of the hash map and rehash all existing entries.

        This method is called automatically when the loading factor exceeds MAX_LOADING_FACTOR.
        """
        try:
            self._resizing = True
            self.SIZE = self.SIZE * 2
            old_hashmap = self.hashmap
            self.hashmap = [PlayerList() for _ in range(self.SIZE)]
            
            # Rehash all existing entries
            for player_list in old_hashmap:
                if len(player_list) > 0:
                    for player_node in player_list:
                        # Use proper hashing through __setitem__
                        player = player_node.player
                        self[player.uid] = player.name
        finally:
            self._resizing = False  # Ensure flag is reset even if an error occurs

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

        player = Player(key, value)

        if not self._resizing and self.is_loading_factor_exceeded:
            self.resize()

        player_list = self.hashmap[self.get_index(key)]
        result = player_list.find_node_with_key(key)
        player_node = PlayerNode(player)
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
            TypeError: If key is not a string.
            ValueError: If key is empty.
        """
        # validates key
        player = Player(key, "default")

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
            TypeError: If key is not a string.
            ValueError: If key is empty.
        """
        try:
            player = Player(key, "default")
        except ValueError as e:
            raise ValueError(f"Invalid player ID: {e}")
        except TypeError as e:
            raise TypeError(f"Invalid type for player ID: {e}")

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