#Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.


def find_path(grid):
    if grid is None or len(grid) == 0:
        return None
    path = list()
    cache = {}

    if _find_path(grid,len(grid),len(grid[0])-1,path,cache):
        return path
    else:
        return None

def _find_path(grid,r,c,path,cache):
    if r < 0 or c < 0 or not grid[r][c]:
        return False
    if (r,c) in cache:
        return cache[(r,c)]
    else:
        is_at_origin = r==0 and c ==0
        is_in_path = False
        if is_at_origin or _find_path(grid,r-1,c,path,cache) or _find_path(grid,r,c-1,path,cache):
            path.append((r,c))
            is_in_path = True
        cache[(r,c)] = is_in_path
        return is_in_path