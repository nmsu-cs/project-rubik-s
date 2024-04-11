# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import random
import time


# Import other files
import Solver
import Display
import GetUserInput
# import ImportCube


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

        # Create a frame for the set cube command
        set_cube_button = tk.Button(self.canvas_cube,text="Set Cube",command = GUI.set_user_input_command)
        self.canvas_cube.create_window(0, 0, anchor='nw', window=set_cube_button)



        # GetUserInput.get(self)
        Display.display(self,upper,down,front,back,left,right)


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
        move_upper_ccw_button.grid(row=1,column=2,sticky="nsew")

        move_down_cw_button = tk.Button(movement_buttons_frame,text="Down CW",command = self.move_down_cw_button_command,width=8)
        move_down_cw_button.grid(row=0,column=3,sticky="nsew")
        move_down_ccw_button = tk.Button(movement_buttons_frame,text="Down CC",command = self.move_down_ccw_button_command,width=8)
        move_down_ccw_button.grid(row=1,column=3,sticky="nsew")

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
        solve_button =   tk.Button(mini_display_frame,text="Solve"  ,command = self.solve_button_command,height=2,width=21)
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

        # Create a label for next step
        self.next_step_label = tk.Label(next_step_frame_inner,text = "",font=("Courier", 14),justify='left')
        self.next_step_label.pack(anchor='nw')

    def set_user_input_command():
        (upper,down,front,back,left,right) = GetUserInput.get()
    
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
        Display.display(self,upper,down,front,back,left,right)
                  
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_down_cw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_down_ccw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_front_cw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_front_ccw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_back_cw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_back_ccw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_left_cw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_left_ccw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_right_cw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)
        
    def move_right_ccw_button_command(self):
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
        Display.display(self,upper,down,front,back,left,right)

    def shuffle_button_command(self):
        i = random.randint(10,20)
        i = 8
        for i in range(1,i+1):
            m = random.randint(1,12)
            if (m ==  1): self.move_front_cw_button_command()
            if (m ==  2): self.move_front_ccw_button_command()
            if (m ==  3): self.move_upper_cw_button_command()
            if (m ==  4): self.move_upper_ccw_button_command()
            if (m ==  5): self.move_left_cw_button_command()
            if (m ==  6): self.move_left_ccw_button_command()
            if (m ==  7): self.move_right_cw_button_command()
            if (m ==  8): self.move_right_ccw_button_command()
            if (m ==  9): self.move_down_cw_button_command()
            if (m == 10): self.move_down_ccw_button_command()
            if (m == 11): self.move_back_cw_button_command()
            if (m == 12): self.move_back_ccw_button_command()
            
    def solve_button_command(self):
        output = self.getNext()


        self.next_step_label.configure(text = output)


    def getNext(self):
        str = Solver.solve(upper,down,front,back,left,right)
        return(str)
    
    def stack2str(stack):
        out_string = ""
        while stack:
            out_string += stack.pop()
            if stack:
                out_string += ","
        return(out_string)

    

                 

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
down =  ['y','y','y','y']
front = ['b','b','b','b']
back  = ['g','g','g','g']
left  = ['r','r','r','r']
right = ['o','o','o','o']

# Cube 10 steps
# upper = ['w', 'b', 'r', 'y']
# down =  ['w', 'w', 'y', 'w']
# front = ['y', 'g', 'b', 'b'] 
# back =  ['o', 'g', 'o', 'r']
# left =  ['r', 'g', 'b', 'o'] 
# right = ['o', 'y', 'r', 'g']

if __name__ == "__main__":
    main()