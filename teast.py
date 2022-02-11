from tkinter import *
from tkinter import Canvas

from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 800

root = Tk()

global l,m

l=0
m=0

canvas: Canvas = Canvas(root, height=HEIGHT, width=WIDTH,bg='black')
canvas.grid(row=0, column=0)

canvas.create_line(740, 5, 800 ,30, fill='#c5f6fc') # create object to animate
canvas.create_line(660, 5, 800 ,70, fill='#c5f6fc') # create object to animate
canvas.create_line(560, 5, 800 ,110, fill='#c5f6fc') # create object to animate
canvas.create_line(475, 5, 800 ,150, fill='#c5f6fc') # create object to animate
canvas.create_line(390, 5, 800 ,190, fill='#c5f6fc') # create object to animate
canvas.create_line(285, 5, 800 ,230, fill='#c5f6fc') # create object to animate
canvas.create_line(180, 5, 800 ,270, fill='#c5f6fc') # create object to animate
canvas.create_line(75, 0, 800 ,310, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 5, 800 ,350, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 45, 800 ,390, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 85, 800 ,430, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 125, 800 ,470, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 165, 800 ,510, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 205, 800 ,550, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 245, 800 ,590, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 285, 800 ,630, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 325, 800 ,710, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 365, 800 ,750, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 405, 800 ,790, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 445, 800 ,830, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 485, 800 ,870, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 525, 800 ,910, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 565, 800 ,950, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 605, 800 ,990, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 645, 800 ,1030, fill='#c5f6fc') # create object to animate
canvas.create_line(0, 685, 800 ,1070, fill='#c5f6fc') # create object to animate

ball = canvas.create_oval(50, 50, 170, 170, tags='ball', fill='#f26711')  # create object to animate
ball2 = canvas.create_oval(735, 150, 795 , 250, tags='ball', fill='#f26711')  # create object to animate
t = canvas.create_text(110, 110, font=("Purisa"), text='Rover Views', fill='white')
t2 = canvas.create_text(767, 195, text='welcome', fill='white')

global frame2

frame2 = Frame(root,bg='red')
frame2.place(relx=.9,rely=.85,relwidth = .10, relheight = .15)

i = Image.open('buskett.jpg')
if i.size != (80,15):
    i = i.resize((80,155), Image.ANTIALIAS)
i = ImageTk.PhotoImage(i)
my_label = Label(frame2, image=i)
my_label.grid(row=1, column=1)


# ball1 = canvas.create_oval(50, 50, 70, 70, tags = 'ball1', fill = 'red') # create object to animate

global k
global I
I = Image.open('logo-2.png')
if I.size != (80, 105):
    I = I.resize((80, 105), Image.ANTIALIAS)
I = ImageTk.PhotoImage(I)

k=0

def animation(bal, t, x_move, y_move):
    global l, m
    canvas.move(bal, x_move, y_move)
    canvas.move(t, x_move, y_move)
    # canvas.update()
    # canvas.after(5) # milliseconds in wait time, this is 50 fps
    l = l + 1
    # print(x_move, l)
    # root.after_idle(animation, bal,t, x_move, y_move) # loop variables and animation, these are updatable variables
    if l == 300 and m % 2 == 0:
        x_move = -2
        l = 0
        m = m + 1
    elif l == 300 and m % 2 == 1:
        x_move = 2
        l = 0
        m = m + 1
    canvas.after(10, animation, bal, t, x_move, y_move)

def animation2(bal,t ,x_move, y_move):
    global k,my_label,I
    canvas.move(bal, x_move, y_move)
    canvas.move(t, x_move, y_move)

    k=k+1
    print(k)

    if k>=200 :
        my_label.grid_forget()
        my_labe = Label(frame2, image=I)
        my_labe.place(relwidth=1,relheight=1)


    canvas.after(10, animation2, bal,t, x_move, y_move)



animation(ball, t, 2, 0)
animation2(ball2,t2, 0, 2)

frame = Frame(root, bg='#f26711')
frame.place(relx=.09, rely=.25, relwidth=.77, relheight=.6)

mimagg1 = ImageTk.PhotoImage(Image.open('a1.jpg'))
mimagg2 = ImageTk.PhotoImage(Image.open('a2.jpg'))
mimagg3 = ImageTk.PhotoImage(Image.open('a3.jpg'))

image_list = [mimagg1, mimagg2, mimagg3]

my_label = Label(frame, image=mimagg1)
my_label.place(relwidth=1, relheight=1)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(frame, image=image_list[image_number - 1])
    button_forward = Button(frame, text="Next", bg='#f26711', fg='white', command=lambda: forward(image_number + 1))
    button_back = Button(frame, text="Back", bg='#f26711', fg='white', command=lambda: back(image_number - 1))

    if image_number == 3:
        button_forward = Button(frame, text="Next", bg='#f26711', state=DISABLED)

    my_label.place(relwidth=1, relheight=1)
    button_back.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()

    my_label = Label(frame, image=image_list[image_number - 1])
    button_forward = Button(frame, text="Next", bg='#f26711', fg='white', command=lambda: forward(image_number + 1))
    button_back = Button(frame, text="Back", bg='#f26711', fg='white', command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(frame, text="Back", bg='#f26711', state=DISABLED)

    my_label.place(relwidth=1, relheight=1)
    button_back.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


button_back = Button(frame, text="Back", bg='#f26711', fg='white', command=lambda: back(1))
button_forward = Button(frame, text="Next", bg='#f26711', fg='white', command=lambda: forward(2))

button_back.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# background_image = PhotoImage('background.jpg')
# background_label = Label(root, image = background_image)
# background_label.grid.(relwidth=1, relheight = 1)

root.mainloop()