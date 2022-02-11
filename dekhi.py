from tkinter import *
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 800

root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.grid(row=0,column=0)

frame = Frame(root, bg='grey')
frame.place(relwidth=.5, relheight=.85)

global  my_label
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
   mimagg1 = mimagg1.resize((400,550), Image.ANTIALIAS)
mimagg1 = ImageTk.PhotoImage(mimagg1)
my_label = Label(frame, image=mimagg1)
my_label.grid(row=1,column=1)

text = Label(frame, text ='Complete robotic arm')
text.grid(row=2,column=1)

frame1 = Frame(root, bg='blue')
frame1.place(rely=.86, relwidth=.5, relheight=.14)

frame2 = Frame(root, bg='green')
frame2.place(relx=.51, relwidth=.49, relheight=1)

global text0
text0= Label(frame2,font=("Purisa"), text ='ROBOTIC ARM: There are four types of \n robotic arms according to there \n geometry. Rectangular, Cylindrical,Spherical\n and Jointed Spherical.'
'Jointed\n arm is used in the latest  \n Interplanetar rover "MONGOL-E V4.0"\n. Here we will see a description\n of different parts of the robotic \n'
'arm. The rover "MONGOL-E V4.0" \n can open a latch,drawer, pick up objects\n and place in the drawer and lift \n weight up to 7kg. To know\n'
'more about robotic arm  parts \n click the button on bottom left.')
text0.place(relwidth=1,relheight=1)

oc = StringVar(root)
oc.set('Click here for description of different components')

def function(x):
  global text0
  global my_label
  global text

  if x=="Click here for description of different components":
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
      text0= Label(frame2,font=("Purisa"),text='BASE: A servo motor is used in the\n base as the first rotation axis.\n It holds the sholder og the arm.\n The rotation of arm around the rover is \nperformed' 
'by the Base servo.\n Metallic disks are added to support\n the base and hold the shoulder.\n High torque motor is must because\n it is the main support' 
'componenet\n of the whole arm. The base\n also controls the upwards and downwards\n movement. ')
      text0.place(relwidth=1,relheight=1)

      my_label.grid_forget()
      text.grid_forget()

      my_label = Label(frame, image=image_list[1])
      my_label.grid(row=1, column=1)

      text = Label(frame, text='Base of the arm')
      text.grid(row=2, column=1)

  elif x == "SHOULDER":
      text0.grid_forget()
      text0= Label(frame2,font=("Purisa"),text='SHOULDER: This part connects the\n base and the elbow. The servo\n motors connected with the base\n controll the up down movement.\n Two motors are in the' 
'shoulder for \nside-to-side (horizontal) and up and \ndown (vertical) movements. The \n shoulder can move in the horizontal \n plane for about 160°. If the arm moved \n farther'
'from left to right, it \n would hit the front rocker-bogie "leg" \n portion of the wheel suspension.\n The shoulder can also move the arm\n through 70° in the vertical plane.')
      text0.place(relwidth=1,relheight=1)

      my_label.grid_forget()
      text.grid_forget()

      my_label = Label(frame, image=image_list[2])
      my_label.grid(row=1, column=1)

      text = Label(frame, text='Shoulder of the arm')
      text.grid(row=2, column=1)

  elif x == "ELBOW":
     text0.grid_forget()
     text0 = Label(frame2,font=("Purisa"), text='ELBOW: Elbow is the connection\n between shoulder and the wrist.\n It holds the two parts of thge arm\n The elbow is powered by another\n motor and can move through 290°,\n'
'folding the arm up or out.\n The controlling of this part must be\n precise. The motos must be powerful.\n The motor of elbow controls how high\n the rover can reach along'
'with\n the servo on the sholder')
     text0.place(relwidth=1,relheight=1)

     my_label.grid_forget()
     text.grid_forget()

     my_label = Label(frame, image=image_list[3])
     my_label.grid(row=1, column=1)

     text = Label(frame, text='Elbow of the arm')
     text.grid(row=2, column=1)

  elif x == "WRIST":
     text0.grid_forget()
     text0 = Label(frame2,font=("Purisa"), text='WRIST: Two motors reside in the\n wrist to twist the "handful" of instruments\n vertically and horizontally to place the\n chosen instrument perpendicular\n to the target surface. The' 
'wrist\n can rotate vertically through 340°,\n more motion than the human \n wrist. Functioning similar to a Lazy Susan,\n the turret handles the horizontal wrist\n rotation, and can spin' 
'through 350°.\n It controls the angles in which the\n grabbers are set and scientific analysis.\n It is controlled in the basis of the data\n received from the camera. ')
     text0.place(relwidth=1,relheight=1)

     my_label.grid_forget()
     text.grid_forget()

     my_label = Label(frame, image=image_list[4])
     my_label.grid(row=1, column=1)

     text = Label(frame, text='Wrist of the arm')
     text.grid(row=2, column=1)

  elif x == "GRIPPER":
     text0.grid_forget()
     text0 = Label(frame2,font=("Purisa"), text='GRIPPER: Gripper is the part of the\n rover that helps the rover catch things.\n It works as the hand, head and\n prime sensori and ractionary part\n of the rover. The rover has two \n'
'cameras held by the gripper. The\n gripper has two parts, They work as fingers.\n It helps to conduct scientific analysis.\n The mud samples that is necessary\n  for such activities are \n'
'collected by it. This part needs to be\n controlled properly for activities like\n opening latch and collecting objects. It\n also needs to be powerful to be able to\n collect heavy weights.'
'The two part\n can move independently. But to perform\n a task they need to be co-ordinated\n  properly. It can also send visual sensori \n response')
     text0.place(relwidth=1,relheight=1)

     my_label.grid_forget()
     text.grid_forget()

     my_label = Label(frame, image=image_list[5])
     my_label.grid(row=1, column=1)

     text = Label(frame, text='Gripper of the arm')
     text.grid(row=2, column=1)


o = OptionMenu(frame1, oc,"Click here for description of different components","BASE","SHOULDER","ELBOW","WRIST", "GRIPPER", command=function)
o.place(relheight=1,relwidth=1)

root.mainloop()
