# Import Libraries
import tkinter as tk
from tkinter import Tk, Frame
from PIL import ImageTk, Image
import os

# Display()
# Function: Called statically and will return a String of the layout of the cube
# Need to: Update to use images and not a text based display
# PRE: The variables holding the colors on each face of the cube must not be empty
# Return: A string with the current layout of the cube
def Display():
    text = ""
    text += "\n          __ __\n         |"
    if (upper[0] == 'b'): text += "bl" 
    elif(upper[0] == 'g'): text += "gr" 
    elif(upper[0] == 'r'): text += "rd" 
    elif(upper[0] == 'w'): text += "wh" 
    elif(upper[0] == 'o'): text += "or" 
    elif(upper[0] == 'y'): text += "yl" 
    text += "|"
    if (upper[1] == 'b'): text += "bl" 
    elif(upper[1] == 'g'): text += "gr" 
    elif(upper[1] == 'r'): text += "rd" 
    elif(upper[1] == 'w'): text += "wh" 
    elif(upper[1] == 'o'): text += "or" 
    elif(upper[1] == 'y'): text += "yl" 
    text += "|\n         |__|__|\n         |"
    if (upper[2] == 'b'): text += "bl" 
    elif(upper[2] == 'g'): text += "gr" 
    elif(upper[2] == 'r'): text += "rd" 
    elif(upper[2] == 'w'): text += "wh" 
    elif(upper[2] == 'o'): text += "or" 
    elif(upper[2] == 'y'): text += "yl" 
    text += "|"
    if (upper[3] == 'b'): text += "bl" 
    elif(upper[3] == 'g'): text += "gr" 
    elif(upper[3] == 'r'): text += "rd" 
    elif(upper[3] == 'w'): text += "wh" 
    elif(upper[3] == 'o'): text += "or" 
    elif(upper[3] == 'y'): text += "yl" 
    text += "|\n         |__|__|\n  __ __   __ __   __ __   __ __        \n |"
    if ( left[0] == 'b'): text += "bl" 
    elif( left[0] == 'g'): text += "gr" 
    elif( left[0] == 'r'): text += "rd" 
    elif( left[0] == 'w'): text += "wh" 
    elif( left[0] == 'o'): text += "or" 
    elif( left[0] == 'y'): text += "yl" 
    text += "|"
    if ( left[1] == 'b'): text += "bl" 
    elif( left[1] == 'g'): text += "gr" 
    elif( left[1] == 'r'): text += "rd" 
    elif( left[1] == 'w'): text += "wh" 
    elif( left[1] == 'o'): text += "or" 
    elif( left[1] == 'y'): text += "yl" 
    text += "| |"
    if (front[0] == 'b'): text += "bl" 
    elif(front[0] == 'g'): text += "gr" 
    elif(front[0] == 'r'): text += "rd" 
    elif(front[0] == 'w'): text += "wh" 
    elif(front[0] == 'o'): text += "or" 
    elif(front[0] == 'y'): text += "yl" 
    text += "|"
    if (front[1] == 'b'): text += "bl" 
    elif(front[1] == 'g'): text += "gr" 
    elif(front[1] == 'r'): text += "rd" 
    elif(front[1] == 'w'): text += "wh" 
    elif(front[1] == 'o'): text += "or" 
    elif(front[1] == 'y'): text += "yl" 
    text += "| |"
    if (right[0] == 'b'): text += "bl" 
    elif(right[0] == 'g'): text += "gr" 
    elif(right[0] == 'r'): text += "rd" 
    elif(right[0] == 'w'): text += "wh" 
    elif(right[0] == 'o'): text += "or" 
    elif(right[0] == 'y'): text += "yl" 
    text += "|"
    if (right[1] == 'b'): text += "bl" 
    elif(right[1] == 'g'): text += "gr" 
    elif(right[1] == 'r'): text += "rd" 
    elif(right[1] == 'w'): text += "wh" 
    elif(right[1] == 'o'): text += "or" 
    elif(right[1] == 'y'): text += "yl" 
    text += "| |"
    if ( back[0] == 'b'): text += "bl" 
    elif( back[0] == 'g'): text += "gr" 
    elif( back[0] == 'r'): text += "rd" 
    elif( back[0] == 'w'): text += "wh" 
    elif( back[0] == 'o'): text += "or" 
    elif( back[0] == 'y'): text += "yl" 
    text += "|"
    if ( back[1] == 'b'): text += "bl" 
    elif( back[1] == 'g'): text += "gr" 
    elif( back[1] == 'r'): text += "rd" 
    elif( back[1] == 'w'): text += "wh" 
    elif( back[1] == 'o'): text += "or" 
    elif( back[1] == 'y'): text += "yl" 
    text += "|\n |__|__| |__|__| |__|__| |__|__|\n |"
    if ( left[2] == 'b'): text += "bl" 
    elif( left[2] == 'g'): text += "gr" 
    elif( left[2] == 'r'): text += "rd" 
    elif( left[2] == 'w'): text += "wh" 
    elif( left[2] == 'o'): text += "or" 
    elif( left[2] == 'y'): text += "yl" 
    text += "|"
    if ( left[3] == 'b'): text += "bl" 
    elif( left[3] == 'g'): text += "gr" 
    elif( left[3] == 'r'): text += "rd" 
    elif( left[3] == 'w'): text += "wh" 
    elif( left[3] == 'o'): text += "or" 
    elif( left[3] == 'y'): text += "yl" 
    text += "| |"
    if (front[2] == 'b'): text += "bl" 
    elif(front[2] == 'g'): text += "gr" 
    elif(front[2] == 'r'): text += "rd" 
    elif(front[2] == 'w'): text += "wh" 
    elif(front[2] == 'o'): text += "or" 
    elif(front[2] == 'y'): text += "yl" 
    text += "|"
    if (front[3] == 'b'): text += "bl" 
    elif(front[3] == 'g'): text += "gr" 
    elif(front[3] == 'r'): text += "rd" 
    elif(front[3] == 'w'): text += "wh" 
    elif(front[3] == 'o'): text += "or" 
    elif(front[3] == 'y'): text += "yl" 
    text += "| |"
    if (right[2] == 'b'): text += "bl" 
    elif(right[2] == 'g'): text += "gr" 
    elif(right[2] == 'r'): text += "rd" 
    elif(right[2] == 'w'): text += "wh" 
    elif(right[2] == 'o'): text += "or" 
    elif(right[2] == 'y'): text += "yl" 
    text += "|"
    if (right[3] == 'b'): text += "bl" 
    elif(right[3] == 'g'): text += "gr" 
    elif(right[3] == 'r'): text += "rd" 
    elif(right[3] == 'w'): text += "wh" 
    elif(right[3] == 'o'): text += "or" 
    elif(right[3] == 'y'): text += "yl" 
    text += "| |"
    if ( back[2] == 'b'): text += "bl" 
    elif( back[2] == 'g'): text += "gr" 
    elif( back[2] == 'r'): text += "rd" 
    elif( back[2] == 'w'): text += "wh" 
    elif( back[2] == 'o'): text += "or" 
    elif( back[2] == 'y'): text += "yl" 
    text += "|"
    if ( back[3] == 'b'): text += "bl" 
    elif( back[3] == 'g'): text += "gr" 
    elif( back[3] == 'r'): text += "rd" 
    elif( back[3] == 'w'): text += "wh" 
    elif( back[3] == 'o'): text += "or" 
    elif( back[3] == 'y'): text += "yl" 
    text += "|\n |__|__| |__|__| |__|__| |__|__|\n          __ __\n         |"
    if (lower[0] == 'b'): text += "bl" 
    elif(lower[0] == 'g'): text += "gr" 
    elif(lower[0] == 'r'): text += "rd" 
    elif(lower[0] == 'w'): text += "wh" 
    elif(lower[0] == 'o'): text += "or" 
    elif(lower[0] == 'y'): text += "yl" 
    text += "|"
    if (lower[1] == 'b'): text += "bl" 
    elif(lower[1] == 'g'): text += "gr" 
    elif(lower[1] == 'r'): text += "rd" 
    elif(lower[1] == 'w'): text += "wh" 
    elif(lower[1] == 'o'): text += "or" 
    elif(lower[1] == 'y'): text += "yl" 
    text += "|\n         |__|__|\n         |"
    if (lower[2] == 'b'): text += "bl" 
    elif(lower[2] == 'g'): text += "gr" 
    elif(lower[2] == 'r'): text += "rd" 
    elif(lower[2] == 'w'): text += "wh" 
    elif(lower[2] == 'o'): text += "or" 
    elif(lower[2] == 'y'): text += "yl" 
    text += "|"
    if (lower[3] == 'b'): text += "bl" 
    elif(lower[3] == 'g'): text += "gr" 
    elif(lower[3] == 'r'): text += "rd" 
    elif(lower[3] == 'w'): text += "wh" 
    elif(lower[3] == 'o'): text += "or" 
    elif(lower[3] == 'y'): text += "yl" 
    text += "|\n         |__|__|\n"
    text += ""
    print(text)
    return(text)

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
        display_frame = tk.Frame(left_frame, bg="#373737", width= 0.95*(GUI_width // 2), height=0.70*GUI_height)
        display_frame.pack(side="top", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        display_frame.pack_propagate(False)

        self.display_label = tk.Label(display_frame,
                                text = Display(),
                                font=("Courier", 20),
                                anchor='center',
                                justify='left',
                                fg='white',
                                bg='#000000')
        self.display_label.pack(anchor='center', expand=True, fill='both',padx=5,pady=5)

        # Create a frame for the movement buttons section
        movement_buttons_frame = tk.Frame(left_frame, bg="#888888", width= 0.95*(GUI_width // 2), height=0.2*GUI_height)
        movement_buttons_frame.pack(side="bottom", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        movement_buttons_frame.pack_propagate(False)

        move_upper_cw_button = tk.Button(movement_buttons_frame,text="Upper CW",command = self.move_upper_cw_button_command,width=8)
        move_upper_cw_button.grid(row=0,column=0,sticky="nsew")
        move_upper_ccw_button = tk.Button(movement_buttons_frame,text="Upper CC",command = self.move_upper_ccw_button_command,width=8)
        move_upper_ccw_button.grid(row=1,column=0,sticky="nsew")
        move_lower_cw_button = tk.Button(movement_buttons_frame,text="Lower CW",command = self.move_lower_cw_button_command,width=8)
        move_lower_cw_button.grid(row=0,column=1,sticky="nsew")
        move_lower_ccw_button = tk.Button(movement_buttons_frame,text="Lower CC",command = self.move_lower_ccw_button_command,width=8)
        move_lower_ccw_button.grid(row=1,column=1,sticky="nsew")
        move_front_cw_button = tk.Button(movement_buttons_frame,text="Front CW",command = self.move_front_cw_button_command,width=8)
        move_front_cw_button.grid(row=0,column=2,sticky="nsew")
        move_front_ccw_button = tk.Button(movement_buttons_frame,text="Front CC",command = self.move_front_ccw_button_command,width=8)
        move_front_ccw_button.grid(row=1,column=2,sticky="nsew")
        move_back_cw_button = tk.Button(movement_buttons_frame,text="Back CW",command = self.move_back_cw_button_command,width=8)
        move_back_cw_button.grid(row=0,column=3,sticky="nsew")
        move_back_ccw_button = tk.Button(movement_buttons_frame,text="Back CC",command = self.move_back_ccw_button_command,width=8)
        move_back_ccw_button.grid(row=1,column=3,sticky="nsew")
        move_left_cw_button = tk.Button(movement_buttons_frame,text="Left CW",command = self.move_left_cw_button_command,width=8)
        move_left_cw_button.grid(row=0,column=4,sticky="nsew")
        move_left_ccw_button = tk.Button(movement_buttons_frame,text="Left CC",command = self.move_left_ccw_button_command,width=8)
        move_left_ccw_button.grid(row=1,column=4,sticky="nsew") 
        move_right_cw_button = tk.Button(movement_buttons_frame,text="Right CW",command = self.move_right_cw_button_command,width=8)
        move_right_cw_button.grid(row=0,column=5,sticky="nsew")
        move_right_ccw_button = tk.Button(movement_buttons_frame,text="Right CC",command = self.move_right_ccw_button_command,width=8)
        move_right_ccw_button.grid(row=1,column=5,sticky="nsew")

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
        mini_display_frame = tk.Frame(right_frame, bg="#616161", width=GUI_width // 4, height=(GUI_height*0.7))
        mini_display_frame.pack(side="top", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        mini_display_frame.pack_propagate(False)

        # Create a frame for the bottom right window
        next_step_frame_outer = tk.Frame(right_frame, bg="#AAAAAA", width=GUI_width // 4, height=GUI_height*0.3)
        next_step_frame_outer.pack(side="bottom", fill="both", expand=True, padx = 0.01*GUI_width, pady = 0.01*GUI_height)
        next_step_frame_inner = tk.Frame(next_step_frame_outer, bg="#FFFFFF", width=0.99*(GUI_width // 4), height=0.99*(GUI_height*0.3))
        next_step_frame_inner.pack(side="bottom", fill="both", expand=True, padx = 0.02*0.99*(GUI_width // 4), pady = 0.02*0.99*(GUI_height*0.3))
        next_step_frame_inner.pack_propagate(False)
        next_step_label = tk.Label(next_step_frame_inner,text = "TODO: UPDATE NEXT STEP",font=("Courier", 20),justify='left')
        next_step_label.pack(anchor='nw')

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
        self.display_label.config(text=Display())
                  
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())
        
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
        self.display_label.config(text=Display())

# Cube class
class Solver:
    def Solve_White_1():
        print()

    print()


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
back  = ['o','o','o','o']
left  = ['g','g','g','g']
right = ['r','r','r','r']
print()

if __name__ == "__main__":
    main()