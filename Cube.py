# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import random
import time

# Display()
# Function: Called statically and will return a String of the layout of the cube
# Need to: Update to use images and not a text based display
# PRE: The variables holding the colors on each face of the cube must not be empty
# POST: None
# Return: A string with the current layout of the cube



# GUI class
class GUI:
    def __init__(self, master):
        # Create the main window
        self.master = master

        # Get Window Hieght and Width for Frame Sizing
        GUI_height = self.master.winfo_screenheight()*(1-0.16)
        GUI_width = self.master.winfo_screenwidth()

        # Create a frame for the entire left section
        left_frame = tk.Frame(master, bg="#DEDDDD", width=GUI_width*0.6, height=GUI_height)
        left_frame.pack(side="left", fill="both", expand=True, padx = (GUI_width//100, GUI_width//100//2), pady = GUI_height//100)
        left_frame.pack_propagate(False)
        
        # Create a frame for the display section
        display_frame = tk.Frame(left_frame, bg="#373737", width= 742, height=504)
        display_frame.pack(side="top",  padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        display_frame.pack_propagate(False)

        # Create a canvas for the display, pack with cube
        self.canvas_cube = Canvas(display_frame, bg = '#939393', width= 742, height=500,highlightthickness=0)
        self.canvas_cube.pack(expand=True, padx = 5, pady = 5)

        # Create a default background
        background_cube_image = Image.open(os.getcwd() + '/Assets/Images/cube_background.png')
        background_cube_image = ImageTk.PhotoImage(background_cube_image)
        self.background_cube_image = background_cube_image
        self.canvas_cube.create_image(371,250,image=background_cube_image,anchor='center')

        # upper0_image = Image.open(os.getcwd() + '/Assets/Images/upper0_white.png')
        upper0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/upper0_white.png'))
        self.upper0_image_id = self.canvas_cube.create_image(371, 95, image=upper0_image, anchor='center')

        # upper1_image = Image.open(os.getcwd() + '/Assets/Images/upper1_white.png')
        upper1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/upper1_white.png'))
        self.upper1_image_id = self.canvas_cube.create_image(459, 141, image=upper1_image, anchor='center')

        upper2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/upper2_white.png'))
        self.upper2_image_id = self.canvas_cube.create_image(284, 140, image=upper2_image, anchor='center')

        upper3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/upper3_white.png'))
        self.upper3_image_id = self.canvas_cube.create_image(372, 185, image=upper3_image, anchor='center')

        right0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/right0_red.png'))
        self.right0_image_id = self.canvas_cube.create_image(427, 276, image=right0_image, anchor='center')

        right1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/right1_red.png'))
        self.right1_image_id = self.canvas_cube.create_image(528, 231, image=right1_image, anchor='center')

        right2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/right2_red.png'))
        self.right2_image_id = self.canvas_cube.create_image(427, 373, image=right2_image, anchor='center')

        right3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/right3_red.png'))
        self.right3_image_id = self.canvas_cube.create_image(528, 328, image=right3_image, anchor='center')

        front0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/front0_blue.png'))
        self.front0_image_id = self.canvas_cube.create_image(215, 231, image=front0_image, anchor='center')

        front1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/front1_blue.png'))
        self.front1_image_id = self.canvas_cube.create_image(315, 276, image=front1_image, anchor='center')

        front2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/front2_blue.png'))
        self.front2_image_id = self.canvas_cube.create_image(215, 328, image=front2_image, anchor='center')

        front3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/front3_blue.png'))
        self.front3_image_id = self.canvas_cube.create_image(315, 373, image=front3_image, anchor='center')
        GUI.Display(self)


        # Create a frame for the movement buttons section
        movement_buttons_frame = tk.Frame(left_frame, bg="#888888", width= 0.95*(GUI_width // 2), height=0.2*GUI_height)
        movement_buttons_frame.pack(side="bottom", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        movement_buttons_frame.pack_propagate(False)


        move_left_cw_button = tk.Button(movement_buttons_frame,text="Left CW",command = self.move_left_cw_button_command,width=8)
        move_left_cw_button.grid(row=0,column=1,sticky="nsew")
        move_left_ccw_button = tk.Button(movement_buttons_frame,text="Left CC",command = self.move_left_ccw_button_command,width=8)
        move_left_ccw_button.grid(row=1,column=1,sticky="nsew")
        move_front_cw_button = tk.Button(movement_buttons_frame,text="Front CW",command = self.move_front_cw_button_command,width=8)
        move_front_cw_button.grid(row=0,column=0,sticky="nsew")
        move_front_ccw_button = tk.Button(movement_buttons_frame,text="Front CC",command = self.move_front_ccw_button_command,width=8)
        move_front_ccw_button.grid(row=1,column=0,sticky="nsew")

        move_upper_cw_button = tk.Button(movement_buttons_frame,text="Upper CW",command = self.move_upper_cw_button_command,width=8)
        move_upper_cw_button.grid(row=0,column=2,sticky="nsew")
        move_upper_ccw_button = tk.Button(movement_buttons_frame,text="Upper CC",command = self.move_upper_ccw_button_command,width=8)
        move_upper_ccw_button.grid(row=0,column=3,sticky="nsew")

        move_lower_cw_button = tk.Button(movement_buttons_frame,text="Lower CW",command = self.move_lower_cw_button_command,width=8)
        move_lower_cw_button.grid(row=1,column=2,sticky="nsew")
        move_lower_ccw_button = tk.Button(movement_buttons_frame,text="Lower CC",command = self.move_lower_ccw_button_command,width=8)
        move_lower_ccw_button.grid(row=1,column=3,sticky="nsew")

        move_back_cw_button = tk.Button(movement_buttons_frame,text="Back CW",command = self.move_back_cw_button_command,width=8)
        move_back_cw_button.grid(row=0,column=5,sticky="nsew")
        move_back_ccw_button = tk.Button(movement_buttons_frame,text="Back CC",command = self.move_back_ccw_button_command,width=8)
        move_back_ccw_button.grid(row=1,column=5,sticky="nsew")

        move_right_cw_button = tk.Button(movement_buttons_frame,text="Right CW",command = self.move_right_cw_button_command,width=8)
        move_right_cw_button.grid(row=0,column=4,sticky="nsew")
        move_right_ccw_button = tk.Button(movement_buttons_frame,text="Right CC",command = self.move_right_ccw_button_command,width=8)
        move_right_ccw_button.grid(row=1,column=4,sticky="nsew")

        # Configure grid options to make buttons fill frame
        for i in range(6):  # Assuming 6 columns
            movement_buttons_frame.grid_columnconfigure(i, weight=1)

        for j in range(2):  # Assuming 2 rows
            movement_buttons_frame.grid_rowconfigure(j, weight=1)

        # Create a frame for the entire right section
        right_frame = tk.Frame(master, bg="#DEDDDD", width=GUI_width*0.4, height=GUI_height)
        right_frame.pack(side="right", fill="both", expand=True, padx = (0.005*GUI_width, 0.01*GUI_width), pady = 0.01*GUI_height)
        right_frame.pack_propagate(False)

        # Create a frame for the top right window
        mini_display_frame = tk.Frame(right_frame, bg="#616161", width=0.35*GUI_width, height=(GUI_height*0.4))
        mini_display_frame.pack(side="top", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        mini_display_frame.pack_propagate(False)

        # Create a frame for the top right window - buttons
        mini_display_buttons_frame = tk.Frame(mini_display_frame, bg="#000000", width=GUI_width*0.4, height=0.15*GUI_height*0.3)
        mini_display_buttons_frame.pack(side="top", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)

        # Create the shuffle and solve buttons
        shuffle_button = tk.Button(mini_display_frame,text="Shuffle",command = self.shuffle_button_command,height=2,width=21)
        shuffle_button.pack(side='left', fill="both", expand=True)        
        solve_button =   tk.Button(mini_display_frame,text="Solve"  ,command = Solve_Tree.set,height=2,width=21)
        solve_button.pack(side='left', fill="both", expand=True)

        # Create a frame for the bottom right window
        next_step_frame_outer = tk.Frame(right_frame, bg="#AAAAAA", width=GUI_width*0.4, height=GUI_height*0.4)
        next_step_frame_outer.pack(side="top", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        next_step_frame_inner = tk.Frame(next_step_frame_outer, bg="#FFFFFF", width=GUI_width*0.4, height=GUI_height*0.4)
        next_step_frame_inner.pack(side="top", fill="both", expand=True, padx = 0.02*0.99*(GUI_width // 4), pady = 0.02*0.99*(GUI_height*0.3))

        # Create a frame for the next and back steps
        next_step_button_frame = tk.Frame(next_step_frame_inner, bg="#000000", width=GUI_width*0.4, height=0.15*GUI_height*0.3)
        next_step_button_frame.pack(side="bottom", fill="x", padx=0,pady=0)

        # Create the next and back buttons
        back_button = tk.Button(next_step_button_frame,text="Back",command = print("test back"),height=2,width=21)
        back_button.pack(side="left")   
        next_button = tk.Button(next_step_button_frame,text="Next",command = print("test next"),height=2,width=21)
        next_button.pack(side="left")

        # 
        self.next_step_label = tk.Label(next_step_frame_inner,text = "Placeholder",font=("Courier", 20),justify='left')
        self.next_step_label.pack(anchor='nw')

    
    def Display(self):
        color_dict = {'w' : 'white',
                      'y' : 'yellow',
                      'r' : 'red',
                      'b' : 'blue',
                      'g' : 'green',
                      'o' : 'orange'}
        
        new_upper0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'upper0_' + color_dict[upper[0]] + '.png'))
        self.upper0_image = new_upper0_image
        self.canvas_cube.itemconfig(self.upper0_image_id, image=new_upper0_image)

        new_upper1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'upper1_' + color_dict[upper[1]] + '.png'))
        self.upper1_image = new_upper1_image
        self.canvas_cube.itemconfig(self.upper1_image_id, image=new_upper1_image)

        new_upper2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'upper2_' + color_dict[upper[2]] + '.png'))
        self.upper2_image = new_upper2_image
        self.canvas_cube.itemconfig(self.upper2_image_id, image=new_upper2_image)

        new_upper3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'upper3_' + color_dict[upper[3]] + '.png'))
        self.upper3_image = new_upper3_image
        self.canvas_cube.itemconfig(self.upper3_image_id, image=new_upper3_image)
        
        new_right0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'right0_' + color_dict[right[0]] + '.png'))
        self.right0_image = new_right0_image
        self.canvas_cube.itemconfig(self.right0_image_id, image=new_right0_image)

        new_right1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'right1_' + color_dict[right[1]] + '.png'))
        self.right1_image = new_right1_image
        self.canvas_cube.itemconfig(self.right1_image_id, image=new_right1_image)

        new_right2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'right2_' + color_dict[right[2]] + '.png'))
        self.right2_image = new_right2_image
        self.canvas_cube.itemconfig(self.right2_image_id, image=new_right2_image)

        new_right3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'right3_' + color_dict[right[3]] + '.png'))
        self.right3_image = new_right3_image
        self.canvas_cube.itemconfig(self.right3_image_id, image=new_right3_image)
        
        new_front0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'front0_' + color_dict[front[0]] + '.png'))
        self.front0_image = new_front0_image
        self.canvas_cube.itemconfig(self.front0_image_id, image=new_front0_image)

        new_front1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'front1_' + color_dict[front[1]] + '.png'))
        self.front1_image = new_front1_image
        self.canvas_cube.itemconfig(self.front1_image_id, image=new_front1_image)

        new_front2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'front2_' + color_dict[front[2]] + '.png'))
        self.front2_image = new_front2_image
        self.canvas_cube.itemconfig(self.front2_image_id, image=new_front2_image)

        new_front3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/' + 'front3_' + color_dict[front[3]] + '.png'))
        self.front3_image = new_front3_image
        self.canvas_cube.itemconfig(self.front3_image_id, image=new_front3_image)

    def move_upper_cw_button_command(self):
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
        self.Display()
                  
    def move_upper_ccw_button_command(self):
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
        self.Display()
        
    def move_lower_cw_button_command(self):
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
        self.Display()
        
    def move_lower_ccw_button_command(self):
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
        self.Display()
        
    def move_front_cw_button_command(self):
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
        self.Display()
        
    def move_front_ccw_button_command(self):
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
        self.Display()
        
    def move_back_cw_button_command(self):
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
        self.Display()
        
    def move_back_ccw_button_command(self):
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
        self.Display()
        
    def move_left_cw_button_command(self):
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
        self.Display()
        
    def move_left_ccw_button_command(self):
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
        self.Display()
        
    def move_right_cw_button_command(self):
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
        self.Display()
        
    def move_right_ccw_button_command(self):
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
        self.Display()

    def shuffle_button_command(self):
        i = random.randint(10,20)
        for i in range(1,i):
            m = random.randint(1,12)
            if (m ==  1): self.move_front_cw_button_command()
            if (m ==  2): self.move_front_ccw_button_command()
            if (m ==  3): self.move_upper_cw_button_command()
            if (m ==  4): self.move_upper_ccw_button_command()
            if (m ==  5): self.move_left_cw_button_command()
            if (m ==  6): self.move_left_ccw_button_command()
            if (m ==  7): self.move_right_cw_button_command()
            if (m ==  8): self.move_right_ccw_button_command()
            if (m ==  9): self.move_lower_cw_button_command()
            if (m == 10): self.move_lower_ccw_button_command()
            if (m == 11): self.move_back_cw_button_command()
            if (m == 12): self.move_back_ccw_button_command()
            

# Solve class
class Solve_Tree:
    def set():
        tree_upper = [upper[0],upper[1],upper[2],upper[3]]
        tree_lower = [lower[0],lower[1],lower[2],lower[3]]
        tree_front = [front[0],front[1],front[2],front[3]]
        tree_back  = [ back[0], back[1], back[2], back[3]]
        tree_left  = [ left[0], left[1], left[2], left[3]]
        tree_right = [right[0],right[1],right[2],right[3]]

        path = ''
        depth = 1
        last_move = ''
        move_list = ['move_tree_upper_cw',
                     'move_tree_upper_ccw',
                     'move_tree_lower_cw',
                     'move_tree_lower_ccw',
                     'move_tree_front_cw',
                     'move_tree_front_ccw',
                     'move_tree_back_cw',
                     'move_tree_back_ccw',
                     'move_tree_left_cw',
                     'move_tree_left_ccw',
                     'move_tree_right_cw',
                     'move_tree_right_ccw']
        Solve_Tree.solve_step()

    def solve_step(depth, path, last_move,consecutive_count):
        if(depth == 3):
            return("TEST_EXIT_3")
        if(Solve_Tree.check_solved()):
            return(path)
        for move in set.move_list:
            if move != last_move:
                print()
        
        

    def check_solved():
        if(tree_upper == ['w','w','w','w']):
            if(tree_front == ['b','b','b','b']):
                if(tree_right == ['r','r','r','r']):
                    if(tree_lower == ['y','y','y','y']):
                        if(tree_back == ['o','o','o','o']):
                            if(tree_left == ['g','g','g','g']):
                                return(TRUE)
                            else:
                                return(FALSE)
                        else:
                            return(FALSE)
                    else:
                        return(FALSE)
                else:
                    return(FALSE)
            else:
                return(FALSE)
        else:
            return(FALSE)

    def make_move(in_move):
        if  (in_move == 'move_tree_upper_cw'):
            Solve_Tree.move_tree_upper_cw()
        elif(in_move == 'move_tree_upper_ccw'):
            Solve_Tree.move_tree_upper_ccw()
        elif  (in_move == 'move_tree_lower_cw'):
            Solve_Tree.move_tree_lower_cw()
        elif(in_move == 'move_tree_lower_ccw'):
            Solve_Tree.move_tree_lower_ccw()
        elif  (in_move == 'move_tree_front_cw'):
            Solve_Tree.move_tree_front_cw()
        elif(in_move == 'move_tree_front_ccw'):
            Solve_Tree.move_tree_front_ccw()
        elif  (in_move == 'move_tree_back_cw'):
            Solve_Tree.move_tree_back_cw()
        elif(in_move == 'move_tree_back_ccw'):
            Solve_Tree.move_tree_back_ccw()
        elif  (in_move == 'move_tree_left_cw'):
            Solve_Tree.move_tree_left_cw()
        elif(in_move == 'move_tree_left_ccw'):
            Solve_Tree.move_tree_left_ccw()
        elif  (in_move == 'move_tree_right_cw'):
            Solve_Tree.move_tree_right_cw()
        elif(in_move == 'move_tree_right_ccw'):
            Solve_Tree.move_tree_right_ccw()


    def move_tree_upper_cw():
        temp = tree_front[0]
        temp2 = tree_front[1]
        tree_front[0] = tree_right[0]
        tree_front[1] = tree_right[1]
        tree_right[0] = tree_back[0]
        tree_right[1] = tree_back[1]
        tree_back[0] = tree_left[0]
        tree_back[1] = tree_left[1]
        tree_left[0] = temp
        tree_left[1] = temp2

        temp3 = tree_upper[0]
        tree_upper[0] = tree_upper[2]
        tree_upper[2] = tree_upper[3]
        tree_upper[3] = tree_upper[1]
        tree_upper[1] = temp3
                    
    def move_tree_upper_ccw():
        temp = tree_front[0]
        temp2 = tree_front[1]
        tree_front[0] = tree_left[0]
        tree_front[1] = tree_left[1]
        tree_left[0] = tree_back[0]
        tree_left[1] = tree_back[1]
        tree_back[0] = tree_right[0]
        tree_back[1] = tree_right[1]
        tree_right[0] = temp
        tree_right[1] = temp2

        temp3 = tree_upper[0]
        tree_upper[0] = tree_upper[1]
        tree_upper[1] = tree_upper[3]
        tree_upper[3] = tree_upper[2]
        tree_upper[2] = temp3
        
    def move_tree_lower_cw():
        temp = tree_front[2]
        temp2 = tree_front[3]
        tree_front[2] = tree_left[2]
        tree_front[3] = tree_left[3]
        tree_left[2] = tree_back[2] 
        tree_left[3] = tree_back[3]
        tree_back[2] = tree_right[2]
        tree_back[3] = tree_right[3]
        tree_right[2] = temp
        tree_right[3] = temp2

        temp3 = tree_lower[0]
        tree_lower[0] = tree_lower[2]
        tree_lower[2] = tree_lower[3]
        tree_lower[3] = tree_lower[1]
        tree_lower[1] = temp3
        
    def move_tree_lower_ccw():
        temp = tree_front[2]
        temp2 = tree_front[3]
        tree_front[2] = tree_right[2]
        tree_front[3] = tree_right[3]
        tree_right[2] = tree_back[2]
        tree_right[3] = tree_back[3]
        tree_back[2] = tree_left[2]
        tree_back[3] = tree_left[3]
        tree_left[2] = temp
        tree_left[3] = temp2

        temp3 = tree_lower[0]
        tree_lower[0] = tree_lower[1]
        tree_lower[1] = tree_lower[3]
        tree_lower[3] = tree_lower[2]
        tree_lower[2] = temp3
        
    def move_tree_front_cw():
        temp = tree_upper[2]
        temp2 = tree_upper[3]
        tree_upper[2] = tree_left[3]
        tree_upper[3] = tree_left[1]
        tree_left[3] = tree_lower[1]
        tree_left[1] = tree_lower[0]
        tree_lower[0] = tree_right[2]
        tree_lower[1] = tree_right[0]
        tree_right[2] = temp2
        tree_right[0] = temp
        temp3 = tree_front[0]
        tree_front[0] = tree_front[2]
        tree_front[2] = tree_front[3]
        tree_front[3] = tree_front[1]
        tree_front[1] = temp3
        
    def move_tree_front_ccw():
        temp = tree_upper[2]
        temp2 = tree_upper[3]
        tree_upper[2] = tree_right[0]
        tree_upper[3] = tree_right[2]
        tree_right[0] = tree_lower[1]
        tree_right[2] = tree_lower[0]
        tree_lower[1] = tree_left[3]
        tree_lower[0] = tree_left[1]
        tree_left[3] = temp
        tree_left[1] = temp2

        temp3 = tree_front[0]
        tree_front[0] = tree_front[1]
        tree_front[1] = tree_front[3]
        tree_front[3] = tree_front[2]
        tree_front[2] = temp3
        
    def move_tree_back_cw():
        temp = tree_upper[0]
        temp2 = tree_upper[1]
        tree_upper[0] = tree_right[1]
        tree_upper[1] = tree_right[3]
        tree_right[1] = tree_lower[3]
        tree_right[3] = tree_lower[2]
        tree_lower[3] = tree_left[2]
        tree_lower[2] = tree_left[0]
        tree_left[2] = temp
        tree_left[0] = temp2

        temp3 = tree_back[0]
        tree_back[0] = tree_back[2]
        tree_back[2] = tree_back[3]
        tree_back[3] = tree_back[1]
        tree_back[1] = temp3
        
    def move_tree_back_ccw():
        temp = tree_upper[0]
        temp2 = tree_upper[1]
        tree_upper[0] = tree_left[2]
        tree_upper[1] = tree_left[0]
        tree_left[2] = tree_lower[3]
        tree_left[0] = tree_lower[2]
        tree_lower[3] = tree_right[1]
        tree_lower[2] = tree_right[3]
        tree_right[1] = temp
        tree_right[3] = temp2

        temp3 = tree_back[0]
        tree_back[0] = tree_back[1]
        tree_back[1] = tree_back[3]
        tree_back[3] = tree_back[2]
        tree_back[2] = temp3
        
    def move_tree_left_cw():
        temp = tree_upper[0]
        temp2 = tree_upper[2]
        tree_upper[0] = tree_back[3]
        tree_upper[2] = tree_back[1]
        tree_back[3] = tree_lower[0]
        tree_back[1] = tree_lower[2]
        tree_lower[0] = tree_front[0]
        tree_lower[2] = tree_front[2]
        tree_front[0] = temp
        tree_front[2] = temp2

        temp3 = tree_left[0]
        tree_left[0] = tree_left[2]
        tree_left[2] = tree_left[3]
        tree_left[3] = tree_left[1]
        tree_left[1] = temp3
        
    def move_tree_left_ccw():
        temp = tree_upper[0]
        temp2 = tree_upper[2]
        tree_upper[0] = tree_front[0]
        tree_upper[2] = tree_front[2]
        tree_front[0] = tree_lower[0]
        tree_front[2] = tree_lower[2]
        tree_lower[0] = tree_back[3]
        tree_lower[2] = tree_back[1]
        tree_back[3] = temp
        tree_back[1] = temp2

        temp3 = tree_left[0]
        tree_left[0] = tree_left[1]
        tree_left[1] = tree_left[3]
        tree_left[3] = tree_left[2]
        tree_left[2] = temp3
        
    def move_tree_right_cw():
        temp = tree_upper[1]
        temp2 = tree_upper[3]
        tree_upper[1] = tree_front[1]
        tree_upper[3] = tree_front[3]
        tree_front[1] = tree_lower[1]
        tree_front[3] = tree_lower[3]
        tree_lower[1] = tree_back[2]
        tree_lower[3] = tree_back[0]
        tree_back[2] = temp
        tree_back[0] = temp2

        temp3 = tree_right[0]
        tree_right[0] = tree_right[2]
        tree_right[2] = tree_right[3]
        tree_right[3] = tree_right[1]
        tree_right[1] = temp3
        
    def move_tree_right_ccw():
        temp = tree_upper[1]
        temp2 = tree_upper[3]
        tree_upper[1] = tree_back[2]
        tree_upper[3] = tree_back[0]
        tree_back[2] = tree_lower[1]
        tree_back[0] = tree_lower[3]
        tree_lower[1] = tree_front[1]
        tree_lower[3] = tree_front[3]
        tree_front[1] = temp
        tree_front[3] = temp2

        temp3 = right[0]
        tree_right[0] = tree_right[1]
        tree_right[1] = tree_right[3]
        tree_right[3] = tree_right[2]
        tree_right[2] = temp3

    def Solve_White_1():
        if((back[0]  == 'w') & (upper[1] == 'b') & (right[1] == 'o')): next = "Right C-Clockwise"
        if((front[3] == 'w') & (right[2] == 'o') & (lower[1] == 'b')): next = "Right Clockwise"
        if((right[3] == 'o') & (lower[3] == 'w') & (back[2]  == 'b')): next = "Right Clockwise"
        if((upper[0] == 'o') & (left[0]  == 'b') & (back[1]  == 'w')): next = "Back C-Clockwise"
        if((front[2] == 'o') & (left[3]  == 'w') & (lower[0] == 'b')): next = "Lower Clockwise"
        if((right[3] == 'w') & (lower[3] == 'b') & (back[2]  == 'o')): next = "Lower C-Clockwise"
        if((back[3]  == 'w') & (lower[2] == 'b') & (left[2]  == 'o')): next = "Lower Clockwise"
        if((back[3]  == 'o') & (lower[2] == 'w') & (left[2]  == 'b')): next = "Lower C-Clockwise"
        if((back[0]  == 'b') & (upper[1] == 'o') & (right[1] == 'w')): next = "Right Clockwise"
        if((front[3] == 'b') & (right[2] == 'w') & (lower[1] == 'o')): next = "Right C-Clockwise"
        if((front[3] == 'o') & (right[2] == 'b') & (lower[1] == 'w')): next = "Lower Clockwise"
        if((front[1] == 'w') & (upper[3] == 'o') & (right[0] == 'b')): next = "Right C-Clockwise"
        if((front[1] == 'o') & (upper[3] == 'b') & (right[0] == 'w')): next = "Right Clockwise"
        if((back[0]  == 'o') & (upper[1] == 'w') & (right[1] == 'b')): next = "Upper Clockwise"
        if((upper[0] == 'w') & (left[0]  == 'o') & (back[1]  == 'b')): next = "Back Clockwise"
        if((front[2] == 'b') & (left[3]  == 'o') & (lower[0] == 'w')): next = "Lower Clockwise"
        if((front[2] == 'w') & (left[3]  == 'b') & (lower[0] == 'o')): next = "Lower Clockwise"
        if((right[3] == 'b') & (lower[3] == 'o') & (back[2]  == 'w')): next = "Right Clockwise"
        if((upper[0] == 'b') & (left[0]  == 'w') & (back[1]  == 'o')): next = "Upper Clockwise"
        if((back[3]  == 'b') & (lower[2] == 'o') & (left[2]  == 'w')): next = "Lower Clockwise"
        else: next = ""
        # main.GUI.next_step_label.config(text = next)


                        



    

# Start the GUI
def main():
    root = tk.Tk()
    Width, Height = root.winfo_screenwidth(), root.winfo_screenheight()
    ToolBarHeight = 0.16*Height
    Height = Height - ToolBarHeight
    root.configure(background='#4C4C4C')
    root.geometry('%dx%d+0+0' % (Width,Height))
    root.title("Rubik's Cube Solver")

    app = GUI(root)
    root.mainloop()


# Begin global variables
upper = ['w','w','w','w']
lower = ['y','y','y','y']
front = ['b','b','b','b']
back  = ['g','g','g','g']
left  = ['r','r','r','r']
right = ['o','o','o','o']

tree_upper = [upper[0],upper[1],upper[2],upper[3]]
tree_lower = [lower[0],lower[1],lower[2],lower[3]]
tree_front = [front[0],front[1],front[2],front[3]]
tree_back  = [ back[0], back[1], back[2], back[3]]
tree_left  = [ left[0], left[1], left[2], left[3]]
tree_right = [right[0],right[1],right[2],right[3]]





if __name__ == "__main__":
    main()