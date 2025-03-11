from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class PlayerHashMap:
    def __init__(self) -> None:
        """
        Object containing a hashmap object (list containing PlayerLists)
        Used for reducing time complexity of storing Players in a list
        """
        self.SIZE = 10
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash_djb3(key) % self.SIZE  # TODO ensure hash is a class method in Player
            # TODO: Really don't like calling hash_djb3 from outside the Player class.

    def __len__(self) -> int:
        # Count total number of players across all lists
        total = 0
        for player_list in self.hashmap:
            total += len(player_list)
        return total

    def __setitem__(self, key, value) -> None:
        """
        Add or update a player in the hash map
        key: player ID as string
        value: player name as string
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
        """
        Get a player by key (player ID)
        """
        player_list = self.hashmap[self.get_index(key)]
        result = player_list.find_node_with_key(key)
        if result is None:
            raise KeyError(f"No player found with key: {key}")
        return result.player.name

    def __delitem__(self, key):
        """
        Delete a player by key (player ID)
        """
        player_list = self.hashmap[self.get_index(key)]
        if not player_list.delete_node_with_key(key):
            raise KeyError(f"No player found with key: {key}")

    def display(self) -> None:
        """Display a message to console including contents of hash map"""
        default = PlayerList()
        for index, player_list in enumerate(self.hashmap):
            if player_list.is_empty is False:
                print(f"{index=}, {player_list=!r}")


if __name__ == "__main__":
    phm = PlayerHashMap()

    # Adding players directly to the hash map
    phm["20"] = "John Smith"
    phm["23"] = "Stephen Curry"
    phm["42"] = "Douglas Adams"

    # Display the hash map
    phm.display()

    # Example of retrieval
    print(f"Player with ID '23': {phm['23']}")

    # Update a player's name
    phm["42"] = "Jackie Robinson"
    # Display again after update
    phm.display()

    print(phm['12'])