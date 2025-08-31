import random

def getPathRec(grid, i ,j, path, visited):
    if i < 0 or j < 0 or (i,j) in visited or grid[i][j] == "X":
        return False
    if (i==0 and j==0) or \
        getPathRec(grid, i-1,j,path, visited) or \
        getPathRec(grid, i, j-1, path, visited):
        path.append((i,j))
        return True
    visited.add((i,j))
    return False

def getPath(g):
    if not g or len(g) < 1:
        return None
    path = []
    gotPath = getPathRec(g, len(g)-1, len(g[0]) - 1, path, set())
    if gotPath: return path
    return None


cols = 4000
rows = 3000
g = [["." for _ in range(cols)] for _ in range(rows)]
for _ in range(random.randint((cols*rows)//10, (cols*rows)//5)):
    randi = random.randint(0,rows-1)
    randj = random.randint(0,cols-1)
    if (randi==0 and randj==0) or (randi==rows-1 and randj==cols-1):
        continue
    g[randi][randj] = "X"

# for row in g:
#     print(''.join(row))

# gstr = """.XX.
# ....
# ..X."""
#
# g = [list(row) for row in gstr.split()]

print(getPath(g))