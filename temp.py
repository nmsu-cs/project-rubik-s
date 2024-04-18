
import tkinter as tk
from PIL import Image, ImageTk
import os


def submit_button_command(master):
    global upper0ID
    global upper1ID
    global upper2ID
    global upper3ID
    global down0ID
    global down1ID
    global down2ID
    global down3ID
    global U
    global D
    
    U = [upper0ID,upper1ID,upper2ID,upper3ID]
    D = [down0ID ,down1ID ,down2ID ,down3ID ]
    
    color_dict = {  0 : 'w',
                    1 : 'y',
                    2 : 'b',
                    3 : 'g',
                    4 : 'r',
                    5 : 'o'}  
    
    for i in range(4):
        U[i] = color_dict[U[i]]
        D[i] = color_dict[D[i]]

    master.destroy()
        
def get():
    global U
    global D
    return(U,D)


def GUI(master):

    color_dict = {  'w' : 'white',
                    'y' : 'yellow',
                    'r' : 'red',
                    'b' : 'blue',
                    'g' : 'green',
                    'o' : 'orange'} 
    

    upper = ['w','w','w','w']
    down =  ['y','y','y','y']

    global upper0ID
    global upper1ID
    global upper2ID
    global upper3ID
    global down0ID
    global down1ID
    global down2ID
    global down3ID

    upper0ID = 0
    upper1ID = 0
    upper2ID = 0
    upper3ID = 0
    down0ID = 1
    down1ID = 1
    down2ID = 1
    down3ID = 1

    set_input = tk.Toplevel(master,bg="#EEEEEE")
    set_input.title("Enter a Rubik's Cube")

    # Calculate the position of the Toplevel window
    x = (set_input.winfo_screenwidth() - 300) // 6  # Center horizontally
    y = (set_input.winfo_screenheight() - 150) // 6  # Center vertically

    # Set Format the size and position of the window
    set_input.geometry("+{}+{}".format(x, y))
    set_input.geometry("480x400")
    
    # Load all images
    upper0_image = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper0_'  + color_dict[upper[0]] + '.png').resize((50,50)))
    upper1_image = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper1_'  + color_dict[upper[0]] + '.png').resize((50,50)))
    upper2_image = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper2_'  + color_dict[upper[0]] + '.png').resize((50,50)))
    upper3_image = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'upper3_'  + color_dict[upper[0]] + '.png').resize((50,50)))
    down0_image  = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'down0_'   + color_dict[down[0]]  + '.png').resize((50,50)))
    down1_image  = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'down1_'   + color_dict[down[0]]  + '.png').resize((50,50)))
    down2_image  = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'down2_'   + color_dict[down[0]]  + '.png').resize((50,50)))
    down3_image  = ImageTk.PhotoImage(Image.open(os.getcwd()  + '/Assets/Set_Images/set_' + 'down3_'   + color_dict[down[0]]  + '.png').resize((50,50)))


    # Pack all buttons
    upper0_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:upper0_button_command(upper0_button,upper0_image))
    upper0_button.image = upper0_image
    upper0_button.config(image = upper0_image)
    upper0_button.grid(row=1, column=3, padx=1, pady=1)

    upper1_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:upper1_button_command(upper1_button,upper1_image))
    upper1_button.image = upper1_image
    upper1_button.config(image = upper1_image)
    upper1_button.grid(row=1, column=4, padx=1, pady=1)

    upper2_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:upper2_button_command(upper2_button,upper2_image))
    upper2_button.image = upper2_image
    upper2_button.config(image = upper2_image)
    upper2_button.grid(row=2, column=3, padx=1, pady=1)

    upper3_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:upper3_button_command(upper3_button,upper3_image))
    upper3_button.image = upper3_image
    upper3_button.config(image = upper3_image)
    upper3_button.grid(row=2, column=4, padx=1, pady=1)

    down0_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:down0_button_command(down0_button,down0_image))
    down0_button.image = down0_image
    down0_button.config(image = down0_image)
    down0_button.grid(row=5, column=3, padx=1, pady=1)

    down1_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:down1_button_command(down1_button,down1_image))
    down1_button.image = down1_image
    down1_button.config(image = down1_image)
    down1_button.grid(row=5, column=4, padx=1, pady=1)

    down2_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:down2_button_command(down2_button,down2_image))
    down2_button.image = down2_image
    down2_button.config(image = down2_image)
    down2_button.grid(row=6, column=3, padx=1, pady=1)

    down3_button = tk.Button(set_input, bg="#DEDDDD", command=lambda:down3_button_command(down3_button,down3_image))
    down3_button.image = down3_image
    down3_button.config(image = down3_image)
    down3_button.grid(row=6, column=4, padx=1, pady=1)

    
    submit_button = tk.Button(set_input,text="Submit",bg="gray",width = 5, command = submit_button_command(master))
    submit_button.grid(row=1,column=7,columnspan=2,padx=1,pady=1)















def upper0_button_command(button, image):
    global upper0ID

    upper0ID = upper0ID + 1
    if(upper0ID >= 6):
        upper0ID=0

    if(upper0ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_white' + '.png').resize((50,50)))
    if(upper0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_yellow' + '.png').resize((50,50)))
    if(upper0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_blue' + '.png').resize((50,50)))
    if(upper0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_green' + '.png').resize((50,50)))
    if(upper0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_red' + '.png').resize((50,50)))
    if(upper0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def upper1_button_command(button, image):
    global upper1ID

    upper1ID = upper1ID + 1
    if(upper1ID >= 6):
        upper1ID=0

    if(upper1ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_white' + '.png').resize((50,50)))
    if(upper1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_yellow' + '.png').resize((50,50)))
    if(upper1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_blue' + '.png').resize((50,50)))
    if(upper1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_green' + '.png').resize((50,50)))
    if(upper1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_red' + '.png').resize((50,50)))
    if(upper1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def upper2_button_command(button, image):
    global upper2ID

    upper2ID = upper2ID + 1
    if(upper2ID >= 6):
        upper2ID=0

    if(upper2ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_white' + '.png').resize((50,50)))
    if(upper2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_yellow' + '.png').resize((50,50)))
    if(upper2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_blue' + '.png').resize((50,50)))
    if(upper2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_green' + '.png').resize((50,50)))
    if(upper2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_red' + '.png').resize((50,50)))
    if(upper2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def upper3_button_command(button, image):
    global upper3ID

    upper3ID = upper3ID + 1
    if(upper3ID >= 6):
        upper3ID=0

    if(upper3ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_white' + '.png').resize((50,50)))
    if(upper3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_yellow' + '.png').resize((50,50)))
    if(upper3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_blue' + '.png').resize((50,50)))
    if(upper3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_green' + '.png').resize((50,50)))
    if(upper3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_red' + '.png').resize((50,50)))
    if(upper3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def down0_button_command(button, image):
    global down0ID

    down0ID = down0ID + 1
    if(down0ID >=6):
        down0ID=0

    if(down0ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_white' + '.png').resize((50,50)))
    if(down0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_yellow' + '.png').resize((50,50)))
    if(down0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_blue' + '.png').resize((50,50)))
    if(down0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_green' + '.png').resize((50,50)))
    if(down0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_red' + '.png').resize((50,50)))
    if(down0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def down1_button_command(button, image):
    global down1ID

    down1ID = down1ID + 1
    if(down1ID >= 6):
        down1ID=0

    if(down1ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_white' + '.png').resize((50,50)))
    if(down1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_yellow' + '.png').resize((50,50)))
    if(down1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_blue' + '.png').resize((50,50)))
    if(down1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_green' + '.png').resize((50,50)))
    if(down1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_red' + '.png').resize((50,50)))
    if(down1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def down2_button_command(button, image):
    global down2ID

    down2ID = down2ID + 1
    if(down2ID >= 6):
        down2ID=0

    if(down2ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_white' + '.png').resize((50,50)))
    if(down2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_yellow' + '.png').resize((50,50)))
    if(down2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_blue' + '.png').resize((50,50)))
    if(down2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_green' + '.png').resize((50,50)))
    if(down2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_red' + '.png').resize((50,50)))
    if(down2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image


def down3_button_command(button, image):
    global down3ID

    down3ID = down3ID + 1
    if(down3ID >= 6):
        down3ID=0

    if(down3ID == 0):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_white' + '.png').resize((50,50)))
    if(down3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_yellow' + '.png').resize((50,50)))
    if(down3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_blue' + '.png').resize((50,50)))
    if(down3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_green' + '.png').resize((50,50)))
    if(down3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_red' + '.png').resize((50,50)))
    if(down3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_orange' + '.png').resize((50,50)))

    button.config(image = image)
    button.image = image

