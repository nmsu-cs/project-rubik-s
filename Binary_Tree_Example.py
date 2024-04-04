# This is kind of binary search tree.
# It takes a an array x[4] and completes "moves" on them in a binary way
# The moves are shift_left and shift_right
# It uses a binary level traverse algorithm to find which node will leave the 
#   array x in a solved state



# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from collections import deque

# Shift the array values left, move end to opposite end
def move_left(x):
    temp = x[0]
    x[0] = x[1]
    x[1] = x[2]
    x[2] = x[3]
    x[3] = temp

# Shift the array values right, move end to opposite end
def move_right(x):
    temp = x[3]
    x[3] = x[2]
    x[2] = x[1]
    x[1] = x[0]
    x[0] = temp

# A condition to check for a solved array
def check_solved(x):
    return (x == ['a','b','c','d'])
    
# Binary tree
def solve_tree(x,max_depth):
    # Set Queue and Solve Path
    queue = deque([(x,"",0)])
    solve_path = None

    # Traverse binary tree through queue
    while queue:
        # Queue
        current_state, path, depth = queue.popleft()

        # Print Current path and status
        # print("" + path + "   \t: " + str(check_solved(current_state)))
        
        # If solved, return path
        if(check_solved(current_state)):
            solve_path = path
            break

        # If depth limit reached, stop
        if(depth >= max_depth):
            print("Reached Depth Limit: " + str(max_depth) + ". Stopping.")
            break
        
        # Search next paths
        next_states = []
        move_left(current_state)
        next_states.append((current_state[:], path + "left->",depth+1))
        move_right(current_state)
        next_states.append((current_state[:], path + "right->",depth+1))
        queue.extend(next_states)

    print("Solve Steps: " + str(solve_path))




x = ['a','b','d','d']

move_left(x)
move_left(x)
print("Start    : x = [%c,%c,%c,%c]" %(x[0],x[1],x[2],x[3]))
print("Solved at: x = [a,b,c,d]")

max_depth = 20
solve_tree(x,max_depth)

