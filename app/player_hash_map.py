from player_list import PlayerList

class PlayerHashMap:
    def __init__(self):
        self.SIZE = 10
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def __len__(self):
        return len(self.hashmap) # TODO: check this for empty players

    def __setitem__(self, key, name):
        pass

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass