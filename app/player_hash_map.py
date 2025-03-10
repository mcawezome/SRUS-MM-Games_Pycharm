from player_list import PlayerList
from player import Player
from player_node import PlayerNode

class PlayerHashMap:
    def __init__(self):
        self.SIZE = 10
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash(key) % self.SIZE  # TODO ensure hash is a class method in Player

    def __len__(self):
        return len(self.hashmap) # TODO: test this for empty players

    def __setitem__(self, key, name):
        """
            ''' Psuedo code:
        1. Use the key to calculate an index into the hash map
           (TODO: Implement a hash function in the Player class that returns a player hash and then modulate it by the size of the hashmap)
        2. Get the PlayerList at that index
        3. Check if the player is already on that player list.
             If it is, update the player's name.
             If it isn't, create a player and add the player to the player list.

         '''
         # get the player's appropriate PlayerList:
         player_list = self.hashmap[self.get_index(key)]
         # check if the player is in the list
         # If it is, update the player's name
         # If it isn't, create a player and add the player to the player list
        """
        player_list = self.hashmap[self.get_index(key)]
        # TODO: ^ requires __getitem__
        result = player_list.find_node_with_key(key)
        if result is not None:
            # we need to update name (currently can't do this directly)
            pass
        else:
            player_node = PlayerNode(Player(key, name))
            player_list.insert_at_tail(player_node)



    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass