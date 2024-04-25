# Save_Cube.py
# Called from the GUI when Save Cube button is clicked

# Import Libraries
import tkinter as tk
from tkinter import *
import os

# Function: save
# Purpose: Will export the state of the cube into a read-able csv file, can be imported later
#        : File name will be chosen by the user from a GUI
# Parameters: The arrays holding the state of the cube
# Precondition: The arrays holding the state of the cube must be defined
# Postcondition: A new file with the state of the cube
def save(upper,down,front,back,left,right):
    # Function submit_input
    # Helper to save function
    def submit_input():
        # Retrieve filename from text box
        filename = entry.get()
        
        # Create csv file in desired format
        with open(os.getcwd() + '/Assets/Cube_Sets/' + filename + '.csv', 'w+') as file:
            save_data = ','.join(upper) + '\n' + ','.join(down) + '\n' + ','.join(front) + '\n' + ','.join(back) + '\n' + ','.join(left) + '\n' + ','.join(right) + '\n'
            file.write(save_data)
        user_input.destroy()
    
    # Create a GUI window to retrieve the desired name of the file from the user input
    user_input = tk.Toplevel()
    user_input.title("Save as CSV: ")
    user_input.geometry("300x100")

    label = tk.Label(user_input,text="Choose a file name: ")
    label.pack()

    # Create a text box for the user to enter text
    entry = tk.Entry(user_input)
    entry.pack()

    # Create the "submit" button when user is done defining the filename
    submit_button = tk.Button(user_input,text="Submit",command = submit_input)
    submit_button.pack()