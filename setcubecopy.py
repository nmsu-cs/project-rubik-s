
import tkinter as tk
import os


def get(self):    
    color_dict = {  'w' : 'white',
                    'y' : 'yellow',
                    'r' : 'red',
                    'b' : 'blue',
                    'g' : 'green',
                    'o' : 'orange'} 
    

    upper = ['w','w','w','w']
    down =  ['y','y','y','y']
    front = ['b','b','b','b']
    back  = ['g','g','g','g']
    left  = ['r','r','r','r']
    right = ['o','o','o','o']

    global upper0ID
    global upper1ID
    global upper2ID
    global upper3ID
    global down0ID
    global down1ID
    global down2ID
    global down3ID
    global front0ID
    global front1ID
    global front2ID
    global front3ID
    global back0ID
    global back1ID
    global back2ID
    global back3ID
    global left0ID
    global left1ID
    global left2ID
    global left3ID
    global right0ID
    global right1ID
    global right2ID
    global right3ID

    upper0ID = 1
    upper1ID = 1
    upper2ID = 1
    upper3ID = 1
    down0ID = 2
    down1ID = 2
    down2ID = 2
    down3ID = 2
    front0ID = 3
    front1ID = 3
    front2ID = 3
    front3ID = 3
    back0ID = 4
    back1ID = 4
    back2ID = 4
    back3ID = 4
    left0ID = 5
    left1ID = 5
    left2ID = 5
    left3ID = 5
    right0ID = 6
    right1ID = 6
    right2ID = 6
    right3ID = 6

    self.user_input = tk.Toplevel(self.master,bg="#555555")
    self.user_input.title("Enter a Rubik's Cube")

    # Calculate the position of the Toplevel window
    x = (self.user_input.winfo_screenwidth() - 300) // 6  # Center horizontally
    y = (self.user_input.winfo_screenheight() - 150) // 6  # Center vertically

    # Set Format the size and position of the window
    self.user_input.geometry("+{}+{}".format(x, y))
    self.user_input.geometry("800x400")
    
    # Load all images
    upper0_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper0_'  + color_dict[upper[0]] + '.png'))
    upper1_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper1_'  + color_dict[upper[0]] + '.png'))
    upper2_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper2_'  + color_dict[upper[0]] + '.png'))
    upper3_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper3_'  + color_dict[upper[0]] + '.png'))
    down0_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'down0_'   + color_dict[down[0]]  + '.png'))
    down1_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'down1_'   + color_dict[down[0]]  + '.png'))
    down2_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'down2_'   + color_dict[down[0]]  + '.png'))
    down3_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'down3_'   + color_dict[down[0]]  + '.png'))
    front0_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'front0_'  + color_dict[front[0]] + '.png'))
    front1_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'front1_'  + color_dict[front[0]] + '.png'))
    front2_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'front2_'  + color_dict[front[0]] + '.png'))
    front3_image = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'front3_'  + color_dict[front[0]] + '.png'))
    back0_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'back0_'   + color_dict[back[0]]  + '.png'))
    back1_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'back1_'   + color_dict[back[0]]  + '.png'))
    back2_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'back2_'   + color_dict[back[0]]  + '.png'))
    back3_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'back3_'   + color_dict[back[0]]  + '.png'))
    left0_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'left0_'   + color_dict[left[0]]  + '.png'))
    left1_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'left1_'   + color_dict[left[0]]  + '.png'))
    left2_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'left2_'   + color_dict[left[0]]  + '.png'))
    left3_image  = tk.PhotoImage(file=(os.getcwd()  + '/Assets/Set_Images/set_' + 'left3_'   + color_dict[left[0]]  + '.png'))
    right0_image  = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_' + color_dict[right[0]]  + '.png'))
    right1_image  = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_' + color_dict[right[0]]  + '.png'))
    right2_image  = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_' + color_dict[right[0]]  + '.png'))
    right3_image  = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_' + color_dict[right[0]]  + '.png'))

    # Pack all buttons
    self.upper0_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:upper0_button_command(self.upper0_button,upper0_image))
    self.upper0_button.image = upper0_image
    self.upper0_button.config(image = upper0_image)
    self.upper0_button.grid(row=1, column=3, padx=1, pady=1)

    self.upper1_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:upper1_button_command(self.upper1_button,upper1_image))
    self.upper1_button.image = upper1_image
    self.upper1_button.config(image = upper1_image)
    self.upper1_button.grid(row=1, column=4, padx=1, pady=1)

    self.upper2_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:upper2_button_command(self.upper2_button,upper2_image))
    self.upper2_button.image = upper2_image
    self.upper2_button.config(image = upper2_image)
    self.upper2_button.grid(row=2, column=3, padx=1, pady=1)

    self.upper3_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:upper3_button_command(self.upper3_button,upper3_image))
    self.upper3_button.image = upper3_image
    self.upper3_button.config(image = upper3_image)
    self.upper3_button.grid(row=2, column=4, padx=1, pady=1)

    self.down0_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:down0_button_command(self.down0_button,down0_image))
    self.down0_button.image = down0_image
    self.down0_button.config(image = down0_image)
    self.down0_button.grid(row=5, column=3, padx=1, pady=1)

    self.down1_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:down1_button_command(self.down1_button,down1_image))
    self.down1_button.image = down1_image
    self.down1_button.config(image = down1_image)
    self.down1_button.grid(row=5, column=4, padx=1, pady=1)

    self.down2_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:down2_button_command(self.down2_button,down2_image))
    self.down2_button.image = down2_image
    self.down2_button.config(image = down2_image)
    self.down2_button.grid(row=6, column=3, padx=1, pady=1)

    self.down3_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:down3_button_command(self.down3_button,down3_image))
    self.down3_button.image = down3_image
    self.down3_button.config(image = down3_image)
    self.down3_button.grid(row=6, column=4, padx=1, pady=1)

    self.front0_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:front0_button_command(self.front0_button,front0_image))
    self.front0_button.image = front0_image
    self.front0_button.config(image = front0_image)
    self.front0_button.grid(row=3, column=3, padx=1, pady=1)

    self.front1_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:front1_button_command(self.front1_button,front1_image))
    self.front1_button.image = front1_image
    self.front1_button.config(image = front1_image)
    self.front1_button.grid(row=3, column=4, padx=1, pady=1)

    self.front2_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:front2_button_command(self.front2_button,front2_image))
    self.front2_button.image = front2_image
    self.front2_button.config(image = front2_image)
    self.front2_button.grid(row=4, column=3, padx=1, pady=1)

    self.front3_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:front3_button_command(self.front3_button,front3_image))
    self.front3_button.image = front3_image
    self.front3_button.config(image = front3_image)
    self.front3_button.grid(row=4, column=4, padx=1, pady=1)

    self.back0_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:back0_button_command(self.back0_button,back0_image))
    self.back0_button.image = back0_image
    self.back0_button.config(image = back0_image)
    self.back0_button.grid(row=3, column=7, padx=1, pady=1)

    self.back1_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:back1_button_command(self.back1_button,back1_image))
    self.back1_button.image = back1_image
    self.back1_button.config(image = back1_image)
    self.back1_button.grid(row=3, column=8, padx=1, pady=1)

    self.back2_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:back2_button_command(self.back2_button,back2_image))
    self.back2_button.image = back2_image
    self.back2_button.config(image = back2_image)
    self.back2_button.grid(row=4, column=7, padx=1, pady=1)

    self.back3_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:back3_button_command(self.back3_button,back3_image))
    self.back3_button.image = back3_image
    self.back3_button.config(image = back3_image)
    self.back3_button.grid(row=4, column=8, padx=1, pady=1)

    self.left0_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:left0_button_command(self.left0_button,left0_image))
    self.left0_button.image = left0_image
    self.left0_button.config(image = left0_image)
    self.left0_button.grid(row=3, column=1, padx=1, pady=1)

    self.left1_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:left1_button_command(self.left1_button,left1_image))
    self.left1_button.image = left1_image
    self.left1_button.config(image = left1_image)
    self.left1_button.grid(row=3, column=2, padx=1, pady=1)

    self.left2_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:left2_button_command(self.left2_button,left2_image))
    self.left2_button.image = left2_image
    self.left2_button.config(image = left2_image)
    self.left2_button.grid(row=4, column=1, padx=1, pady=1)

    self.left3_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:left3_button_command(self.left3_button,left3_image))
    self.left3_button.image = left3_image
    self.left3_button.config(image = left3_image)
    self.left3_button.grid(row=4, column=2, padx=1, pady=1)

    self.right0_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:right0_button_command(self.right0_button,right0_image))
    self.right0_button.image = right0_image
    self.right0_button.config(image = right0_image)
    self.right0_button.grid(row=3, column=5, padx=1, pady=1)

    self.right1_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:right1_button_command(self.right1_button,right1_image))
    self.right1_button.image = right1_image
    self.right1_button.config(image = right1_image)
    self.right1_button.grid(row=3, column=6, padx=1, pady=1)

    self.right2_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:right2_button_command(self.right2_button,right2_image))
    self.right2_button.image = right2_image
    self.right2_button.config(image = right2_image)
    self.right2_button.grid(row=4, column=5, padx=1, pady=1)

    self.right3_button = tk.Button(self.user_input, bg="#DEDDDD", command=lambda:right3_button_command(self.right3_button,right3_image))
    self.right3_button.image = right3_image
    self.right3_button.config(image = right3_image)
    self.right3_button.grid(row=4, column=6, padx=1, pady=1)



def upper0_button_command(button, image):
    global upper0ID

    if(upper0ID == 6):
        upper0ID=0
    upper0ID = upper0ID + 1

    if(upper0ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_white' + '.png'))
    if(upper0ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_yellow' + '.png'))
    if(upper0ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_blue' + '.png'))
    if(upper0ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_green' + '.png'))
    if(upper0ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_red' + '.png'))
    if(upper0ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def upper1_button_command(button, image):
    global upper1ID

    if(upper1ID == 6):
        upper1ID=0
    upper1ID = upper1ID + 1

    if(upper1ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_white' + '.png'))
    if(upper1ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_yellow' + '.png'))
    if(upper1ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_blue' + '.png'))
    if(upper1ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_green' + '.png'))
    if(upper1ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_red' + '.png'))
    if(upper1ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def upper2_button_command(button, image):
    global upper2ID

    if(upper2ID == 6):
        upper2ID=0
    upper2ID = upper2ID + 1

    if(upper2ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_white' + '.png'))
    if(upper2ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_yellow' + '.png'))
    if(upper2ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_blue' + '.png'))
    if(upper2ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_green' + '.png'))
    if(upper2ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_red' + '.png'))
    if(upper2ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def upper3_button_command(button, image):
    global upper3ID

    if(upper3ID == 6):
        upper3ID=0
    upper3ID = upper3ID + 1

    if(upper3ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_white' + '.png'))
    if(upper3ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_yellow' + '.png'))
    if(upper3ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_blue' + '.png'))
    if(upper3ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_green' + '.png'))
    if(upper3ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_red' + '.png'))
    if(upper3ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_orange' + '.png'))

    button.config(image = image)
    button.image = image

def down0_button_command(button, image):
    global down0ID

    if(down0ID == 6):
        down0ID=0
    down0ID = down0ID + 1

    if(down0ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_white' + '.png'))
    if(down0ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_yellow' + '.png'))
    if(down0ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_blue' + '.png'))
    if(down0ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_green' + '.png'))
    if(down0ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_red' + '.png'))
    if(down0ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down1_button_command(button, image):
    global down1ID

    if(down1ID == 6):
        down1ID=0
    down1ID = down1ID + 1

    if(down1ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_white' + '.png'))
    if(down1ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_yellow' + '.png'))
    if(down1ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_blue' + '.png'))
    if(down1ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_green' + '.png'))
    if(down1ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_red' + '.png'))
    if(down1ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down2_button_command(button, image):
    global down2ID

    if(down2ID == 6):
        down2ID=0
    down2ID = down2ID + 1

    if(down2ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_white' + '.png'))
    if(down2ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_yellow' + '.png'))
    if(down2ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_blue' + '.png'))
    if(down2ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_green' + '.png'))
    if(down2ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_red' + '.png'))
    if(down2ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down3_button_command(button, image):
    global down3ID

    if(down3ID == 6):
        down3ID=0
    down3ID = down3ID + 1

    if(down3ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_white' + '.png'))
    if(down3ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_yellow' + '.png'))
    if(down3ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_blue' + '.png'))
    if(down3ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_green' + '.png'))
    if(down3ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_red' + '.png'))
    if(down3ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_orange' + '.png'))

    button.config(image = image)
    button.image = image

def front0_button_command(button, image):
    global front0ID

    if(front0ID == 6):
        front0ID=0
    front0ID = front0ID + 1

    if(front0ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_white' + '.png'))
    if(front0ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_yellow' + '.png'))
    if(front0ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_blue' + '.png'))
    if(front0ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_green' + '.png'))
    if(front0ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_red' + '.png'))
    if(front0ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def front1_button_command(button, image):
    global front1ID

    if(front1ID == 6):
        front1ID=0
    front1ID = front1ID + 1

    if(front1ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_white' + '.png'))
    if(front1ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_yellow' + '.png'))
    if(front1ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_blue' + '.png'))
    if(front1ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_green' + '.png'))
    if(front1ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_red' + '.png'))
    if(front1ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def front2_button_command(button, image):
    global front2ID

    if(front2ID == 6):
        front2ID=0
    front2ID = front2ID + 1

    if(front2ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_white' + '.png'))
    if(front2ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_yellow' + '.png'))
    if(front2ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_blue' + '.png'))
    if(front2ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_green' + '.png'))
    if(front2ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_red' + '.png'))
    if(front2ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def front3_button_command(button, image):
    global front3ID

    if(front3ID == 6):
        front3ID=0
    front3ID = front3ID + 1

    if(front3ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_white' + '.png'))
    if(front3ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_yellow' + '.png'))
    if(front3ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_blue' + '.png'))
    if(front3ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_green' + '.png'))
    if(front3ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_red' + '.png'))
    if(front3ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_orange' + '.png'))

    button.config(image = image)
    button.image = image

def back0_button_command(button, image):
    global back0ID

    if(back0ID == 6):
        back0ID=0
    back0ID = back0ID + 1

    if(back0ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_white' + '.png'))
    if(back0ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_yellow' + '.png'))
    if(back0ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_blue' + '.png'))
    if(back0ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_green' + '.png'))
    if(back0ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_red' + '.png'))
    if(back0ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back1_button_command(button, image):
    global back1ID

    if(back1ID == 6):
        back1ID=0
    back1ID = back1ID + 1

    if(back1ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_white' + '.png'))
    if(back1ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_yellow' + '.png'))
    if(back1ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_blue' + '.png'))
    if(back1ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_green' + '.png'))
    if(back1ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_red' + '.png'))
    if(back1ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back2_button_command(button, image):
    global back2ID

    if(back2ID == 6):
        back2ID=0
    back2ID = back2ID + 1

    if(back2ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_white' + '.png'))
    if(back2ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_yellow' + '.png'))
    if(back2ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_blue' + '.png'))
    if(back2ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_green' + '.png'))
    if(back2ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_red' + '.png'))
    if(back2ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back3_button_command(button, image):
    global back3ID

    if(back3ID == 6):
        back3ID=0
    back3ID = back3ID + 1

    if(back3ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_white' + '.png'))
    if(back3ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_yellow' + '.png'))
    if(back3ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_blue' + '.png'))
    if(back3ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_green' + '.png'))
    if(back3ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_red' + '.png'))
    if(back3ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_orange' + '.png'))

    button.config(image = image)
    button.image = image

def left0_button_command(button, image):
    global left0ID

    if(left0ID == 6):
        left0ID=0
    left0ID = left0ID + 1

    if(left0ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_white' + '.png'))
    if(left0ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_yellow' + '.png'))
    if(left0ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_blue' + '.png'))
    if(left0ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_green' + '.png'))
    if(left0ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_red' + '.png'))
    if(left0ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left1_button_command(button, image):
    global left1ID

    if(left1ID == 6):
        left1ID=0
    left1ID = left1ID + 1

    if(left1ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_white' + '.png'))
    if(left1ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_yellow' + '.png'))
    if(left1ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_blue' + '.png'))
    if(left1ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_green' + '.png'))
    if(left1ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_red' + '.png'))
    if(left1ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left2_button_command(button, image):
    global left2ID

    if(left2ID == 6):
        left2ID=0
    left2ID = left2ID + 1

    if(left2ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_white' + '.png'))
    if(left2ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_yellow' + '.png'))
    if(left2ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_blue' + '.png'))
    if(left2ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_green' + '.png'))
    if(left2ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_red' + '.png'))
    if(left2ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left3_button_command(button, image):
    global left3ID

    if(left3ID == 6):
        left3ID=0
    left3ID = left3ID + 1

    if(left3ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_white' + '.png'))
    if(left3ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_yellow' + '.png'))
    if(left3ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_blue' + '.png'))
    if(left3ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_green' + '.png'))
    if(left3ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_red' + '.png'))
    if(left3ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_orange' + '.png'))

    button.config(image = image)
    button.image = image

def right0_button_command(button, image):
    global right0ID

    if(right0ID == 6):
        right0ID=0
    right0ID = right0ID + 1

    if(right0ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_white' + '.png'))
    if(right0ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_yellow' + '.png'))
    if(right0ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_blue' + '.png'))
    if(right0ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_green' + '.png'))
    if(right0ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_red' + '.png'))
    if(right0ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right1_button_command(button, image):
    global right1ID

    if(right1ID == 6):
        right1ID=0
    right1ID = right1ID + 1

    if(right1ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_white' + '.png'))
    if(right1ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_yellow' + '.png'))
    if(right1ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_blue' + '.png'))
    if(right1ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_green' + '.png'))
    if(right1ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_red' + '.png'))
    if(right1ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right2_button_command(button, image):
    global right2ID

    if(right2ID == 6):
        right2ID=0
    right2ID = right2ID + 1

    if(right2ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_white' + '.png'))
    if(right2ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_yellow' + '.png'))
    if(right2ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_blue' + '.png'))
    if(right2ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_green' + '.png'))
    if(right2ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_red' + '.png'))
    if(right2ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right3_button_command(button, image):
    global right3ID

    if(right3ID == 6):
        right3ID=0
    right3ID = right3ID + 1

    if(right3ID == 1):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_white' + '.png'))
    if(right3ID == 2):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_yellow' + '.png'))
    if(right3ID == 3):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_blue' + '.png'))
    if(right3ID == 4):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_green' + '.png'))
    if(right3ID == 5):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_red' + '.png'))
    if(right3ID == 6):image = tk.PhotoImage(file=(os.getcwd() + '/Assets/Set_Images/set_' + 'right3_orange' + '.png'))

    button.config(image = image)
    button.image = image