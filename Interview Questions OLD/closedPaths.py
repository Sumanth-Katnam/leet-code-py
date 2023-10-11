def closedPaths(grid):
    visited = [] # add tuples to this

    def dfs(i, j, dir, current, target):

        if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] != target:
            return False

        if (i, j, dir) in visited:
            return True

        visited.append((i, j, dir))
        
        next_dir = dir_map[(current, dir)] # ['l', 'd']
        target = target * -1
        return dfs(i + dir_pos[next_dir][0], j + dir_pos[next_dir][1], next_dir, grid[i][j], target)

    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res = False
            for dir in dirs:
                if (i, j, dir) not in visited:
                    target = grid[i][j] * -1
                    res = res or dfs(i + dir_pos[dir][0], j + dir_pos[dir][1], dir, grid[i][j], target)

            if res:
                count += 1

    return int(count/4)

dirs = ['l', 'r', 'u', 'd']
dir_pos = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}
# dir_map = {
#     (1, 'r'):['l', 'd'],
#     (1, 'd'):['u','r'],
#     (1, 'u'):['d', 'l'],
#     (1, 'l'):['r', 'u'],
#     (-1, 'r'):['l','u'],
#     (-1, 'd'):['u','l'],
#     (-1, 'u'):['d','r'],
#     (-1, 'l'):['r','d']
# }

dir_map = {
    (1, 'r'):'d',
    (1, 'd'):'r',
    (1, 'u'):'l',
    (1, 'l'):'u',
    (-1, 'r'):'u',
    (-1, 'd'):'l',
    (-1, 'u'):'r',
    (-1, 'l'):'d'
}

if __name__ == "__main__":
    # string = "\\//\\\\/\n\\///\\/\n//\\\\/\\\n\\/\\///"
    string = "/\\/\\\n\\/\\/"
    grid = []
    row = []
    for char in string:
        if char == '\n':
            grid.append(row)
            row = []
        else:
            if char == "\\":
                row.append(-1)
            elif char == "/":
                row.append(1)
            else:
                row.append(0) # Not handled yet
    grid.append(row)
    print(grid)
    print(closedPaths(grid))






# import json
# import ast
# def countComponents(grid):
#   count = 0
#   dir = {('f','l'):[(0,-1,"r"),(0,0,"t")],
#          ('f','t'):[(0,0,"l"),(-1,0,"b")],
#          ('f','r'):[(0,1,"l"),(0,0,"b")],
#          ('f','b'):[(1,0,"t"),(0,0,"r")],
#          ('b','t'):[(-1,0,"b"),(0,0,"r")],
#          ('b','b'):[(1,0,"t"),(0,0,"l")],
#          ('b','l'):[(0,0,"b"),(0,-1,"r")],
#          ('b','r'):[(0,0,"u"),(0,1,"l")]}

#   traingles = ["l","r","t","b"]
#   visited = set()# r,c,pos(l,r,t,b)
#   ROWS, COLS = len(grid), len(grid[0])
#   print(dir[('f', 'l')])
  
#   def dfs(r,c,pos):
#     if (r not in range(ROWS) or # row exit
#         c not in range(COLS)): # column exit
#       return False#
#     visited.add((r,c,pos)) 
#     curPos = (grid[r][c], pos)
#     res = True
#     for (newR, newC, newP) in dir.get(curPos,[]):
#       print(newR, newC, newP)
#       if (newR, newC, newP) not in visited and not dfs(r + newR, c + newC, newP): 
#         res = False #
#     return res
    
#   for r in range(ROWS):
#     for c in range(COLS):
#       for dir in traingles:
#         currentSet = set()
#         if (r, c, dir) not in visited and dfs(r, c,dir):
#             count += 1
            
#   return count

# grid = [["f","b","f"],
#         ["b","f","b"],
#         ["b","f","b"]]

# print(countComponents(grid))