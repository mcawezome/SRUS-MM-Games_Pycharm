from player_bnode import PlayerBNode

class PlayBST:
    def __init__(self, data=None):
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
            return node
        elif name < node.player.name:
            return self._search(name, node.left)
        else:
            return self._search(name, node.right)

    def balance(self):
        """
        Balance the Binary Search Tree using AVL (Adelson-Velsky and Landis) algorithm.
        
        AVL trees are self-balancing binary search trees where the heights of the two
        child subtrees of any node differ by at most one. This ensures that the tree
        remains approximately balanced, providing O(log n) time complexity for search,
        insert, and delete operations.
        
        The balancing process involves:
        1. Converting the BST to a sorted array using in-order traversal
        2. Rebuilding the tree from the sorted array in a balanced manner
        3. This approach guarantees a perfectly balanced tree
        
        Algorithm Steps:
        1. Perform in-order traversal to get sorted list of nodes
        2. Clear the current tree structure
        3. Rebuild tree by selecting middle element as root recursively
        4. This creates a perfectly balanced tree (height difference ≤ 1)
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for storing the sorted array
        """
        if self.root is None:
            return
        
        # Step 1: Convert BST to sorted array using in-order traversal
        sorted_nodes = []
        self._inorder_traversal(self.root, sorted_nodes)
        
        # Step 2: Clear the current tree
        self.root = None
        
        # Step 3: Rebuild the tree in a balanced manner
        self.root = self._build_balanced_tree(sorted_nodes, 0, len(sorted_nodes) - 1)
    
    def _inorder_traversal(self, node, result):
        """
        Perform in-order traversal to get nodes in sorted order.
        
        In-order traversal visits nodes in the order: left subtree, current node, right subtree.
        For a BST, this produces nodes in ascending order based on their values.
        
        Args:
            node: Current node being visited
            result: List to store nodes in sorted order
        """
        if node is not None:
            # Visit left subtree first (smaller values)
            self._inorder_traversal(node.left, result)
            # Visit current node
            result.append(node)
            # Visit right subtree last (larger values)
            self._inorder_traversal(node.right, result)
    
    def _build_balanced_tree(self, sorted_nodes, start, end):
        """
        Build a balanced tree from a sorted array of nodes.
        
        This method uses a divide-and-conquer approach:
        1. Select the middle element as the root
        2. Recursively build left subtree from left half of array
        3. Recursively build right subtree from right half of array
        
        This ensures that the tree is perfectly balanced because:
        - The root is always the median element
        - Left and right subtrees have equal (or nearly equal) number of nodes
        - Height difference between left and right subtrees is at most 1
        
        Args:
            sorted_nodes: List of nodes in sorted order
            start: Starting index of the current subarray
            end: Ending index of the current subarray
            
        Returns:
            PlayerBNode: Root of the balanced subtree
        """
        # Base case: no elements to process
        if start > end:
            return None
        
        # Find the middle element to use as root
        # This ensures equal distribution of nodes between left and right subtrees
        mid = (start + end) // 2
        
        # Create root node from middle element
        root = sorted_nodes[mid]
        
        # Recursively build left subtree from left half of array
        # This contains all elements smaller than the root
        root.left = self._build_balanced_tree(sorted_nodes, start, mid - 1)
        
        # Recursively build right subtree from right half of array
        # This contains all elements larger than the root
        root.right = self._build_balanced_tree(sorted_nodes, mid + 1, end)
        
        return root
    
    def get_height(self, node):
        """
        Calculate the height of a node in the tree.
        
        The height of a node is the length of the longest path from that node
        to a leaf node. Leaf nodes have height 0.
        
        Args:
            node: The node whose height we want to calculate
            
        Returns:
            int: Height of the node, or -1 if node is None
        """
        if node is None:
            return -1
        return max(self.get_height(node.left), self.get_height(node.right)) + 1
    
    def get_balance_factor(self, node):
        """
        Calculate the balance factor of a node.
        
        The balance factor is the difference between the height of the left subtree
        and the height of the right subtree. For an AVL tree, this factor should
        be between -1 and 1 (inclusive).
        
        Balance factor = height(left subtree) - height(right subtree)
        
        Args:
            node: The node whose balance factor we want to calculate
            
        Returns:
            int: Balance factor of the node
        """
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def is_balanced(self):
        """
        Check if the tree is balanced according to AVL criteria.
        
        A tree is AVL balanced if for every node, the heights of its left and right
        subtrees differ by at most 1.
        
        Returns:
            bool: True if the tree is balanced, False otherwise
        """
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        """
        Recursively check if a subtree is balanced.
        
        Args:
            node: Root of the subtree to check
            
        Returns:
            bool: True if the subtree is balanced, False otherwise
        """
        if node is None:
            return True
        
        # Check if current node is balanced
        balance_factor = self.get_balance_factor(node)
        if abs(balance_factor) > 1:
            return False
        
        # Recursively check left and right subtrees
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))
    
    def display(self):
        """
        Display the tree structure in a readable format.
        """
        if self.root is None:
            print("Empty tree")
            return
        
        self._display_recursive(self.root, "", True)
    
    def _display_recursive(self, node, prefix, is_left):
        """
        Recursively display the tree structure.
        
        Args:
            node: Current node to display
            prefix: String prefix for indentation
            is_left: Whether this node is a left child
        """
        if node is not None:
            print(prefix + ("└── " if is_left else "┌── ") + str(node.player.name))
            new_prefix = prefix + ("    " if is_left else "│   ")
            self._display_recursive(node.left, new_prefix, True)
            self._display_recursive(node.right, new_prefix, False)