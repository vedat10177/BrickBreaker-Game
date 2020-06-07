"""
File: brickbreaker.py
----------------
YOUR DESCRIPTION HERE
"""

import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 650     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 10            # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING ) / N_COLS

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Break')
    for row in range(10):
        for col in range(10):
            draw_brick(canvas,col,row)


    ball = make_ball(canvas)
    paddle = canvas.create_rectangle(10,PADDLE_Y,PADDLE_WIDTH,PADDLE_Y+30,fill = "red")

    dx = -10
    dy = -10

    while True:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle,mouse_x-(PADDLE_WIDTH/2),PADDLE_Y)



        canvas.move(ball,dx,dy)
        if hit_left_wall(canvas,ball) or hit_right_wall(canvas, ball) :
            dx *= -1
        if hit_top_wall(canvas,ball) :
            dy *= -1
        if hit_bottom(canvas,ball):
            canvas.create_rectangle(40,200,550,450, fill= 'black')
            canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text="Game is over! ",
                               fill='white', font="Arial 45 bold", anchor="s")
        if hit_paddle(canvas,ball,paddle):
            dy *= -1

        elif hit_brick(canvas,ball,paddle):
            dy *= -1


        canvas.update()
        time.sleep(1/30)

    canvas.mainloop()


def hit_brick(canvas,ball,paddle):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    x2 = ball_coords[1]
    x3 = ball_coords[2]
    x4 = ball_coords[3]
    results = canvas.find_overlapping(x1,x2,x3,x4)
    if len(results) >1:
         for obj in results:
            if obj !=paddle:
                canvas.delete(obj)
                return results
            else:
                return None

def hit_paddle(canvas,ball,paddle):
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    x2 = paddle_coords[1]
    x3 = paddle_coords[2]
    x4 = paddle_coords[3]
    results = canvas.find_overlapping(x1,x2,x3,x4)
    return len(results) >1

def hit_right_wall(canvas, ball) :
    return canvas.coords(ball)[2] >= CANVAS_WIDTH
def hit_left_wall(canvas,ball):
    return get_left_x(canvas,ball) <= 0
def hit_top_wall(canvas,ball):
    return get_top_y(canvas,ball) <= 0
def hit_bottom(canvas,ball):
    return get_top_y(canvas,ball) >= CANVAS_HEIGHT



def make_ball(canvas):
    x1 = 300 - BALL_SIZE/2
    y1 = 400 - BALL_SIZE/2
    x2 = x1 + BALL_SIZE
    y2 = y1 + BALL_SIZE
    ball = canvas.create_oval(x1,y1,x2,y2 , fill = "blue")
    return ball

def draw_brick(canvas,col,row):
    x0 = col * (BRICK_WIDTH + SPACING)
    y0 = BRICK_START_Y + (BRICK_HEIGHT + SPACING) * row
    x1 = col * (BRICK_WIDTH + SPACING) + BRICK_WIDTH
    y1 = BRICK_START_Y + (BRICK_HEIGHT + SPACING) * row + BRICK_HEIGHT
    color1 = get_color(row)
    brick = canvas.create_rectangle(x0, y0, x1, y1, fill= color1)

def get_color(row):
    if row == 0 or row == 1 :
        return 'red'
    elif row == 2 or row == 3:
        return 'orange'
    elif row== 4 or row == 5:
        return 'yellow'
    elif row== 6 or row == 7:
        return 'green'
    else:
        return 'cyan'


def get_top_y(canvas, ball):
    '''
    This friendly method returns the y coordinate of the top of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    '''
    return canvas.coords(ball)[1]

def get_left_x(canvas, ball):
    '''
    This friendly method returns the x coordinate of the left of an object.
    Recall that canvas.coords(object) returns a list of the object 
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    '''
    return canvas.coords(ball)[0]

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
