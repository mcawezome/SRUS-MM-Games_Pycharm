class PlayerBNode:
    def __init__(self, player):
        self.player = player

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        self._player = value

    def __str__(self):
        return f"PlayerBNode(player={self.player})"