import pyautogui
from PIL import Image
import argparse


parser = argparse.ArgumentParser(description='Try and draw a image with mouse movements')

parser.add_argument('file', type=str, help='The file to try replicate with mouse movements. Must be of a format that supports transparency such as png, otherwise you may get unexpected results')
parser.add_argument('-d', '--delay', type=float ,help='Amount of time between actions: mouse move, click, etc', default=0.001)
parser.add_argument('-i', '--inverted', action='store_true', help='Treat the blank pixels of the inputted image as filled in and the filled in pixels as blank pixels', default=False)

group = parser.add_mutually_exclusive_group()
group.add_argument('--click', action='store_true', help='Click every single pixel')
group.add_argument('--drag', action='store_true', help='Drag lines of pixels')

args = parser.parse_args()

if args.drag == False and args.click == False:
    print('Choose either --click or --drag drawing mode')
    exit()

pyautogui.PAUSE = args.delay

image = Image.open(args.file)
image_pixels = image.load()

starting_position = pyautogui.position()

if args.drag == True:                     #lllllcccclllllcccl
    for y in range(image.size[0]):        #111110000111110001
        for x in range(image.size[1]):
            if args.inverted:
                if image_pixels[x, y][3] != 0:
                    pyautogui.mouseUp(x=x+starting_position[0], y=y+starting_position[1])
                else:
                    pyautogui.mouseDown(x=x+starting_position[0], y=y+starting_position[1])
            else:
                if image_pixels[x, y][3] != 0:
                    pyautogui.mouseDown(x=x+starting_position[0], y=y+starting_position[1])
                else:
                    pyautogui.mouseUp(x=x+starting_position[0], y=y+starting_position[1])
        pyautogui.mouseUp()
    
    pyautogui.mouseUp() # This ensures that the mouse is not being held down after the drawing is done

else:
    for y in range(image.size[0]):
        for x in range(image.size[1]):
            if args.inverted:
                if image_pixels[x, y][3] == 0:
                    pyautogui.click(x+starting_position[0], y+starting_position[1])
            else:
                if image_pixels[x, y][3] != 0:
                    pyautogui.click(x+starting_position[0], y+starting_position[1])

