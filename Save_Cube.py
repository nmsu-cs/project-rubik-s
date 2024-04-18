# Import Libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import random
import time
import csv


def save(upper,down,front,back,left,right):
    def submit_input():
        filename = entry.get()
        

        with open(os.getcwd() + '/Assets/Cube_Sets/' + filename + '.csv', 'w+') as file:
            save_data = ','.join(upper) + '\n' + ','.join(down) + '\n' + ','.join(front) + '\n' + ','.join(back) + '\n' + ','.join(left) + '\n' + ','.join(right) + '\n'
            file.write(save_data)
        user_input.destroy()
    
    user_input = tk.Toplevel()
    user_input.title("Save as CSV: ")
    user_input.geometry("300x100")

    label = tk.Label(user_input,text="Choose a file name: ")
    label.pack()

    entry = tk.Entry(user_input)
    entry.pack()

    submit_button = tk.Button(user_input,text="Submit",command = submit_input)
    submit_button.pack()