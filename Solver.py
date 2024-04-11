# Solver Class
# Called from GUI Main program "Cube.py"
# Function: Will use a game tree algorithm (similar to BST) to 
#         : find the least amount of required moves to solve the Rubik's cube
# Parameters: The current configuration of the cube 
#             through arrays upper,down,front,back,left,right
# Precondition: Parameters must already be defined
# Postcondition: Will return a stack of the next moves

# TODO: Add conditions so the same move can't be repeated more than twice
# TODO: Add condition so one move won't be cancelled out by the next
#       Example: front_clockwise undoes front_counterclockwise
# TODO: Store moves in a stack and make stack accessible from GUI

# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from collections import deque
import time



def solve(upper,down,front,back,left,right):

    # Start runtime clock
    start_time = time.time()


    solve_path = ""
    cube = upper+down+front+back+left+right
    solve_path = solve_tree(cube)

    print("Solve Steps: " + str(solve_path))
    print("--- %s seconds ---" % (time.time() - start_time))
    return(solve_path)


## Movement functions
# Function: These are used in the solver to calculate the solution.
# Parameters: The current confiuration of the cube through arrays
# Precondition: The parameters must already be defined.
#             : If the cube is already solved, will return an empty stack
# Postcondition: The state of the cube must not change while these functions run. Static.

def move_upper_cw(cube):
    temp = cube[8]
    temp2 = cube[9]
    cube[8] = cube[20]
    cube[9] = cube[21]
    cube[20] = cube[12]
    cube[21] = cube[13]
    cube[12] = cube[16]
    cube[13] = cube[17]
    cube[16] = temp
    cube[17] = temp2

    temp3 = cube[0]
    cube[0] = cube[2]
    cube[2] = cube[3]
    cube[3] = cube[1]
    cube[1] = temp3
                
def move_upper_ccw(cube):
    temp = cube[8]
    temp2 = cube[9]
    cube[8] = cube[16]
    cube[9] = cube[17]
    cube[16] = cube[12]
    cube[17] = cube[13]
    cube[12] = cube[20]
    cube[13] = cube[21]
    cube[20] = temp
    cube[21] = temp2

    temp3 = cube[0]
    cube[0] = cube[1]
    cube[1] = cube[3]
    cube[3] = cube[2]
    cube[2] = temp3
    
def move_front_cw(cube):
    temp = cube[2]
    temp2 = cube[3]
    cube[2] = cube[19]
    cube[3] = cube[17]
    cube[19] = cube[5]
    cube[17] = cube[4]
    cube[4] = cube[22]
    cube[5] = cube[20]
    cube[22] = temp2
    cube[20] = temp
    temp3 = cube[8]
    cube[8] = cube[10]
    cube[10] = cube[11]
    cube[11] = cube[9]
    cube[9] = temp3
    
def move_front_ccw(cube):
    temp = cube[2]
    temp2 = cube[3]
    cube[2] = cube[20]
    cube[3] = cube[22]
    cube[20] = cube[5]
    cube[22] = cube[4]
    cube[5] = cube[19]
    cube[4] = cube[17]
    cube[19] = temp
    cube[17] = temp2

    temp3 = cube[8]
    cube[8] = cube[9]
    cube[9] = cube[11]
    cube[11] = cube[10]
    cube[10] = temp3
    
def move_left_cw(cube):
    temp = cube[0]
    temp2 = cube[2]
    cube[0] = cube[15]
    cube[2] = cube[13]
    cube[15] = cube[4]
    cube[13] = cube[6]
    cube[4] = cube[8]
    cube[6] = cube[10]
    cube[8] = temp
    cube[10] = temp2

    temp3 = cube[16]
    cube[16] = cube[18]
    cube[18] = cube[19]
    cube[19] = cube[17]
    cube[17] = temp3
    
def move_left_ccw(cube):
    temp = cube[0]
    temp2 = cube[2]
    cube[0] = cube[8]
    cube[2] = cube[10]
    cube[8] = cube[4]
    cube[10] = cube[6]
    cube[4] = cube[15]
    cube[6] = cube[13]
    cube[15] = temp
    cube[13] = temp2

    temp3 = cube[16]
    cube[16] = cube[17]
    cube[17] = cube[19]
    cube[19] = cube[18]
    cube[18] = temp3
    

# Check_Solved Function:
# Function: Utilized by the solve_tree function to determine if a state is solved
# Parameters: The upper, lower, and front face of the cube. 
# Precondition: The input parameters must already be defined. 
# Note: A cube is solved if 3 adjacent faces are solved
def Check_Solved(cube):
    if(cube[0] != cube[1]): return(FALSE)
    if                     ((cube[0] == cube[1]) &(cube[1] == cube[2])&(cube[2] == cube[3])):
        if                 ((cube[16] == cube[17]) &(cube[17] == cube[18])&(cube[18] == cube[19])):
            if             ((cube[8] == cube[9]) &(cube[9] == cube[10])&(cube[10] == cube[11])):
                return(TRUE)
    else:
        return(FALSE)
    return(FALSE)


# Game Tree
def solve_tree(cube):
    # Set Queue and Solve Path
    queue = deque([(cube,"",0)])

    # Trackers
    solve_path = ""
    visited = set()
    max_depth = 10


    # Level Traverse binary tree through queue
    while queue: 
        # Queue
        cube, path, depth = queue.popleft()

        # If depth limit reached, stop
        if(depth > max_depth):
            print("Reached Depth Limit: " + str(max_depth) + ". Stopping.")
            break

        # If solved, return path
        if(Check_Solved(cube)):
            solve_path = path
            break
        
        # Check if the state has been checked
        state = tuple(cube)
        if state in visited:
            continue
        visited.add(state)

        # Search next paths
        move_functions = [
            (move_upper_cw, "U -"),
            (move_upper_ccw, "U'-"),
            (move_front_cw, "F -"),
            (move_front_ccw, "F'-"),
            (move_left_cw, "L -"),
            (move_left_ccw, "L'-")
        ]

        for move_function, move_str in move_functions:
            new_cube = cube[:]  # Create a copy of the cube state
            move_function(new_cube)
            queue.append((new_cube, path + move_str, depth + 1))


    return(solve_path)


# # # Cube 10 steps
# upper = ['w', 'b', 'r', 'y']
# down =  ['w', 'w', 'y', 'w']
# front = ['y', 'g', 'b', 'b'] 
# back =  ['o', 'g', 'o', 'r']
# left =  ['r', 'g', 'b', 'o'] 
# right = ['o', 'y', 'r', 'g']

# # # Cube 8 steps
# # upper = ['w','y','y','w']
# # down =  ['y','w','w','y']
# front = ['b','b','b','b']
# back  = ['g','g','g','g']
# left  = ['r','o','o','r']
# right = ['o','r','r','o']

# solve(upper,down,front,back,left,right)