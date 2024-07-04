from typing import Any, Generator, Tuple

from tree_node import TreeNode

def insert_recursive(key, value, current_node: TreeNode):
    if key == current_node.key:
        raise KeyError(f"Key: {key} already exists")
    elif key < current_node.key:
        if current_node.left == None:
            current_node.left = TreeNode(key, value)
        else: 
            insert_recursive(key, value, current_node.left)
    elif key > current_node.key:
        if current_node.right == None:
            current_node.right = TreeNode(key, value)
        else:
            insert_recursive(key, value, current_node.right)

def find_recursive(key, current_node: TreeNode):
    if key == current_node.key:
        return current_node
    elif key > current_node.key and current_node.right != None:
        find_recursive(key, current_node.right)
    elif key < current_node.key and current_node.left != None:
        find_recursive(key, current_node.left)
    else: 
        raise KeyError(f"Key: {key} is not in the Tree")
    
def recursive_size(current_node: TreeNode, counter):
    if current_node != None:
        counter += 1
        recursive_size(current_node.left, counter)
        recursive_size(current_node.right, counter)

def remove_search(current_node: TreeNode):
    if current_node.left == None:
        return [current_node, current_node.right, current_node.parent]
    else: 
        remove_search(current_node.left)

def recursive_comparison(self, current_node: TreeNode, key: int, tree_comparisons: int):
    tree_comparison = tree_comparisons
    if current_node.key == key:
        tree_comparison += 1
        self = tree_comparison
        return self
    if current_node.key != key:
        tree_comparison += 1
    elif key > current_node.key:
        tree_comparison += 1
        recursive_comparison(current_node.right, key, tree_comparison)
    elif key < current_node.key:
        tree_comparison += 1
        recursive_comparison(current_node.left, key, tree_comparison)

def validation_search(current_node: TreeNode, validator: bool):
    if validator == False:
        return validator
    comparison_key = current_node.key
    if current_node.left != None:
        if current_node.left.key < comparison_key:
            validation_search(current_node.left, validator)
        else: 
            validator = False
            return validator
    elif current_node.right != None:
        if current_node.right.key > comparison_key:
            validation_search(current_node.right, validator)
        else: 
            validator = False
            return validator

def inorder_search(current_node: TreeNode, list_of_node_keys: list):
    if current_node != None:
        inorder_search(current_node.left, list_of_node_keys)
        list_of_node_keys.append(current_node.key)
        inorder_search(current_node.right, list_of_node_keys)

def preorder_search(current_node: TreeNode, list_of_node_keys: list):
    if current_node != None:
        list_of_node_keys.append(current_node.key)
        preorder_search(current_node.left, list_of_node_keys)
        preorder_search(current_node.right, list_of_node_keys)

def postorder_search(current_node: TreeNode, list_of_node_keys: list):
    if current_node != None:
        postorder_search(current_node.left, list_of_node_keys)
        postorder_search(current_node.right, list_of_node_keys)
        list_of_node_keys.append(current_node.key)

class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is neither a TreeNode nor None.
        """
        self._root = root
        self._size = 0 if root is None else 1
        self._num_of_comparisons = 0

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """

        if type(key) != int:
            raise ValueError("Key must be an integer")
        if self._root == None:
            self._root = TreeNode(key=key, value=value)
        else:
            current_node = self._root
            insert_recursive(key=key, value=value, current_node=current_node)
            

    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """

        if type(key) != int:
            raise ValueError("Key must be an integer")
        current_node = self._root
        while current_node.key != key:
            if key < current_node.key and current_node.left != None:
                current_node = current_node.left
            elif key > current_node.key and current_node.right != None:
                current_node = current_node.right
            else: 
                raise KeyError(f"Key: {key} is not in the BST")
        else: 
            return current_node

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""

        counter = 0
        for i in self._inorder(self._root):
            counter += 1
        self._size = counter
        return self._size

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size 

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        node_to_remove = self.find(key)
        if node_to_remove == self._root and node_to_remove.is_internal:
            replacement_nodes = remove_search(node_to_remove.right.left)
            replacement_nodes[0].parent = None
            replacement_nodes[0].left = node_to_remove.left
            replacement_nodes[0].right = node_to_remove.right
            replacement_nodes[2].left = replacement_nodes[1]
        elif node_to_remove == self._root and node_to_remove.is_external:
            node_to_remove = None

        parent = node_to_remove.parent
        child_left = node_to_remove.left
        child_right = node_to_remove.right
        if child_left == None and child_right == None:
            if node_to_remove.key < parent.key:
                parent.left = None
            elif node_to_remove.key > parent.key:
                parent.right = None
        elif child_left == None:
            if node_to_remove.key < parent.key:
                parent.left = child_right
            elif node_to_remove.key > parent.key:
                parent.right = child_right
        elif child_right == None:
            if node_to_remove.key < parent.key:
                parent.left = child_left
            elif node_to_remove.key > parent.key:
                parent.right = child_left
        else: 
            left_child_left = child_left.left
            right_child_left = child_left.right
            left_child_right = child_right.left
            right_child_right = child_right.right
            if (left_child_left == None and right_child_left == None) or (right_child_left == None):
                child_left.right = node_to_remove.right
                child_left.parent = parent
            elif (left_child_right == None and right_child_right == None) or (left_child_right == None):
                child_right.left = node_to_remove.left
                child_right.parent = parent
            else: 
                replacement_nodes = remove_search(node_to_remove.right.left)
                if node_to_remove == parent.left:
                    parent.left = replacement_nodes[0]
                    replacement_nodes[0].left = node_to_remove.left
                    replacement_nodes[0].right = node_to_remove.right
                    replacement_nodes[2].left = replacement_nodes[1]
                elif node_to_remove == parent.right:
                    parent.right = replacement_nodes[0]
                    replacement_nodes[0].left = node_to_remove.left
                    replacement_nodes[0].right = node_to_remove.right
                    replacement_nodes[2].left = replacement_nodes[1]
            
       
    # Hint: The following 3 methods can be implemented recursively, and 
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        yield from self._inorder(node)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._preorder(node)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._postorder(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]: 
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        validator = True
        return validation_search(self._root, validator)
        
    def return_max_key(self) -> TreeNode:
            """Return the node with the largest key (None if tree is empty)."""
            if self._root == None:
                return None
            else: 
                key_list = self._inorder(self._root)
                max_node = self.find(key_list[-1])
                return max_node

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(self)
        list_comparisons = 0
        for i in python_list:
            if i != key:
                list_comparisons += 1
            else: 
                list_comparisons += 1
                break

        tree_comparisons = 0
        recursive_comparison(self._num_of_comparisons, self._root, key, tree_comparisons)
        
        return tuple([list_comparisons, self._num_of_comparisons])

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        list_of_node_keys = []
        inorder_search(current_node, list_of_node_keys)
        return list_of_node_keys

    def _preorder(self, current_node):
        list_of_node_keys = []
        preorder_search(current_node, list_of_node_keys)
        return list_of_node_keys

    def _postorder(self, current_node):
        list_of_node_keys = []
        postorder_search(current_node, list_of_node_keys)
        return list_of_node_keys

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)

#################### TEST ZONE ####################
bst = BinarySearchTree(TreeNode(5, 5))
for i in [4,1,3,2,7,6,8]:
    bst.insert(i,i)
print(bst)
node = bst.find(6)
print(node.depth)
print(node.is_external)
print(node.is_internal)
#print(bst.size)
#print(bst.remove(6))
#print(bst)
#print(bst.__getitem__(6))
#print(list(bst))
#print(bst.is_valid)
#print(bst.return_max_key())
print(bst.find_comparison(2))
#print(bst.get_root())