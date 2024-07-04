from typing import Any


class TreeNode:
    
    def __init__(self, key: int, value: Any, right: 'TreeNode' = None, 
                 left: 'TreeNode' = None, parent: 'TreeNode' = None):
        """Initialize TreeNode.

        Args:
            key (int): Key used for sorting the node into a BST.
            value (Any): Whatever data the node shall carry.
            right (TreeNode, optional): Node to the right, with a larger key. Defaults to None.
            left (TreeNode, optional): Node to the left, with a lesser key. Defaults to None.
            parent (TreeNode, optional): Parent node. Defaults to None.
        """
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

    def __repr__(self) -> str:
        return f"TreeNode({self.key}, {self.value})"

    @property
    def depth(self) -> int:
        """Return depth of the node, i.e. the number of parents/grandparents etc.

        Returns:
            int: Depth of node
        """
        pass
        depth = 0
        while True:
            if self.parent == None:
                break
            else:
                depth += 1
        return depth

    @property
    def is_external(self) -> bool:
        """Return if node is an external node (= leaf)."""
        pass
        # TODO
        if self.right == None and self.left == None:
            return True
        else:
            return False
   
    @property
    def is_internal(self) -> bool: 
        """Return if node is an internal node."""
        pass
        # TODO
        if self.right == None and self.left == None:
            return False
        else:
            return True
 
    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)

