# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from collections import deque
import os


def move_left(x):
    temp = x[0]
    x[0] = x[1]
    x[1] = x[2]
    x[2] = x[3]
    x[3] = temp

def move_right(x):
    temp = x[3]
    x[3] = x[2]
    x[2] = x[1]
    x[1] = x[0]
    x[0] = temp

def check_solved(x):
    return (x == ['a','b','c','d'])
    

def solve_tree(x):
    queue = deque([(x,"")])

    while queue:
        current_state, path = queue.popleft()
        print("" + path + "   \t: " + str(check_solved(current_state)))
        
        if(check_solved(current_state)):
            return(True)
        
        next_states = []
        move_left(current_state)
        next_states.append((current_state[:], path + "left->"))
        move_right(current_state)
        next_states.append((current_state[:], path + "right->"))
        queue.extend(next_states)
    return(FALSE)




x = ['a','b','c','d']

move_left(x)
move_left(x)
print("Start    : x = [%c,%c,%c,%c]" %(x[0],x[1],x[2],x[3]))
print("Solved at: x = [a,b,c,d]")


depth = 8
if solve_tree(x):
    print("TEST_SOLVABLE")
else:
    print("TEST UNSOLVABLE")