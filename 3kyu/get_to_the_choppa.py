'''
Description:

GET TO THE CHOPPA! DO IT NOW!

For this kata you must create a function that will find the shortest possible path between two nodes in a 2D grid of nodes.

Details:

Your function will take three arguments: a grid of nodes, a start node, and an end node. Your function will return a list of nodes that represent, in order, the path that one must follow to get from the start node to the end node. The path must begin with the start node and end with the end node. No single node should be repeated in the path (ie. no backtracking).
def find_shortest_path(grid, start_node, end_node):
  pass
The grid is a list of lists of nodes. Each node object has a position that indicates where in the grid the node is (it's indices).
node.position.x  # 2
node.position.y  # 5
node.position  # (2,5)
node is grid[2][5]  # True
Each node may or may not be 'passable'. All nodes in a path must be passable. A node that is not passable is effectively a wall that the shortest path must go around.
a_node.passable  # True
Diagonal traversals between nodes are NOT allowed in this kata. Your path must move in one of 4 directions at any given step along the path: left, right, up, or down.
Grids will always be rectangular (NxM), but they may or may not be square (NxN).
Your function must return a shortest path for grid widths and heights ranging between 0 and 200. This includes 0x0 and 200x200 grids.
When more than one shortest path exists (different paths, all viable, with the same number of steps) then any one of these paths will be considered a correct answer.
Your function must be efficient enough (in terms of time complexity) to pass all the included tests within the allowed timeframe (6 seconds).
For your convenience, a print_grid function exists that you can use to print a grid. You can also use print_grid to visualize a given path on the given grid. The print_grid function has the following signature:
def print_grid(grid, start_node=None, end_node=None, path=None)
# output without a path
"""
S0110
01000
01010
00010
0001E
"""

# output with a path
"""
S0110
#1###
#1#1#
###1#
0001E
"""
Good luck!
'''



##########MY SOLUTION##########
def get_neighbors(node,grid,grid_x,grid_y):
    neighbors = []
    x = node.position.x
    y = node.position.y
    if x > 0 and grid[x-1][y].passable:
        neighbors.append(grid[x-1][y])
    if x+1 < grid_x and grid[x+1][y].passable:
        neighbors.append(grid[x+1][y])
    if y > 0 and grid[x][y-1].passable:
        neighbors.append(grid[x][y-1])
    if y+1 < grid_y and grid[x][y+1].passable:
        neighbors.append(grid[x][y+1])
    return neighbors

#def find_all_nodes(graph, start='Graph theory'): #graph is a tuple of (node, (tuple of edges))
def find_shortest_path(grid, start_node, end_node):
    grid_x = len(grid)
    if grid_x == 0:
        return []
    grid_y = len(grid[0])
    path_dict_out = {start_node:[start_node]}
    Q = [start_node]
    while Q: #while Q is not empty
        next_Q = []
        for node in Q:
            if node == end_node:
                return path_dict_out[node]
            neighbors = get_neighbors(node,grid, grid_x,grid_y)
            for neighbor in neighbors:
                if neighbor not in path_dict_out:
                    temp = list(path_dict_out[node])
                    temp.append(neighbor)
                    path_dict_out[neighbor] = temp
                    next_Q.append(neighbor)
        Q = next_Q
    return []