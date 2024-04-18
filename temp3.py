from PIL import Image,ImageTk
import os

def upper0_button_command(button, image):
    global upper0ID

    if(upper0ID == 6):
        upper0ID=0
    upper0ID = upper0ID + 1

    if(upper0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_white' + '.png'))
    if(upper0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_yellow' + '.png'))
    if(upper0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_blue' + '.png'))
    if(upper0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_green' + '.png'))
    if(upper0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_red' + '.png'))
    if(upper0ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def upper1_button_command(button, image):
    global upper1ID

    if(upper1ID == 6):
        upper1ID=0
    upper1ID = upper1ID + 1

    if(upper1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_white' + '.png'))
    if(upper1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_yellow' + '.png'))
    if(upper1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_blue' + '.png'))
    if(upper1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_green' + '.png'))
    if(upper1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_red' + '.png'))
    if(upper1ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def upper2_button_command(button, image):
    global upper2ID

    if(upper2ID == 6):
        upper2ID=0
    upper2ID = upper2ID + 1

    if(upper2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_white' + '.png'))
    if(upper2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_yellow' + '.png'))
    if(upper2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_blue' + '.png'))
    if(upper2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_green' + '.png'))
    if(upper2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_red' + '.png'))
    if(upper2ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def upper3_button_command(button, image):
    global upper3ID

    if(upper3ID == 6):
        upper3ID=0
    upper3ID = upper3ID + 1

    if(upper3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_white' + '.png'))
    if(upper3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_yellow' + '.png'))
    if(upper3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_blue' + '.png'))
    if(upper3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_green' + '.png'))
    if(upper3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_red' + '.png'))
    if(upper3ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'upper3_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down0_button_command(button, image):
    global down0ID

    if(down0ID == 6):
        down0ID=0
    down0ID = down0ID + 1

    if(down0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_white' + '.png'))
    if(down0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_yellow' + '.png'))
    if(down0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_blue' + '.png'))
    if(down0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_green' + '.png'))
    if(down0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_red' + '.png'))
    if(down0ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down1_button_command(button, image):
    global down1ID

    if(down1ID == 6):
        down1ID=0
    down1ID = down1ID + 1

    if(down1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_white' + '.png'))
    if(down1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_yellow' + '.png'))
    if(down1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_blue' + '.png'))
    if(down1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_green' + '.png'))
    if(down1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_red' + '.png'))
    if(down1ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down2_button_command(button, image):
    global down2ID

    if(down2ID == 6):
        down2ID=0
    down2ID = down2ID + 1

    if(down2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_white' + '.png'))
    if(down2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_yellow' + '.png'))
    if(down2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_blue' + '.png'))
    if(down2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_green' + '.png'))
    if(down2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_red' + '.png'))
    if(down2ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def down3_button_command(button, image):
    global down3ID

    if(down3ID == 6):
        down3ID=0
    down3ID = down3ID + 1

    if(down3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_white' + '.png'))
    if(down3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_yellow' + '.png'))
    if(down3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_blue' + '.png'))
    if(down3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_green' + '.png'))
    if(down3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_red' + '.png'))
    if(down3ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'down3_orange' + '.png'))

    button.config(image = image)
    button.image = image

def front0_button_command(button, image):
    global front0ID

    if(front0ID == 6):
        front0ID=0
    front0ID = front0ID + 1

    if(front0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_white' + '.png'))
    if(front0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_yellow' + '.png'))
    if(front0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_blue' + '.png'))
    if(front0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_green' + '.png'))
    if(front0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_red' + '.png'))
    if(front0ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def front1_button_command(button, image):
    global front1ID

    if(front1ID == 6):
        front1ID=0
    front1ID = front1ID + 1

    if(front1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_white' + '.png'))
    if(front1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_yellow' + '.png'))
    if(front1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_blue' + '.png'))
    if(front1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_green' + '.png'))
    if(front1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_red' + '.png'))
    if(front1ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def front2_button_command(button, image):
    global front2ID

    if(front2ID == 6):
        front2ID=0
    front2ID = front2ID + 1

    if(front2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_white' + '.png'))
    if(front2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_yellow' + '.png'))
    if(front2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_blue' + '.png'))
    if(front2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_green' + '.png'))
    if(front2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_red' + '.png'))
    if(front2ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def front3_button_command(button, image):
    global front3ID

    if(front3ID == 6):
        front3ID=0
    front3ID = front3ID + 1

    if(front3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_white' + '.png'))
    if(front3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_yellow' + '.png'))
    if(front3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_blue' + '.png'))
    if(front3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_green' + '.png'))
    if(front3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_red' + '.png'))
    if(front3ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'front3_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back0_button_command(button, image):
    global back0ID

    if(back0ID == 6):
        back0ID=0
    back0ID = back0ID + 1

    if(back0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_white' + '.png'))
    if(back0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_yellow' + '.png'))
    if(back0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_blue' + '.png'))
    if(back0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_green' + '.png'))
    if(back0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_red' + '.png'))
    if(back0ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back1_button_command(button, image):
    global back1ID

    if(back1ID == 6):
        back1ID=0
    back1ID = back1ID + 1

    if(back1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_white' + '.png'))
    if(back1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_yellow' + '.png'))
    if(back1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_blue' + '.png'))
    if(back1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_green' + '.png'))
    if(back1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_red' + '.png'))
    if(back1ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back2_button_command(button, image):
    global back2ID

    if(back2ID == 6):
        back2ID=0
    back2ID = back2ID + 1

    if(back2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_white' + '.png'))
    if(back2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_yellow' + '.png'))
    if(back2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_blue' + '.png'))
    if(back2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_green' + '.png'))
    if(back2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_red' + '.png'))
    if(back2ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def back3_button_command(button, image):
    global back3ID

    if(back3ID == 6):
        back3ID=0
    back3ID = back3ID + 1

    if(back3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_white' + '.png'))
    if(back3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_yellow' + '.png'))
    if(back3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_blue' + '.png'))
    if(back3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_green' + '.png'))
    if(back3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_red' + '.png'))
    if(back3ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'back3_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left0_button_command(button, image):
    global left0ID

    if(left0ID == 6):
        left0ID=0
    left0ID = left0ID + 1

    if(left0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_white' + '.png'))
    if(left0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_yellow' + '.png'))
    if(left0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_blue' + '.png'))
    if(left0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_green' + '.png'))
    if(left0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_red' + '.png'))
    if(left0ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left1_button_command(button, image):
    global left1ID

    if(left1ID == 6):
        left1ID=0
    left1ID = left1ID + 1

    if(left1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_white' + '.png'))
    if(left1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_yellow' + '.png'))
    if(left1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_blue' + '.png'))
    if(left1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_green' + '.png'))
    if(left1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_red' + '.png'))
    if(left1ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left2_button_command(button, image):
    global left2ID

    if(left2ID == 6):
        left2ID=0
    left2ID = left2ID + 1

    if(left2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_white' + '.png'))
    if(left2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_yellow' + '.png'))
    if(left2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_blue' + '.png'))
    if(left2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_green' + '.png'))
    if(left2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_red' + '.png'))
    if(left2ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def left3_button_command(button, image):
    global left3ID

    if(left3ID == 6):
        left3ID=0
    left3ID = left3ID + 1

    if(left3ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_white' + '.png'))
    if(left3ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_yellow' + '.png'))
    if(left3ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_blue' + '.png'))
    if(left3ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_green' + '.png'))
    if(left3ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_red' + '.png'))
    if(left3ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'left3_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right0_button_command(button, image):
    global right0ID

    if(right0ID == 6):
        right0ID=0
    right0ID = right0ID + 1

    if(right0ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_white' + '.png'))
    if(right0ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_yellow' + '.png'))
    if(right0ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_blue' + '.png'))
    if(right0ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_green' + '.png'))
    if(right0ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_red' + '.png'))
    if(right0ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right0_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right1_button_command(button, image):
    global right1ID

    if(right1ID == 6):
        right1ID=0
    right1ID = right1ID + 1

    if(right1ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_white' + '.png'))
    if(right1ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_yellow' + '.png'))
    if(right1ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_blue' + '.png'))
    if(right1ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_green' + '.png'))
    if(right1ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_red' + '.png'))
    if(right1ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right1_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right2_button_command(button, image):
    global right2ID

    if(right2ID == 6):
        right2ID=0
    right2ID = right2ID + 1

    if(right2ID == 1):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_white' + '.png'))
    if(right2ID == 2):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_yellow' + '.png'))
    if(right2ID == 3):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_blue' + '.png'))
    if(right2ID == 4):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_green' + '.png'))
    if(right2ID == 5):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_red' + '.png'))
    if(right2ID == 6):image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Set_Images/set_' + 'right2_orange' + '.png'))

    button.config(image = image)
    button.image = image


def right3_button_command(button, image):