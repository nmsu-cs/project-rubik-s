
import tkinter as tk
def submit_input(self):
    user_cube = self.entry.get()
    print(user_cube)

def get(self):
    self.user_input = tk.Toplevel(self.master)
    self.user_input.title("Enter a Rubik's Cube")


    ########################
    screen_width = self.user_input.winfo_screenwidth()
    screen_height = self.user_input.winfo_screenheight()

    # Calculate the position of the Toplevel window
    x = (screen_width - 300) // 2  # Center horizontally
    y = (screen_height - 150) // 2  # Center vertically

    # Set the position of the Toplevel window
    self.user_input.geometry("+{}+{}".format(x, y))
    ##########################



    self.user_input.geometry("700x400")
    
    self.label = tk.Label(self.user_input,text="Enter input: ")
    self.label.pack()

    self.entry = tk.Entry(self.user_input)
    self.entry.pack()

    self.submit_button = tk.Button(self.user_input,text="Submit",command = submit_input)
    self.submit_button.pack()
