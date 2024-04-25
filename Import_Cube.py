# Import_Cube.py
# Called from the GUI when Import Cube button is clicked


# Import Libraries
import tkinter as tk
from tkinter import filedialog
import csv

# Function: get
# Purpose: Retrieve the data in a csv file that contains a state of a cube
# Precondition: The desired csv file must exist, and should be present in the cube_sets folder
#             : The format of the input cube is specific
#               Note that the GUI has an option to save the current state into the required format
def get():
    # Open Folder with cube sets
    filename = filedialog.askopenfilename(initialdir='/Users/Alexamzi/Desktop/project-rubik-s/Assets/Cube_Sets/', title="Select file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    
    # Read the data from the csv into the arrays
    with open(filename, newline='\n') as csvfile:
        (upper_data,down_data,front_data,back_data,left_data,right_data) = list(csv.reader(csvfile))

    # Return the array data
    return(upper_data,down_data,front_data,back_data,left_data,right_data)

