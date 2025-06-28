class PlayerBNode:
    def __init__(self, player):
        self.player = player
        self._left = None
        self._right = None
        self._height = 1  # Height of 1 for leaf nodes

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        self._player = value

    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, value):
        self._right = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self):
        return f"PlayerBNode(player={self.player})"