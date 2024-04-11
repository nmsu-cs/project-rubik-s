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
    view = 1
    if(view == 1):
        display1(self,upper,down,front,back,left,right)
    else:
        display2(self,upper,down,front,back,left,right)


def display1(self,upper,down,front,back,left,right):
    color_dict = {  'w' : 'white',
                    'y' : 'yellow',
                    'r' : 'red',
                    'b' : 'blue',
                    'g' : 'green',
                    'o' : 'orange'}
    
    ## Place images
    ## Note: "left" and "back" faces are placed first so they are layered behind everything
    # Cube back face
    back0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back0_' + color_dict[back[0]] + '.png').resize((72,108)))
    self.back0_image_id = self.canvas_cube.create_image(635, 133, image=back0_image, anchor='center')
    self.back0_image = back0_image
    self.canvas_cube.itemconfig(self.back0_image_id, image=back0_image)

    back1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back1_' + color_dict[back[1]] + '.png').resize((64,94)))
    self.back1_image_id = self.canvas_cube.create_image(560,101, image=back1_image, anchor='center')
    self.back1_image = back1_image
    self.canvas_cube.itemconfig(self.back1_image_id, image=back1_image)

    back2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back2_' + color_dict[back[2]] + '.png').resize((72,94)))
    self.back2_image_id = self.canvas_cube.create_image(635, 204, image=back2_image, anchor='center')
    self.back2_image = back2_image
    self.canvas_cube.itemconfig(self.back2_image_id, image=back2_image)

    back3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'back3_' + color_dict[back[3]] + '.png').resize((63,99)))
    self.back3_image_id = self.canvas_cube.create_image(560, 172, image=back3_image, anchor='center')
    self.back3_image = back3_image
    self.canvas_cube.itemconfig(self.back3_image_id, image=back3_image)

    # # Cube left face
    left0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left0_' + color_dict[left[0]] + '.png').resize((64,96)))
    self.left0_image_id = self.canvas_cube.create_image(182, 101, image=left0_image, anchor='center')
    self.left0_image = left0_image
    self.canvas_cube.itemconfig(self.left0_image_id, image=left0_image)

    left1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left1_' + color_dict[left[1]] + '.png').resize((71,110)))
    self.left1_image_id = self.canvas_cube.create_image(107,133, image=left1_image, anchor='center')
    self.left1_image = left1_image
    self.canvas_cube.itemconfig(self.left1_image_id, image=left1_image)

    left2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left2_' + color_dict[left[2]] + '.png').resize((63,97)))
    self.left2_image_id = self.canvas_cube.create_image(182, 172, image=left2_image, anchor='center')
    self.left2_image = left2_image
    self.canvas_cube.itemconfig(self.left2_image_id, image=left2_image)

    left3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'left3_' + color_dict[left[3]] + '.png').resize((71,91)))
    self.left3_image_id = self.canvas_cube.create_image(107, 204, image=left3_image, anchor='center')
    self.left3_image = left3_image
    self.canvas_cube.itemconfig(self.left3_image_id, image=left3_image)
                         
    # Cube Background Sillhouette
    background_cube_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_cube_background.png'))
    background_cube_image = ImageTk.PhotoImage(background_cube_image)
    self.background_cube_image = background_cube_image
    self.canvas_cube.create_image(371,250,image=background_cube_image,anchor='center')

    # Cube Upper Face
    upper0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper0_' + color_dict[upper[0]] + '.png'))
    self.upper0_image_id = self.canvas_cube.create_image(371, 95, image=upper0_image, anchor='center')
    self.upper0_image = upper0_image
    self.canvas_cube.itemconfig(self.upper0_image_id, image=upper0_image)

    upper1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper1_' + color_dict[upper[1]] + '.png'))
    self.upper1_image_id = self.canvas_cube.create_image(459, 141, image=upper1_image, anchor='center')
    self.upper1_image = upper1_image
    self.canvas_cube.itemconfig(self.upper1_image_id, image=upper1_image)

    upper2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper2_' + color_dict[upper[2]] + '.png'))
    self.upper2_image_id = self.canvas_cube.create_image(284, 140, image=upper2_image, anchor='center')
    self.upper2_image = upper2_image
    self.canvas_cube.itemconfig(self.upper2_image_id, image=upper2_image)

    upper3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'upper3_' + color_dict[upper[3]] + '.png'))
    self.upper3_image_id = self.canvas_cube.create_image(372, 185, image=upper3_image, anchor='center')
    self.upper3_image = upper3_image
    self.canvas_cube.itemconfig(self.upper3_image_id, image=upper3_image)

    # Cube Front Face
    front0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front0_' + color_dict[front[0]] + '.png'))
    self.front0_image_id = self.canvas_cube.create_image(215, 231, image=front0_image, anchor='center')
    self.front0_image = front0_image
    self.canvas_cube.itemconfig(self.front0_image_id, image=front0_image)

    front1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front1_' + color_dict[front[1]] + '.png'))
    self.front1_image_id = self.canvas_cube.create_image(315, 276, image=front1_image, anchor='center')
    self.front1_image = front1_image
    self.canvas_cube.itemconfig(self.front1_image_id, image=front1_image)

    front2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front2_' + color_dict[front[2]] + '.png'))
    self.front2_image_id = self.canvas_cube.create_image(215, 328, image=front2_image, anchor='center')
    self.front2_image = front2_image
    self.canvas_cube.itemconfig(self.front2_image_id, image=front2_image)

    front3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'front3_' + color_dict[front[3]] + '.png'))
    self.front3_image_id = self.canvas_cube.create_image(315, 373, image=front3_image, anchor='center')
    self.front3_image = front3_image
    self.canvas_cube.itemconfig(self.front3_image_id, image=front3_image)  

    # Cube Right Face
    right0_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right0_' + color_dict[right[0]] + '.png'))
    self.right0_image_id = self.canvas_cube.create_image(427, 276, image=right0_image, anchor='center')
    self.right0_image = right0_image
    self.canvas_cube.itemconfig(self.right0_image_id, image=right0_image)

    right1_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right1_' + color_dict[right[1]] + '.png'))
    self.right1_image_id = self.canvas_cube.create_image(528, 231, image=right1_image, anchor='center')
    self.right1_image = right1_image
    self.canvas_cube.itemconfig(self.right1_image_id, image=right1_image)

    right2_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right2_' + color_dict[right[2]] + '.png'))
    self.right2_image_id = self.canvas_cube.create_image(427, 373, image=right2_image, anchor='center')
    self.right2_image = right2_image
    self.canvas_cube.itemconfig(self.right2_image_id, image=right2_image)

    right3_image = ImageTk.PhotoImage(Image.open(os.getcwd() + '/Assets/Images/v1_' + 'right3_' + color_dict[right[3]] + '.png'))
    self.right3_image_id = self.canvas_cube.create_image(528, 328, image=right3_image, anchor='center')
    self.right3_image = right3_image
    self.canvas_cube.itemconfig(self.right3_image_id, image=right3_image)


def display2(self,upper,down,front,back,left,right):
    self.canvas_cube.delete(self.back0_image_id)