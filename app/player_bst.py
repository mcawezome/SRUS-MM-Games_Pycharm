class PlayBST:
    def __init__(self, data):
        self.root = None

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value):
        self._root = value