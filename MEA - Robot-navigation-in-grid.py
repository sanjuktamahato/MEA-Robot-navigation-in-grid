
GRID_SIZE = 5


current_position = [0, 0]  
goal_position = [4, 4]     

while current_position != goal_position:
    
    print("Current Position:", current_position)
    print("Goal Position:", goal_position)
    
    
    x_diff = goal_position[0] - current_position[0]
    y_diff = goal_position[1] - current_position[1]
    
    
    if abs(x_diff) > abs(y_diff):
        if x_diff > 0:
            current_position[0] += 1  
        elif x_diff < 0:
            current_position[0] -= 1  
    else:
        if y_diff > 0:
            current_position[1] += 1  
        elif y_diff < 0:
            current_position[1] -= 1  

    
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    x, y = current_position
    grid[x][y] = 'R'
    
    for row in grid:
        print(" ".join(row))
    print("\n")
    

print("Goal reached at:", current_position)



