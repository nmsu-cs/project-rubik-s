# Display Class
# Called from GUI Main program "Cube.py"
# Function: Will display the cube on the GUI Display screen
# Parameters: The current configuration of the cube 
#             through arrays upper,down,front,back,left,right
# Precondition: Parameters upper,down,front,back,left,right must already be defined
# Postcondition: Will update the Display on the main screen whenever called

import os
from PIL import ImageTk, Image
def display(self,upper,down,front,back,left,right):
    view = 0
    if(view == 1):
        display1(self,upper,down,front,back,left,right)
    else:
        display0(self,upper,down,front,back,left,right)


def display1(self,upper,down,front,back,left,right):
    color_dict = {  'w' : 'white',
                    'y' : 'yellow',
                    'r' : 'red',
                    'b' : 'blue',
                    'g' : 'green',
                    'o' : 'orange'}  

    if hasattr(self, 'v0_left0_image_id'):
        self.canvas_cube.delete(self.v0_left0_image_id)
        self.canvas_cube.delete(self.v0_left1_image_id)
        self.canvas_cube.delete(self.v0_left2_image_id)
        self.canvas_cube.delete(self.v0_left3_image_id)
        self.canvas_cube.delete(self.v0_upper0_image_id)
        self.canvas_cube.delete(self.v0_upper1_image_id)
        self.canvas_cube.delete(self.v0_upper2_image_id)
        self.canvas_cube.delete(self.v0_upper3_image_id)
        self.canvas_cube.delete(self.v0_right0_image_id)
        self.canvas_cube.delete(self.v0_right1_image_id)
        self.canvas_cube.delete(self.v0_right2_image_id)
        self.canvas_cube.delete(self.v0_right3_image_id)
        self.canvas_cube.delete(self.v0_front0_image_id)
        self.canvas_cube.delete(self.v0_front1_image_id)
        self.canvas_cube.delete(self.v0_front2_image_id)
        self.canvas_cube.delete(self.v0_front3_image_id)
    
    
    ## Place images
    ## Note: "left" and "back" faces are placed first so they are layered behind everything
    # Cube back face
    v1_back0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back0_' + color_dict[back[0]] + '.png').resize((72,108)))
    self.v1_back0_image_id = self.canvas_cube.create_image(635, 133, image=v1_back0_image, anchor='center')
    self.v1_back0_image = v1_back0_image
    self.canvas_cube.itemconfig(self.v1_back0_image_id, image=v1_back0_image)

    v1_back1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back1_' + color_dict[back[1]] + '.png').resize((64,94)))
    self.v1_back1_image_id = self.canvas_cube.create_image(560,101, image=v1_back1_image, anchor='center')
    self.v1_back1_image = v1_back1_image
    self.canvas_cube.itemconfig(self.v1_back1_image_id, image=v1_back1_image)

    v1_back2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back2_' + color_dict[back[2]] + '.png').resize((72,94)))
    self.v1_back2_image_id = self.canvas_cube.create_image(635, 204, image=v1_back2_image, anchor='center')
    self.v1_back2_image = v1_back2_image
    self.canvas_cube.itemconfig(self.v1_back2_image_id, image=v1_back2_image)

    v1_back3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back3_' + color_dict[back[3]] + '.png').resize((63,99)))
    self.v1_back3_image_id = self.canvas_cube.create_image(560, 172, image=v1_back3_image, anchor='center')
    self.v1_back3_image = v1_back3_image
    self.canvas_cube.itemconfig(self.v1_back3_image_id, image=v1_back3_image)

    # # Cube left face
    v1_left0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left0_' + color_dict[left[0]] + '.png').resize((64,96)))
    self.v1_left0_image_id = self.canvas_cube.create_image(182, 101, image=v1_left0_image, anchor='center')
    self.v1_left0_image = v1_left0_image
    self.canvas_cube.itemconfig(self.v1_left0_image_id, image=v1_left0_image)

    v1_left1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left1_' + color_dict[left[1]] + '.png').resize((71,110)))
    self.v1_left1_image_id = self.canvas_cube.create_image(107,133, image=v1_left1_image, anchor='center')
    self.v1_left1_image = v1_left1_image
    self.canvas_cube.itemconfig(self.v1_left1_image_id, image=v1_left1_image)

    v1_left2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left2_' + color_dict[left[2]] + '.png').resize((63,97)))
    self.v1_left2_image_id = self.canvas_cube.create_image(182, 172, image=v1_left2_image, anchor='center')
    self.v1_left2_image = v1_left2_image
    self.canvas_cube.itemconfig(self.v1_left2_image_id, image=v1_left2_image)

    v1_left3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left3_' + color_dict[left[3]] + '.png').resize((71,91)))
    self.v1_left3_image_id = self.canvas_cube.create_image(107, 204, image=v1_left3_image, anchor='center')
    self.v1_left3_image = v1_left3_image
    self.canvas_cube.itemconfig(self.v1_left3_image_id, image=v1_left3_image)
                         
    # Cube Background Sillhouette
    v1_background_cube_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_cube_background.png'))
    self.v1_background_cube_image_id = self.canvas_cube.create_image(371,250,image=v1_background_cube_image,anchor='center')
    self.v1_background_cube_image = v1_background_cube_image
    self.canvas_cube.itemconfig(self.v1_background_cube_image_id, image=v1_background_cube_image)

    # Cube Upper Face
    v1_upper0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper0_' + color_dict[upper[0]] + '.png'))
    self.v1_upper0_image_id = self.canvas_cube.create_image(371, 95, image=v1_upper0_image, anchor='center')
    self.v1_upper0_image = v1_upper0_image
    self.canvas_cube.itemconfig(self.v1_upper0_image_id, image=v1_upper0_image)

    v1_upper1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper1_' + color_dict[upper[1]] + '.png'))
    self.v1_upper1_image_id = self.canvas_cube.create_image(459, 141, image=v1_upper1_image, anchor='center')
    self.v1_upper1_image = v1_upper1_image
    self.canvas_cube.itemconfig(self.v1_upper1_image_id, image=v1_upper1_image)

    v1_upper2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper2_' + color_dict[upper[2]] + '.png'))
    self.v1_upper2_image_id = self.canvas_cube.create_image(284, 140, image=v1_upper2_image, anchor='center')
    self.v1_upper2_image = v1_upper2_image
    self.canvas_cube.itemconfig(self.v1_upper2_image_id, image=v1_upper2_image)

    v1_upper3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper3_' + color_dict[upper[3]] + '.png'))
    self.v1_upper3_image_id = self.canvas_cube.create_image(372, 185, image=v1_upper3_image, anchor='center')
    self.v1_upper3_image = v1_upper3_image
    self.canvas_cube.itemconfig(self.v1_upper3_image_id, image=v1_upper3_image)

    # Cube Front Face
    v1_front0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front0_' + color_dict[front[0]] + '.png'))
    self.v1_front0_image_id = self.canvas_cube.create_image(215, 231, image=v1_front0_image, anchor='center')
    self.v1_front0_image = v1_front0_image
    self.canvas_cube.itemconfig(self.v1_front0_image_id, image=v1_front0_image)

    v1_front1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front1_' + color_dict[front[1]] + '.png'))
    self.v1_front1_image_id = self.canvas_cube.create_image(315, 276, image=v1_front1_image, anchor='center')
    self.v1_front1_image = v1_front1_image
    self.canvas_cube.itemconfig(self.v1_front1_image_id, image=v1_front1_image)

    v1_front2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front2_' + color_dict[front[2]] + '.png'))
    self.v1_front2_image_id = self.canvas_cube.create_image(215, 328, image=v1_front2_image, anchor='center')
    self.v1_front2_image = v1_front2_image
    self.canvas_cube.itemconfig(self.v1_front2_image_id, image=v1_front2_image)

    v1_front3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front3_' + color_dict[front[3]] + '.png'))
    self.v1_front3_image_id = self.canvas_cube.create_image(315, 373, image=v1_front3_image, anchor='center')
    self.v1_front3_image = v1_front3_image
    self.canvas_cube.itemconfig(self.v1_front3_image_id, image=v1_front3_image)  

    # Cube Right Face
    v1_right0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right0_' + color_dict[right[0]] + '.png'))
    self.v1_right0_image_id = self.canvas_cube.create_image(427, 276, image=v1_right0_image, anchor='center')
    self.v1_right0_image = v1_right0_image
    self.canvas_cube.itemconfig(self.v1_right0_image_id, image=v1_right0_image)

    v1_right1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right1_' + color_dict[right[1]] + '.png'))
    self.v1_right1_image_id = self.canvas_cube.create_image(528, 231, image=v1_right1_image, anchor='center')
    self.v1_right1_image = v1_right1_image
    self.canvas_cube.itemconfig(self.v1_right1_image_id, image=v1_right1_image)

    v1_right2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right2_' + color_dict[right[2]] + '.png'))
    self.v1_right2_image_id = self.canvas_cube.create_image(427, 373, image=v1_right2_image, anchor='center')
    self.v1_right2_image = v1_right2_image
    self.canvas_cube.itemconfig(self.v1_right2_image_id, image=v1_right2_image)

    v1_right3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right3_' + color_dict[right[3]] + '.png'))
    self.v1_right3_image_id = self.canvas_cube.create_image(528, 328, image=v1_right3_image, anchor='center')
    self.v1_right3_image = v1_right3_image
    self.canvas_cube.itemconfig(self.v1_right3_image_id, image=v1_right3_image)


def display0(self,upper,down,front,back,left,right):
    color_dict = {  'w' : 'white',
                    'y' : 'yellow',
                    'r' : 'red',
                    'b' : 'blue',
                    'g' : 'green',
                    'o' : 'orange'}

    if hasattr(self, 'v1_left0_image_id'):
        self.canvas_cube.delete(self.v1_back0_image_id)
        self.canvas_cube.delete(self.v1_back1_image_id)
        self.canvas_cube.delete(self.v1_back2_image_id)
        self.canvas_cube.delete(self.v1_back3_image_id)
        self.canvas_cube.delete(self.v1_left0_image_id)
        self.canvas_cube.delete(self.v1_left1_image_id)
        self.canvas_cube.delete(self.v1_left2_image_id)
        self.canvas_cube.delete(self.v1_left3_image_id)
        self.canvas_cube.delete(self.v1_upper0_image_id)
        self.canvas_cube.delete(self.v1_upper1_image_id)
        self.canvas_cube.delete(self.v1_upper2_image_id)
        self.canvas_cube.delete(self.v1_upper3_image_id)
        self.canvas_cube.delete(self.v1_right0_image_id)
        self.canvas_cube.delete(self.v1_right1_image_id)
        self.canvas_cube.delete(self.v1_right2_image_id)
        self.canvas_cube.delete(self.v1_right3_image_id)
        self.canvas_cube.delete(self.v1_front0_image_id)
        self.canvas_cube.delete(self.v1_front1_image_id)
        self.canvas_cube.delete(self.v1_front2_image_id)
        self.canvas_cube.delete(self.v1_front3_image_id)    


    # Cube Background Sillhouette
    v0_background_cube_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_cube_background.png'))
    self.v0_background_cube_image_id = self.canvas_cube.create_image(371,250,image=v0_background_cube_image,anchor='center')
    self.v0_background_cube_image = v0_background_cube_image
    self.canvas_cube.itemconfig(self.v0_background_cube_image_id, image=v0_background_cube_image)

    ## Place images
    # Cube left face
    v0_left0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'left0_' + color_dict[left[0]] + '.png'))
    self.v0_left0_image_id = self.canvas_cube.create_image(142, 144, image=v0_left0_image, anchor='center')
    self.v0_left0_image = v0_left0_image
    self.canvas_cube.itemconfig(self.v0_left0_image_id, image=v0_left0_image)

    v0_left1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'left1_' + color_dict[left[1]] + '.png'))
    self.v0_left1_image_id = self.canvas_cube.create_image(176,200, image=v0_left1_image, anchor='center')
    self.v0_left1_image = v0_left1_image
    self.canvas_cube.itemconfig(self.v0_left1_image_id, image=v0_left1_image)

    v0_left2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'left2_' + color_dict[left[2]] + '.png'))
    self.v0_left2_image_id = self.canvas_cube.create_image(142, 264, image=v0_left2_image, anchor='center')
    self.v0_left2_image = v0_left2_image
    self.canvas_cube.itemconfig(self.v0_left2_image_id, image=v0_left2_image)

    v0_left3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'left3_' + color_dict[left[3]] + '.png'))
    self.v0_left3_image_id = self.canvas_cube.create_image(176, 320, image=v0_left3_image, anchor='center')
    self.v0_left3_image = v0_left3_image
    self.canvas_cube.itemconfig(self.v0_left3_image_id, image=v0_left3_image)

    # Cube Upper Face
    v0_upper0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'upper0_' + color_dict[upper[0]] + '.png'))
    self.v0_upper0_image_id = self.canvas_cube.create_image(285, 87, image=v0_upper0_image, anchor='center')
    self.v0_upper0_image = v0_upper0_image
    self.canvas_cube.itemconfig(self.v0_upper0_image_id, image=v0_upper0_image)

    v0_upper1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'upper1_' + color_dict[upper[1]] + '.png'))
    self.v0_upper1_image_id = self.canvas_cube.create_image(455, 87, image=v0_upper1_image, anchor='center')
    self.v0_upper1_image = v0_upper1_image
    self.canvas_cube.itemconfig(self.v0_upper1_image_id, image=v0_upper1_image)

    v0_upper2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'upper2_' + color_dict[upper[2]] + '.png'))
    self.v0_upper2_image_id = self.canvas_cube.create_image(285, 155, image=v0_upper2_image, anchor='center')
    self.v0_upper2_image = v0_upper2_image
    self.canvas_cube.itemconfig(self.v0_upper2_image_id, image=v0_upper2_image)

    v0_upper3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'upper3_' + color_dict[upper[3]] + '.png'))
    self.v0_upper3_image_id = self.canvas_cube.create_image(455, 155, image=v0_upper3_image, anchor='center')
    self.v0_upper3_image = v0_upper3_image
    self.canvas_cube.itemconfig(self.v0_upper3_image_id, image=v0_upper3_image)

    # Cube Front Face
    v0_front0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'front0_' + color_dict[front[0]] + '.png'))
    self.v0_front0_image_id = self.canvas_cube.create_image(285, 260, image=v0_front0_image, anchor='center')
    self.v0_front0_image = v0_front0_image
    self.canvas_cube.itemconfig(self.v0_front0_image_id, image=v0_front0_image)

    v0_front1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'front1_' + color_dict[front[1]] + '.png'))
    self.v0_front1_image_id = self.canvas_cube.create_image(455, 260, image=v0_front1_image, anchor='center')
    self.v0_front1_image = v0_front1_image
    self.canvas_cube.itemconfig(self.v0_front1_image_id, image=v0_front1_image)

    v0_front2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'front2_' + color_dict[front[2]] + '.png'))
    self.v0_front2_image_id = self.canvas_cube.create_image(285, 380, image=v0_front2_image, anchor='center')
    self.v0_front2_image = v0_front2_image
    self.canvas_cube.itemconfig(self.v0_front2_image_id, image=v0_front2_image)

    v0_front3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'front3_' + color_dict[front[3]] + '.png'))
    self.v0_front3_image_id = self.canvas_cube.create_image(455, 380, image=v0_front3_image, anchor='center')
    self.v0_front3_image = v0_front3_image
    self.canvas_cube.itemconfig(self.v0_front3_image_id, image=v0_front3_image)  

    # # Cube Right Face
    v0_right0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'right0_' + color_dict[right[0]] + '.png'))
    self.v0_right0_image_id = self.canvas_cube.create_image(568, 200, image=v0_right0_image, anchor='center')
    self.v0_right0_image = v0_right0_image
    self.canvas_cube.itemconfig(self.v0_right0_image_id, image=v0_right0_image)

    v0_right1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'right1_' + color_dict[right[1]] + '.png'))
    self.v0_right1_image_id = self.canvas_cube.create_image(602, 144, image=v0_right1_image, anchor='center')
    self.v0_right1_image = v0_right1_image
    self.canvas_cube.itemconfig(self.v0_right1_image_id, image=v0_right1_image)

    v0_right2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'right2_' + color_dict[right[2]] + '.png'))
    self.v0_right2_image_id = self.canvas_cube.create_image(568, 320, image=v0_right2_image, anchor='center')
    self.v0_right2_image = v0_right2_image
    self.canvas_cube.itemconfig(self.v0_right2_image_id, image=v0_right2_image)

    v0_right3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v0_' + 'right3_' + color_dict[right[3]] + '.png'))
    self.v0_right3_image_id = self.canvas_cube.create_image(602, 264, image=v0_right3_image, anchor='center')
    self.v0_right3_image = v0_right3_image
    self.canvas_cube.itemconfig(self.v0_right3_image_id, image=v0_right3_image)

