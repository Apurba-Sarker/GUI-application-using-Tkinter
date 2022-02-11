from tkinter import *
from PIL import ImageTk,Image

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Setup Menu
        MainMenu(self)
        # Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Start Page", bg ='#79b0b5')
        label.grid(row=0,column=0)
        page_one = Button(self, text="Page One", bg ='#79b0b5', command=lambda:controller.show_frame(PageOne))
        page_one.grid(row=0,column=1)
        page_two = Button(self, text="Page Two", bg ='#79b0b5', command=lambda:controller.show_frame(PageTwo))
        page_two.grid(row=0,column=2)

        canvas = Canvas(self, height=700, width=800, bg='#546770')
        canvas.grid(row=1, columnspan=3)

        global p
        global q

        p = 0
        q = 0

        ball = canvas.create_oval(50, 50, 170, 170, tags='ball', fill='#f26711')  # create object to animate
        t = canvas.create_text(110, 110, font=("Purisa"), text='Rover Views', fill='white')

        def animation(bal, t, x_move, y_move):
            global p, q
            canvas.move(bal, x_move, y_move)
            canvas.move(t, x_move, y_move)
            # canvas.update()
            # canvas.after(5) # milliseconds in wait time, this is 50 fps
            p = p + 1
            # print(x_move, l)
            # root.after_idle(animation, bal,t, x_move, y_move) # loop variables and animation, these are updatable variables
            if p == 300 and q % 2 == 0:
                x_move = -2
                p = 0
                q = q + 1
            elif p == 300 and q % 2 == 1:
                x_move = 2
                p = 0
                q = q + 1
            canvas.after(10, animation, bal, t, x_move, y_move)

        animation(ball, t, 2, 0)
        frame = Frame(canvas, bg='gray')
        frame.place(relx=.10, rely=.25, relwidth=.75, relheight=.6)
        mimagg1 = ImageTk.PhotoImage(Image.open('a1.jpg'))
        mimagg2 = ImageTk.PhotoImage(Image.open('a2.jpg'))
        mimagg3 = ImageTk.PhotoImage(Image.open('a3.jpg'))

        image_list = [mimagg1, mimagg2, mimagg3]

        global my_label
        my_label = Label(frame, image=mimagg1)
        my_label.place(relx=.1,rely=.1,relwidth=.8, relheight=.8)

        def forward(image_number):
            global my_label
            global button_forward
            global button_back

            my_label.grid_forget()
            my_label = Label(frame, image=image_list[image_number - 1])
            button_forward = Button(frame, text="Next", bg='#f26711', fg='white',
                                    command=lambda: forward(image_number + 1))
            button_back = Button(frame, text="Back", bg='#f26711', fg='white', command=lambda: back(image_number - 1))

            if image_number == 3:
                button_forward = Button(frame, text="Next", bg='#f26711', state=DISABLED)

            my_label.place(relx=.1,rely=.1,relwidth=.8, relheight=.8)
            button_back.grid(row=1, column=1)
            button_forward.grid(row=1, column=2)

        def back(image_number):
            global my_label
            global button_forward
            global button_back
            my_label.grid_forget()

            my_label = Label(frame, image=image_list[image_number - 1])
            button_forward = Button(frame, text="Next", bg='#f26711', fg='white',
                                    command=lambda: forward(image_number + 1))
            button_back = Button(frame, text="Back", bg='#f26711', fg='white', command=lambda: back(image_number - 1))

            if image_number == 1:
                button_back = Button(frame, text="Back", bg='#f26711', state=DISABLED)

            my_label.place(relx=.1,rely=.1,relwidth=.8, relheight=.8)
            button_back.grid(row=1, column=1)
            button_forward.grid(row=1, column=2)


        button_back = Button(frame, text="Back", bg='#f26711', fg='white', command=lambda: back(1))
        button_forward = Button(frame, text="Next", bg='#f26711', fg='white', command=lambda: forward(2))

        button_back.grid(row=1, column=1)
        button_forward.grid(row=1, column=2)


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page One", bg ='#79b0b5')
        label.grid(row=0,column=0)
        start_page = Button(self, text="Start Page", bg ='#79b0b5', command=lambda: controller.show_frame(StartPage))
        start_page.grid(row=0,column=1)
        page_two = Button(self, text="Page Two", bg ='#79b0b5', command=lambda: controller.show_frame(PageTwo))
        page_two.grid(row=0,column=2)

        canvas = Canvas(self, height=700, width=800, bg='#546770')
        canvas.grid(row=1, columnspan=3)

        frame = Frame(canvas, bg='#f26107')
        frame.place(relwidth=.5, relheight=.85)

        global my_label
        global text

        mimagg1 = Image.open('arm.jpg')
        mimagg2 = Image.open('base.jpg')
        mimagg3 = Image.open('shoulder.png')
        mimagg4 = Image.open('elbow.png')
        mimagg5 = Image.open('wrist.png')
        mimagg6 = Image.open('griper.jpg')

        image_list = [mimagg1, mimagg2, mimagg3, mimagg4, mimagg5, mimagg6]

        for P in range(6):
            if image_list[P] != (400, 550):
                image_list[P] = image_list[P].resize((400, 550), Image.ANTIALIAS)
            image_list[P] = ImageTk.PhotoImage(image_list[P])

        if mimagg1.size != (400, 550):
            mimagg1 = mimagg1.resize((400, 550), Image.ANTIALIAS)
        mimagg1 = ImageTk.PhotoImage(mimagg1)
        my_label = Label(frame, image=mimagg1)
        my_label.grid(row=1, column=1)

        text = Label(frame, text='Complete robotic arm')
        text.grid(row=2, column=1)

        frame1 = Frame(canvas, bg='blue')
        frame1.place(rely=.86, relwidth=.5, relheight=.14)

        frame2 = Frame(canvas, bg='green')
        frame2.place(relx=.51, relwidth=.49, relheight=1)
        global text0
        text0 = Label(frame2, font=("Purisa"),
                      text='ROBOTIC ARM: There are four types of \n robotic arms according to there \n geometry. Rectangular, Cylindrical,Spherical\n and Jointed Spherical.'
                           'Jointed\n arm is used in the latest  \n Interplanetar rover "MONGOL-E V4.0"\n. Here we will see a description\n of different parts of the robotic \n'
                           'arm. The rover "MONGOL-E V4.0" \n can open a latch,drawer, pick up objects\n and place in the drawer and lift \n weight up to 7kg. To know\n'
                           'more about robotic arm  parts \n click the button on bottom left.')
        text0.place(relwidth=1, relheight=1)

        oc = StringVar(self)
        oc.set('Click here for description of different components')

        def function(x):
            global text0
            global my_label
            global text

            if x == "Click here for description of different components":
                text0.grid_forget()
                text0 = Label(frame2, font=("Purisa"),
                              text='ROBOTIC ARM: There are four types of \n robotic arms according to there \n geometry. Rectangular, Cylindrical,Spherical\n and Jointed Spherical.'
                                   'Jointed\n arm is used in the latest  \n Interplanetar rover "MONGOL-E V4.0"\n. Here we will see a description\n of different parts of the robotic \n'
                                   'arm. The rover "MONGOL-E V4.0" \n can open a latch,drawer, pick up objects\n and place in the drawer and lift \n weight up to 7kg. To know\n'
                                   'more about robotic arm  parts \n click the button on bottom left.')
                text0.place(relwidth=1, relheight=1)

                my_label.grid_forget()
                text.grid_forget()

                my_label = Label(frame, image=mimagg1)
                my_label.grid(row=1, column=1)

                text = Label(frame, text='Complete robotic arm')
                text.grid(row=2, column=1)


            elif x == "BASE":
                text0.grid_forget()
                text0 = Label(frame2, font=("Purisa"),
                              text='BASE: A servo motor is used in the\n base as the first rotation axis.\n It holds the sholder og the arm.\n The rotation of arm around the rover is \nperformed'
                                   'by the Base servo.\n Metallic disks are added to support\n the base and hold the shoulder.\n High torque motor is must because\n it is the main support'
                                   'componenet\n of the whole arm. The base\n also controls the upwards and downwards\n movement. ')
                text0.place(relwidth=1, relheight=1)

                my_label.grid_forget()
                text.grid_forget()

                my_label = Label(frame, image=image_list[1])
                my_label.grid(row=1, column=1)

                text = Label(frame, text='Base of the arm')
                text.grid(row=2, column=1)

            elif x == "SHOULDER":
                text0.grid_forget()
                text0 = Label(frame2, font=("Purisa"),
                              text='SHOULDER: This part connects the\n base and the elbow. The servo\n motors connected with the base\n controll the up down movement.\n Two motors are in the'
                                   'shoulder for \nside-to-side (horizontal) and up and \ndown (vertical) movements. The \n shoulder can move in the horizontal \n plane for about 160°. If the arm moved \n farther'
                                   'from left to right, it \n would hit the front rocker-bogie "leg" \n portion of the wheel suspension.\n The shoulder can also move the arm\n through 70° in the vertical plane.')
                text0.place(relwidth=1, relheight=1)

                my_label.grid_forget()
                text.grid_forget()

                my_label = Label(frame, image=image_list[2])
                my_label.grid(row=1, column=1)

                text = Label(frame, text='Shoulder of the arm')
                text.grid(row=2, column=1)

            elif x == "ELBOW":
                text0.grid_forget()
                text0 = Label(frame2, font=("Purisa"),
                              text='ELBOW: Elbow is the connection\n between shoulder and the wrist.\n It holds the two parts of thge arm\n The elbow is powered by another\n motor and can move through 290°,\n'
                                   'folding the arm up or out.\n The controlling of this part must be\n precise. The motos must be powerful.\n The motor of elbow controls how high\n the rover can reach along'
                                   'with\n the servo on the sholder')
                text0.place(relwidth=1, relheight=1)

                my_label.grid_forget()
                text.grid_forget()

                my_label = Label(frame, image=image_list[3])
                my_label.grid(row=1, column=1)

                text = Label(frame, text='Elbow of the arm')
                text.grid(row=2, column=1)

            elif x == "WRIST":
                text0.grid_forget()
                text0 = Label(frame2, font=("Purisa"),
                              text='WRIST: Two motors reside in the\n wrist to twist the "handful" of instruments\n vertically and horizontally to place the\n chosen instrument perpendicular\n to the target surface. The'
                                   'wrist\n can rotate vertically through 340°,\n more motion than the human \n wrist. Functioning similar to a Lazy Susan,\n the turret handles the horizontal wrist\n rotation, and can spin'
                                   'through 350°.\n It controls the angles in which the\n grabbers are set and scientific analysis.\n It is controlled in the basis of the data\n received from the camera. ')
                text0.place(relwidth=1, relheight=1)

                my_label.grid_forget()
                text.grid_forget()

                my_label = Label(frame, image=image_list[4])
                my_label.grid(row=1, column=1)

                text = Label(frame, text='Wrist of the arm')
                text.grid(row=2, column=1)

            elif x == "GRIPPER":
                text0.grid_forget()
                text0 = Label(frame2, font=("Purisa"),
                              text='GRIPPER: Gripper is the part of the\n rover that helps the rover catch things.\n It works as the hand, head and\n prime sensori and ractionary part\n of the rover. The rover has two \n'
                                   'cameras held by the gripper. The\n gripper has two parts, They work as fingers.\n It helps to conduct scientific analysis.\n The mud samples that is necessary\n  for such activities are \n'
                                   'collected by it. This part needs to be\n controlled properly for activities like\n opening latch and collecting objects. It\n also needs to be powerful to be able to\n collect heavy weights.'
                                   'The two part\n can move independently. But to perform\n a task they need to be co-ordinated\n  properly. It can also send visual sensori \n response')
                text0.place(relwidth=1, relheight=1)

                my_label.grid_forget()
                text.grid_forget()

                my_label = Label(frame, image=image_list[5])
                my_label.grid(row=1, column=1)

                text = Label(frame, text='Gripper of the arm')
                text.grid(row=2, column=1)

        o = OptionMenu(frame1, oc, "Click here for description of different components", "BASE", "SHOULDER", "ELBOW",
                       "WRIST", "GRIPPER", command=function)
        o.place(relheight=1, relwidth=1)


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page Two", bg ='#79b0b5')
        label.grid(row=0, column=0)
        start_page = Button(self, text="Start Page", bg ='#79b0b5', command=lambda: controller.show_frame(StartPage))
        start_page.grid(row=0, column=1)
        page_one = Button(self, text="Page One", bg ='#79b0b5', command=lambda: controller.show_frame(PageOne))
        page_one.grid(row=0, column=2)

        canvas = Canvas(self, height=700, width=800, bg='#546770')
        canvas.grid(row=1,columnspan = 3)

        global frame1
        global x
        global l
        global L
        global m
        global n

        x = 0
        l = 0
        L = 0
        m = 0
        n = 0

        texts = Label(canvas, text = 'Click the image for informations about me', bg ='#79b0b5')
        texts.place(relheight =.04)

        image = Image.open('me.jpg')

        if image.size != (640, 560):
            image = image.resize((640, 560), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(image)

        def text():
            global frame1
            global x
            if x % 2 == 0:
                frame1.grid_forget()
                frame1 = Button(canvas, font=("Purisa"),
                                text='Hello!!! My name is Apurba Sarker.\n I am currently a student of BUET,\n Mechanical Engineering Department ,\n batch-18. My home town is in'
                                     'Mymensingh.\n My school life was in Mymensingh\n Zilla School and college in Anandamohan\n College. From my childhood I was\n interested in'
                                     'robots. I felt very fascinated\n watching robots work. Completing\n this project was very fun.\n Thank you very much',
                                command=text)
                frame1.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)
                x = x + 1

            elif x % 2 == 1:
                frame1.grid_forget()
                frame1 = Button(canvas, image=image, command=text)
                frame1.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)
                x = x + 1

        r1 = canvas.create_rectangle(50, 50, 170, 170, tags='ball', fill='#f26711')
        r2 = canvas.create_rectangle(50, 550, 170, 670, tags='ball', fill='#f26711')
        r3 = canvas.create_rectangle(630, 48, 750, 170, tags='ball', fill='#f26711')
        r4 = canvas.create_rectangle(630, 550, 750, 670, tags='ball', fill='#f26711')

        R1 = canvas.create_rectangle(50, 50, 170, 170, tags='ball', fill='gray')
        R2 = canvas.create_rectangle(50, 550, 170, 670, tags='ball', fill='gray')
        R3 = canvas.create_rectangle(630, 48, 750, 170, tags='ball', fill='gray')
        R4 = canvas.create_rectangle(630, 550, 750, 670, tags='ball', fill='gray')

        frame1 = Button(canvas, image=image, command=text)
        frame1.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)

        def animation(bal, bal1, bal2, bal3, x_move1, y_move1, x_move2, y_move2, x_move3, y_move3, x_move4, y_move4):
            global l
            global m
            canvas.move(bal, x_move1, y_move1)
            canvas.move(bal1, x_move2, -y_move2)
            canvas.move(bal2, x_move3, y_move3)
            canvas.move(bal3, x_move4, -y_move4)

            l = l + 1
            # print(l)

            if l == 130:
                y_move1 = -y_move1
                y_move2 = -y_move2
                y_move3 = -y_move3
                y_move4 = -y_move4
                l = 0
                m = m + 1
                if (m == 2):
                    return

            canvas.after(10, animation, bal, bal1, bal2, bal3, x_move1, y_move1, x_move2, y_move2, x_move3, y_move3,
                         x_move4, y_move4)

        def animation2(bal, bal1, bal2, bal3, x_move1, y_move1, x_move2, y_move2, x_move3, y_move3, x_move4, y_move4):
            global L
            global n
            canvas.move(bal, x_move1, y_move1)
            canvas.move(bal1, x_move2, y_move2)
            canvas.move(bal2, -x_move3, y_move3)
            canvas.move(bal3, -x_move4, y_move4)

            L = L + 1
            # print(L)

            if L == 130:
                x_move1 = -x_move1
                x_move2 = -x_move2
                x_move3 = -x_move3
                x_move4 = -x_move4
                L = 0
                n = n + 1
                if (n == 2):
                    return

            canvas.after(10, animation2, bal, bal1, bal2, bal3, x_move1, y_move1, x_move2, y_move2, x_move3, y_move3,
                         x_move4, y_move4)

        animation(r1, r2, r3, r4, 0, 2, 0, 2, 0, 2, 0, 2)
        animation(r1, r2, r3, r4, 0, 2, 0, 2, 0, 2, 0, 2)
        animation2(R1, R2, R3, R4, 2, 0, 2, 0, 2, 0, 2, 0)
        animation2(R1, R2, R3, R4, 2, 0, 2, 0, 2, 0, 2, 0)


class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="Exit Program", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.mainloop()
