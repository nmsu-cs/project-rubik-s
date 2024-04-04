# This is kind of ternary search tree.
# It takes a an array x[4] and completes "moves" on them in a binary way
# The moves are shift_left and shift_right
# It uses a binary level traverse algorithm to find which node will leave the 
#   array x in a solved state



# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from collections import deque


# Start runtime clock
import time
start_time = time.time()

# Shift the array values left, move end to opposite end
def move_left(x,y):
    temp = x[0]
    x[0] = x[1]
    x[1] = x[2]
    x[2] = x[3]
    x[3] = temp

# Shift the array values right, move end to opposite end
def move_right(x,y):
    temp = x[3]
    x[3] = x[2]
    x[2] = x[1]
    x[1] = x[0]
    x[0] = temp

def move_upper(x,y):
    print()

def move_lower(x,y):
    print()

# A condition to check for a solved array
def check_solved(x,y):
    return (x == ['a','b','c','d'])
    
# Binary tree
def solve_tree(x,y,max_depth):
    # Set Queue and Solve Path
    queue = deque([((x,y),"",0)])
    solve_path = None

    # Traverse binary tree through queue
    while queue:
        # Queue
        (current_state_x,current_state_y), path, depth = queue.popleft()

        # Print Current path and status
        # print("" + path + "   \t: " + str(check_solved(current_state)))
        
        # If solved, return path
        if(check_solved(current_state_x,current_state_y)):
            solve_path = path
            break

        # If depth limit reached, stop
        if(depth >= max_depth):
            print("Reached Depth Limit: " + str(max_depth) + ". Stopping.")
            break
        
        # Search next paths
        next_states = []
        move_left(current_state_x,current_state_y)
        next_states.append(((current_state_x[:],current_state_y[:]), path + "left->",depth+1))
        move_right(current_state_x,current_state_y)
        next_states.append(((current_state_x[:],current_state_y[:]), path + "right->",depth+1))
        move_upper(current_state_x,current_state_y)
        next_states.append(((current_state_x[:],current_state_y[:]), path + "upper->", depth + 1))
        move_lower(current_state_x,current_state_y)
        next_states.append(((current_state_x[:],current_state_y[:]), path + "lower->", depth + 1))
        queue.extend(next_states)

    print("Solve Steps: " + str(solve_path))




x = ['a','b','c','d']
y = ['a','b','c','d']

move_left(x,y)
move_left(x,y)
print("Start    : x = [%c,%c,%c,%c]" %(x[0],x[1],x[2],x[3]))
print("Solved at: x = [a,b,c,d]")

max_depth = 3
solve_tree(x,y,max_depth)


print("--- %s seconds ---" % (time.time() - start_time))