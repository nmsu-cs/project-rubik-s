import tkinter as tk
from tkinter import filedialog
import csv
def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    root = tk.Tk()
    root.title("File Menu Box Example")


def GetImport(filename):
    data = []
    with open()
