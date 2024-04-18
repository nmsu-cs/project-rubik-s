import tkinter as tk
from tkinter import filedialog
import csv
import os

def get():
    filename = filedialog.askopenfilename(initialdir=os.getcwd() + 'Assets/Cube_Sets/', title="Select file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    
    with open(filename, newline='\n') as csvfile:
        (upper_data,down_data,front_data,back_data,left_data,right_data) = list(csv.reader(csvfile))

    return(upper_data,down_data,front_data,back_data,left_data,right_data)

