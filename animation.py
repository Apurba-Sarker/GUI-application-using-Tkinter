from tkinter import * # version 3.x

HEIGHT = 700
WIDTH = 800
l=0
m=0

root = Tk()

canvas = Canvas(root,height = HEIGHT, width = WIDTH)
canvas.grid(row=0,column=0)
#frame.pack(fill = BOTH, expand = 1)
#canvas.pack(fill = BOTH, expand = 1)

ball = canvas.create_oval(50, 50, 170, 170, tags = 'ball', fill = 'orange') # create object to animate
t = canvas.create_text(110,110,font=("Purisa"),text='Rover Views',fill ='gray')
#ball1 = canvas.create_oval(50, 50, 70, 70, tags = 'ball1', fill = 'red') # create object to animate



def animation(bal, t, x_move, y_move):
    global l,m
    canvas.move(bal, x_move, y_move)
    canvas.move(t, x_move, y_move)
    #canvas.update()
    #canvas.after(5) # milliseconds in wait time, this is 50 fps
    l=l+1
    #print(x_move, l)
    #root.after_idle(animation, bal,t, x_move, y_move) # loop variables and animation, these are updatable variables
    if l==300 and m%2==0:
        x_move=-2
        l=0
        m=m+1
    elif l==300 and m%2==1 :
        x_move = 2
        l=0
        m=m+1
    canvas.after(10, animation,bal,t, x_move, y_move)



animation(ball,t,2,0)

print(1)
#animation(ball1,2,30)
root.mainloop()