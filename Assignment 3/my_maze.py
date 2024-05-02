from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class MyMaze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str = ''):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string,
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is empty.
        """
        if len(maze_str) == 0:
            raise ValueError
        else:
            # We internally treat this as a List[List[str]], as it makes indexing easier.
            self._maze = list(list(row) for row in maze_str.splitlines())
            self._row_range = len(self._maze)
            self._col_range = len(self._maze[0])
            self._exits: List[Tuple[int, int]] = []
            self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        """Find and save all exits into `self._exits` using recursion, save 
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """
        pass
        # TODO
        if start_row not in range(self._row_range) or start_col not in range(self._col_range):
            raise ValueError("Starting Position out of range")
        self._max_recursion_depth = depth
        row_movement = [0,1,1,1,0,-1,-1,-1]
        col_movement = [1,1,0,-1,-1,-1,0,1]
        if depth == 0:
            x, y = start_row+1, start_col+1
            self._maze[x][y] = START
            for i in range(8):
                if self._maze[x+row_movement[i]][y+col_movement[i]] == PATH:
                    self.find_exits(x+row_movement[i],y+col_movement[i],depth=depth+1)
        else: 
            #if depth < 13:
            x, y = start_row, start_col
            self._maze[x][y] = VISITED
            #self._exits.append((start_row-1,start_col-1))
            for i in range(8):
                if self._maze[x+row_movement[i]][y+col_movement[i]] == PATH and x+row_movement[i] in [0,self._row_range-1] or y+col_movement[i] in [0, self._col_range-1] and self._maze[x+row_movement[i]][y+col_movement[i]] == PATH:
                    self._maze[x+row_movement[i]][y+col_movement[i]] = EXIT
                    self._exits.append(f"Exit at: {(x+row_movement[i],y+col_movement[i])}")
                elif self._maze[x+row_movement[i]][y+col_movement[i]] == PATH:
                    self.find_exits(x+row_movement[i],y+col_movement[i],depth=depth+1)
        if len(self.exits) > 0:
            return True
        else:
            return False



    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__

#x = MyMaze("  -1012345678910\n-1 ############\n 0 # #  # ##  #\n 1 # # #  # # #\n 2 ## #  # #  #\n 3 #  # #  # ##\n 4 # # ## # # #\n 5 #  #  # #  #\n 6 ## ## ##  ##\n 7 # ##  ## # #\n 8 # # #  # # #\n 9 #  # #  #  #\n10 ############")
#maze = """###### ###########
##  # ##  ##  # ##
# ## #####  # ## #
# # #   # #    ###
##  ## # ## # ##  
## # ###  # #  # #
# # ## ##  #  # ##
# #  #   # # ##  #
#  ###  # ####  ##
##  # #  #   #   #
 # # # # ## # ## #
# # ### #  # # # #
# ## ### ##  ## ##
## ## # #  # # # #
# # # ## #### # ##
## ## ## ###  # ##
# #  # # #  # ## #
### ##############
#"""
#x = MyMaze(maze)
#print(x.find_exits(8,9))
#print(x)
#print(x.exits)
#print(x.max_recursion_depth)
# """             1111111
# -101234567890123456
#"""
#-1-1-1  -1 0 1     (-1,-1) (-1,0) (-1,1)
# 0 S 0  -1 S 1     (0, -1) (0, 0) (0, 1)
# 1 1 1  -1 0 1     (1, -1) (1, 0) (1, 1)