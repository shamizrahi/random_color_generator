# Random Color Generator
# 

from hmcpng import *
import random


def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels


#Function # 1 - blank_image(height, width)

def blank_image(height, width):
    """that creates and returns a 2-D list of pixels 
    with height rows and width columns 
    """
    height = 3000
    width = 3000
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    
    return create_uniform_image(height, width, [r,g,b])
  


#Function # 2 - flip_horiz(pixels)

def org_image(pixels):
    """calls oiginal image
    """
    
    for r in pixels:
        for c in r:
            
            print(c, end='')
        print()                 #we need to create the 2_D list first or in this case image


 
    
    
###TEST CASES
if __name__ == '__main__':
    
        
    #test for diagonal_grid(height, width)
    
    
    for i in range(0, 5):
        pixels = blank_image(3000, 3000)
        imagename = 'random' + str(i) + '.png'
        print(imagename)
        save_pixels(pixels, imagename)
    
    

    
    
    

