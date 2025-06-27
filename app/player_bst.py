class PlayBST:
    def __init__(self, data):
        self.root = None

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value):
        self._root = value

    def insert(self, player):
        if self.root is None:
            self.root = PlayerBNode(player)
        else:
            self._insert(player, self.root)

    def _insert(self, player, node):
        if player.name < node.player.name:
            if node.left is None:
                node.left = PlayerBNode(player)
            else:
                self._insert(player, node.left)
        else:
            if node.right is None:
                node.right = PlayerBNode(player)
            else:
                self._insert(player, node.right)

    def search(self, name):
        if self.root is None:
            return None
        else:
            return self._search(name, self.root)

    def _search(self, name, node):
        if node is None:
            return None
        elif node.player.name == name: