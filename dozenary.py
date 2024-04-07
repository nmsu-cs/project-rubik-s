# This solver will print the path needed to solve the cube in the least amount of steps.
# It works through a base-12 tree.
# There are 12 movements you can perform on a rubiks cube
#     6 faces x 2 directions = 12
# I used a base-12 tree with each leg being a movement
#     The tree uses a queue for breadth first traversal aka level order traversal

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




def move_upper_cw(upper,front,back,left,right):
    temp = front[0]
    temp2 = front[1]
    front[0] = right[0]
    front[1] = right[1]
    right[0] = back[0]
    right[1] = back[1]
    back[0] = left[0]
    back[1] = left[1]
    left[0] = temp
    left[1] = temp2

    temp3 = upper[0]
    upper[0] = upper[2]
    upper[2] = upper[3]
    upper[3] = upper[1]
    upper[1] = temp3
                
def move_upper_ccw(upper,front,back,left,right):
    temp = front[0]
    temp2 = front[1]
    front[0] = left[0]
    front[1] = left[1]
    left[0] = back[0]
    left[1] = back[1]
    back[0] = right[0]
    back[1] = right[1]
    right[0] = temp
    right[1] = temp2

    temp3 = upper[0]
    upper[0] = upper[1]
    upper[1] = upper[3]
    upper[3] = upper[2]
    upper[2] = temp3
    
def move_down_cw(down,front,back,left,right):
    temp = front[2]
    temp2 = front[3]
    front[2] = left[2]
    front[3] = left[3]
    left[2] = back[2] 
    left[3] = back[3]
    back[2] = right[2]
    back[3] = right[3]
    right[2] = temp
    right[3] = temp2

    temp3 = down[0]
    down[0] = down[2]
    down[2] = down[3]
    down[3] = down[1]
    down[1] = temp3
    
def move_down_ccw(down,front,back,left,right):
    temp = front[2]
    temp2 = front[3]
    front[2] = right[2]
    front[3] = right[3]
    right[2] = back[2]
    right[3] = back[3]
    back[2] = left[2]
    back[3] = left[3]
    left[2] = temp
    left[3] = temp2

    temp3 = down[0]
    down[0] = down[1]
    down[1] = down[3]
    down[3] = down[2]
    down[2] = temp3
    
def move_front_cw(upper,down,front,left,right):
    temp = upper[2]
    temp2 = upper[3]
    upper[2] = left[3]
    upper[3] = left[1]
    left[3] = down[1]
    left[1] = down[0]
    down[0] = right[2]
    down[1] = right[0]
    right[2] = temp2
    right[0] = temp
    temp3 = front[0]
    front[0] = front[2]
    front[2] = front[3]
    front[3] = front[1]
    front[1] = temp3
    
def move_front_ccw(upper,down,front,left,right):
    temp = upper[2]
    temp2 = upper[3]
    upper[2] = right[0]
    upper[3] = right[2]
    right[0] = down[1]
    right[2] = down[0]
    down[1] = left[3]
    down[0] = left[1]
    left[3] = temp
    left[1] = temp2

    temp3 = front[0]
    front[0] = front[1]
    front[1] = front[3]
    front[3] = front[2]
    front[2] = temp3
    
def move_back_cw(upper,down,back,left,right):
    temp = upper[0]
    temp2 = upper[1]
    upper[0] = right[1]
    upper[1] = right[3]
    right[1] = down[3]
    right[3] = down[2]
    down[3] = left[2]
    down[2] = left[0]
    left[2] = temp
    left[0] = temp2

    temp3 = back[0]
    back[0] = back[2]
    back[2] = back[3]
    back[3] = back[1]
    back[1] = temp3
    
def move_back_ccw(upper,down,back,left,right):
    temp = upper[0]
    temp2 = upper[1]
    upper[0] = left[2]
    upper[1] = left[0]
    left[2] = down[3]
    left[0] = down[2]
    down[3] = right[1]
    down[2] = right[3]
    right[1] = temp
    right[3] = temp2

    temp3 = back[0]
    back[0] = back[1]
    back[1] = back[3]
    back[3] = back[2]
    back[2] = temp3
    
def move_left_cw(upper,down,front,back,left):
    temp = upper[0]
    temp2 = upper[2]
    upper[0] = back[3]
    upper[2] = back[1]
    back[3] = down[0]
    back[1] = down[2]
    down[0] = front[0]
    down[2] = front[2]
    front[0] = temp
    front[2] = temp2

    temp3 = left[0]
    left[0] = left[2]
    left[2] = left[3]
    left[3] = left[1]
    left[1] = temp3
    
def move_left_ccw(upper,down,front,back,left):
    temp = upper[0]
    temp2 = upper[2]
    upper[0] = front[0]
    upper[2] = front[2]
    front[0] = down[0]
    front[2] = down[2]
    down[0] = back[3]
    down[2] = back[1]
    back[3] = temp
    back[1] = temp2

    temp3 = left[0]
    left[0] = left[1]
    left[1] = left[3]
    left[3] = left[2]
    left[2] = temp3
    
def move_right_cw(upper,down,front,back,right):
    temp = upper[1]
    temp2 = upper[3]
    upper[1] = front[1]
    upper[3] = front[3]
    front[1] = down[1]
    front[3] = down[3]
    down[1] = back[2]
    down[3] = back[0]
    back[2] = temp
    back[0] = temp2

    temp3 = right[0]
    right[0] = right[2]
    right[2] = right[3]
    right[3] = right[1]
    right[1] = temp3
    
def move_right_ccw(upper,down,front,back,right):
    temp = upper[1]
    temp2 = upper[3]
    upper[1] = back[2]
    upper[3] = back[0]
    back[2] = down[1]
    back[0] = down[3]
    down[1] = front[1]
    down[3] = front[3]
    front[1] = temp
    front[3] = temp2

    temp3 = right[0]
    right[0] = right[1]
    right[1] = right[3]
    right[3] = right[2]
    right[2] = temp3

def check_solved(U,D,F):
    if(U[0] != U[1]): return(FALSE)
    if                     ((U[0] == U[1]) &(U[1] == U[2])&(U[2] == U[3])):
        if                 ((D[0] == D[1]) &(D[1] == D[2])&(D[2] == D[3])):
            if             ((F[0] == F[1]) &(F[1] == F[2])&(F[2] == F[3])):
                return(TRUE)
    else:
        return(FALSE)
    return(FALSE)


# Dozenary tree
def solve_tree(upper,down,front,back,left,right,max_depth):
    # Set Queue and Solve Path
    queue = deque([((upper,down,front,back,left,right),"",0)])

    # Trackers
    solve_path = ""
    visited = set()
    max_depth = 8


    # Level Traverse binary tree through queue
    while queue:
        # Queue
        (c_upper,c_down,c_front,c_back,c_left,c_right), path, depth = queue.popleft()

        # If depth limit reached, stop
        if(depth > max_depth):
            print("Reached Depth Limit: " + str(max_depth) + ". Stopping.")
            break

        # Print Current path and status
        # print("" + path + "   \t\t: ",end="")
        # print(str(check_solved(c_upper,c_front,c_left)))
        
        # If solved, return path
        if(check_solved(c_upper,c_down,c_front)):
            solve_path = path
            break
        
        state = (tuple(c_upper),tuple(c_down),tuple(c_front),tuple(c_back),tuple(c_left),tuple(c_right))
        if state in visited:
            continue
        visited.add(state)
        
        
        # Search next paths
        next_states = []


        move_upper_cw (c_upper,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_down[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "U ->", depth + 1))
        move_upper_ccw(c_upper,c_front, c_back, c_left,c_right)

        move_upper_ccw(c_upper,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_down[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "U'->", depth + 1))
        move_upper_cw (c_upper,c_front, c_back, c_left,c_right)

        move_front_cw (c_upper,c_down,c_front, c_left,c_right)
        next_states.append(((c_upper[:],c_down[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "F ->", depth + 1))
        move_front_ccw(c_upper,c_down,c_front, c_left,c_right)

        move_front_ccw(c_upper,c_down,c_front, c_left,c_right)
        next_states.append(((c_upper[:],c_down[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "F'->", depth + 1))
        move_front_cw (c_upper,c_down,c_front, c_left,c_right)

        move_left_cw  (c_upper,c_down,c_front, c_back, c_left)
        next_states.append(((c_upper[:],c_down[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "L ->",depth+1))
        move_left_ccw (c_upper,c_down,c_front, c_back, c_left)

        move_left_ccw (c_upper,c_down,c_front, c_back, c_left)
        next_states.append(((c_upper[:],c_down[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "L'->",depth+1))
        move_left_cw  (c_upper,c_down,c_front, c_back, c_left)

        queue.extend(next_states)

    
    return(solve_path)

# Store moves in a stack
def str2stack(inString):
    # Moves are a csv string, separate by commas into an array
    move_list = inString.split('->')
    stack = []

    # Store in stack while removing whitespace
    for move in move_list:
        stack.append(move.strip()) 

    stack.reverse()
    return(stack)

def solve(upper,down,front,back,left,right):

    # Start runtime clock
    start_time = time.time()

    solve_path = ""
    max_depth = 15
    solve_path = solve_tree(upper,down,front,back,left,right,max_depth)
    out_stack = str2stack(solve_path)

    print("Solve Steps: " + str(solve_path))
    print("--- %s seconds ---" % (time.time() - start_time))
    return(solve_path)
