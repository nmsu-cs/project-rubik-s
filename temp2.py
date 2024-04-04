# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from collections import deque


# Start runtime clock
import time
start_time = time.time()


def move_upper_cw(upper,lower,front,back,left,right):
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
                
def move_upper_ccw(upper,lower,front,back,left,right):
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
    
def move_lower_cw(upper,lower,front,back,left,right):
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

    temp3 = lower[0]
    lower[0] = lower[2]
    lower[2] = lower[3]
    lower[3] = lower[1]
    lower[1] = temp3
    
def move_lower_ccw(upper,lower,front,back,left,right):
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

    temp3 = lower[0]
    lower[0] = lower[1]
    lower[1] = lower[3]
    lower[3] = lower[2]
    lower[2] = temp3
    
def move_front_cw(upper,lower,front,back,left,right):
    temp = upper[2]
    temp2 = upper[3]
    upper[2] = left[3]
    upper[3] = left[1]
    left[3] = lower[1]
    left[1] = lower[0]
    lower[0] = right[2]
    lower[1] = right[0]
    right[2] = temp2
    right[0] = temp
    temp3 = front[0]
    front[0] = front[2]
    front[2] = front[3]
    front[3] = front[1]
    front[1] = temp3
    
def move_front_ccw(upper,lower,front,back,left,right):
    temp = upper[2]
    temp2 = upper[3]
    upper[2] = right[0]
    upper[3] = right[2]
    right[0] = lower[1]
    right[2] = lower[0]
    lower[1] = left[3]
    lower[0] = left[1]
    left[3] = temp
    left[1] = temp2

    temp3 = front[0]
    front[0] = front[1]
    front[1] = front[3]
    front[3] = front[2]
    front[2] = temp3
    
def move_back_cw(upper,lower,front,back,left,right):
    temp = upper[0]
    temp2 = upper[1]
    upper[0] = right[1]
    upper[1] = right[3]
    right[1] = lower[3]
    right[3] = lower[2]
    lower[3] = left[2]
    lower[2] = left[0]
    left[2] = temp
    left[0] = temp2

    temp3 = back[0]
    back[0] = back[2]
    back[2] = back[3]
    back[3] = back[1]
    back[1] = temp3
    
def move_back_ccw(upper,lower,front,back,left,right):
    temp = upper[0]
    temp2 = upper[1]
    upper[0] = left[2]
    upper[1] = left[0]
    left[2] = lower[3]
    left[0] = lower[2]
    lower[3] = right[1]
    lower[2] = right[3]
    right[1] = temp
    right[3] = temp2

    temp3 = back[0]
    back[0] = back[1]
    back[1] = back[3]
    back[3] = back[2]
    back[2] = temp3
    
def move_left_cw(upper,lower,front,back,left,right):
    temp = upper[0]
    temp2 = upper[2]
    upper[0] = back[3]
    upper[2] = back[1]
    back[3] = lower[0]
    back[1] = lower[2]
    lower[0] = front[0]
    lower[2] = front[2]
    front[0] = temp
    front[2] = temp2

    temp3 = left[0]
    left[0] = left[2]
    left[2] = left[3]
    left[3] = left[1]
    left[1] = temp3
    
def move_left_ccw(upper,lower,front,back,left,right):
    temp = upper[0]
    temp2 = upper[2]
    upper[0] = front[0]
    upper[2] = front[2]
    front[0] = lower[0]
    front[2] = lower[2]
    lower[0] = back[3]
    lower[2] = back[1]
    back[3] = temp
    back[1] = temp2

    temp3 = left[0]
    left[0] = left[1]
    left[1] = left[3]
    left[3] = left[2]
    left[2] = temp3
    
def move_right_cw(upper,lower,front,back,left,right):
    temp = upper[1]
    temp2 = upper[3]
    upper[1] = front[1]
    upper[3] = front[3]
    front[1] = lower[1]
    front[3] = lower[3]
    lower[1] = back[2]
    lower[3] = back[0]
    back[2] = temp
    back[0] = temp2

    temp3 = right[0]
    right[0] = right[2]
    right[2] = right[3]
    right[3] = right[1]
    right[1] = temp3
    
def move_right_ccw(upper,lower,front,back,left,right):
    temp = upper[1]
    temp2 = upper[3]
    upper[1] = back[2]
    upper[3] = back[0]
    back[2] = lower[1]
    back[0] = lower[3]
    lower[1] = front[1]
    lower[3] = front[3]
    front[1] = temp
    front[3] = temp2

    temp3 = right[0]
    right[0] = right[1]
    right[1] = right[3]
    right[3] = right[2]
    right[2] = temp3

# def check_solved(upper,lower,front,back,left,right):
#     if                     ((upper[0] == upper[1]) &(upper[1] == upper[2])&(upper[2] == upper[3])):
#         if                 ((lower[0] == lower[1]) &(lower[1] == lower[2])&(lower[2] == lower[3])):
#             if             ((front[0] == front[1]) &(front[1] == front[2])&(front[2] == front[3])):
#                 if         (( back[0] ==  back[1]) &( back[1] ==  back[2])&( back[2] ==  back[3])):
#                     if     (( left[0] ==  left[1]) &( left[1] ==  left[2])&( left[2] ==  left[3])):
#                         if ((right[0] == right[1]) &(right[1] == right[2])&(right[2] == right[3])):
#                             return(TRUE)
#     else:
#         return(FALSE)
#     return(FALSE)


def check_solved(U,D,F,B,L,R):
    if                     ((U[0] == U[1]) &(U[1] == U[2])&(U[2] == U[3])):
        if                 ((D[0] == D[1]) &(D[1] == D[2])&(D[2] == D[3])):
            if             ((F[0] == F[1]) &(F[1] == F[2])&(F[2] == F[3])):
                if         ((B[0] == B[1]) &(B[1] == B[2])&(B[2] == B[3])):
                    if     ((L[0] == L[1]) &(L[1] == L[2])&(L[2] == L[3])):
                        if ((R[0] == R[1]) &(R[1] == R[2])&(R[2] == R[3])):
                            return(TRUE)
    else:
        return(FALSE)
    return(FALSE)


# Binary tree
def solve_tree(upper,lower,front,back,left,right,max_depth):
    # Set Queue and Solve Path
    queue = deque([((upper,lower,front,back,left,right),"",0)])
    solve_path = None

    # Traverse binary tree through queue
    while queue:
        # Queue
        (c_upper,c_lower,c_front,c_back,c_left,c_right), path, depth = queue.popleft()



        # If depth limit reached, stop
        if(depth > max_depth):
            print("Reached Depth Limit: " + str(max_depth) + ". Stopping.")
            break



        # Print Current path and status
        # print("" + path + "   \t: " )
        # print(c_upper+c_lower+c_front+c_back+c_left+c_right)
        
        # If solved, return path
        if(check_solved(c_upper,c_lower,c_front,c_back,c_left,c_right)):
            solve_path = path
            break
        
        # Search next paths
        next_states = []

        move_upper_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "U->", depth + 1))
        move_upper_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_upper_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "U'->", depth + 1))
        move_upper_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_lower_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "D->", depth + 1))
        move_lower_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_lower_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "D'->", depth + 1))
        move_lower_cw(c_upper,c_lower,c_front, c_back, c_left,c_right)


        move_front_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "F->", depth + 1))
        move_front_ccw (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_front_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "F'->", depth + 1))
        move_front_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_back_cw  (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "B->", depth + 1))
        move_back_ccw (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_back_ccw (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "B'->", depth + 1))
        move_back_cw  (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_left_cw  (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "L->",depth+1))
        move_left_ccw (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_left_ccw (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "L'->",depth+1))
        move_left_cw  (c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_right_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "R->",depth+1))
        move_right_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)

        move_right_ccw(c_upper,c_lower,c_front, c_back, c_left,c_right)
        next_states.append(((c_upper[:],c_lower[:],c_front[:], c_back[:], c_left[:],c_right[:]), path + "R'->",depth+1))
        move_right_cw (c_upper,c_lower,c_front, c_back, c_left,c_right)

        queue.extend(next_states)

    print("Solve Steps: " + str(solve_path))




# Begin global variables
upper = ['w','w','w','w']
lower = ['y','y','y','y']
front = ['b','b','b','b']
back  = ['g','g','g','g']
left  = ['r','r','r','r']
right = ['o','o','o','o']

move_right_cw(upper,lower,front,back,left,right)
move_upper_cw(upper,lower,front,back,left,right)
move_right_cw(upper,lower,front,back,left,right)
move_back_ccw(upper,lower,front,back,left,right)



max_depth = 4
solve_tree(upper,lower,front,back,left,right,max_depth)


