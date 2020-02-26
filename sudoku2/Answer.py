def sudoku2(grid):
    #check row
    for i in range(9):
        if not check_line(grid[i]):
            return(False)
    
    #check col
    for i in range(9):
        col = []
        for j in range(9):
            col.append(grid[j][i])
        if not check_line(col):
            return(False)
    
    #check square
    pos = [-1, -1]
    for i in range(3):
        pos[1] = (i % 3) * 3
        for j in range(3):
            pos[0] = (j % 3) * 3
            if not check_square(grid, pos):
                return(False)
    return(True)

#check to see that a vertical or horizontal line is valid
def check_line(line):
    check = set()
    for i in range(len(line)):
        if line[i] != ".":
            if line[i] not in check:
                check.add(line[i])
            else:
                return(False)
    return(True)

#check to see if a square is valid
def check_square(grid, pos):
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    check = set()

    for a in range(box_y * 3, box_y * 3 + 3):
        for b in range(box_x * 3, box_x * 3 + 3):
            if grid[a][b] != ".":
                if grid[a][b] in check:
                    return(False)
                else:
                    check.add(grid[a][b])
    return(True)
