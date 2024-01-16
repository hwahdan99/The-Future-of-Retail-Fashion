from logging import root
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from sys import path
import serial
from PIL import Image
import time

def check_initial_state():
    ser_bytes = s.readline()
    decoded_ser_bytes = ser_bytes.decode("utf-8")
    # print("this is decoded ser bytes in outside")
    # print(decoded_ser_bytes.strip() == "Right")
    # time.sleep(1)
    if (decoded_ser_bytes.strip() == "Right"):
        # print("this is decoded ser bytes in if")
        # print(decoded_ser_bytes)
        master.destroy()
    else:
        print("this is decoded ser bytes in else")
        print(decoded_ser_bytes)
        master.after(0, check_initial_state)

def rotate_through_image():
    ser_bytes = s.readline()
    decoded_ser_bytes = ser_bytes.decode("utf-8")
    global root

    if (decoded_ser_bytes.strip() == "Right"):
        #Anytime there is a right, you increment counter by 1
        global counter
        counter += 1
        root.destroy()
    else:
        print("this is decoded ser bytes in else in rotation")
        print(decoded_ser_bytes)
        root.after(0, rotate_through_image)

def rotate_through_image1():
    ser_bytes = s.readline()
    decoded_ser_bytes = ser_bytes.decode("utf-8")
    global root1

    if (decoded_ser_bytes.strip() == "Right"):
        #Anytime there is a right, you increment counter by 1
        global counter
        counter += 1
        root1.destroy()
    else:
        print("this is decoded ser bytes in else in rotation1")
        print(decoded_ser_bytes)
        root1.after(0, rotate_through_image1)

def rotate_through_image2():
    ser_bytes = s.readline()
    decoded_ser_bytes = ser_bytes.decode("utf-8")
    global root2

    if (decoded_ser_bytes.strip() == "Right"):
        #Anytime there is a right, you increment counter by 1
        global counter
        counter += 1
        root2.destroy()
    else:
        print("this is decoded ser bytes in else in rotation2")
        print(decoded_ser_bytes)
        root2.after(0, rotate_through_image2)

def rotate_through_image3():
    ser_bytes = s.readline()
    decoded_ser_bytes = ser_bytes.decode("utf-8")
    global root3

    if (decoded_ser_bytes.strip() == "Right"):
        #Anytime there is a right, you increment counter by 1
        global counter
        counter += 1
        root3.destroy()
    else:
        print("this is decoded ser bytes in else in rotation3")
        print(decoded_ser_bytes)
        root3.after(0, rotate_through_image3)




s = serial.Serial(port='/dev/cu.usbmodem14601', baudrate=115200)
s.flushInput()
checkVariable = True
#Making ser_bytes and decoded_ser_bytes global variables
ser_bytes = 0
decoded_ser_bytes = 0

#ser_bytes = s.readline()
#decoded_ser_bytes = ser_bytes.decode("utf-8")
#dist = int(decoded_ser_bytes)

initial_state = 0

master = Tk()
master.wm_attributes('-fullscreen','true')
canvas_width, canvas_height = master.winfo_screenwidth(), master.winfo_screenheight()

canvas1 = Canvas(master, 
           width=canvas_width, 
           height=canvas_height,bg='black',highlightthickness=0)
canvas1.pack()

img2 = ImageTk.PhotoImage(Image.open("/Users/hanya_wahdan/Downloads/thesis-welcome.png"))
canvas1.create_image(1070,590, image=img2)
master.after(500, check_initial_state)
master.mainloop()


print("hello frienemy :)")
    # ser_bytes = s.readline()
    # decoded_ser_bytes = ser_bytes.decode("utf-8")
    # print(decoded_ser_bytes)

    # if (decoded_ser_bytes == "Right"):
    #     ser_bytes = s.readline()
    #     decoded_ser_bytes = ser_bytes.decode("utf-8")
    #     state = int(decoded_ser_bytes)
    #     print("This is state: \n")
    #     print(decoded_ser_bytes)



counter = -1


#Now that initial welcome screen is swiped through, rotate through outfits
while True:

    # This is the very first photo after initial state
    if (counter == -1):
        ser_bytes = s.readline()
        decoded_ser_bytes = ser_bytes.decode("utf-8")

        if (decoded_ser_bytes.strip() == "Right"):
            counter += 1
            state = counter % 3
            if (state == 0):
                print("first outfit")
                pilImage = Image.open("/Users/hanya_wahdan/Downloads/thesis-demo-photo-blue.png")

                root = Tk()
                root.wm_attributes('-fullscreen','true')
                canvas_width, canvas_height = root.winfo_screenwidth(), root.winfo_screenheight()

                # root.geometry("%dx%d+0+0" % (canvas_width, canvas_height))
                # root.focus_set()    
                # root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

                canvas_trial = Canvas(root, 
                        width=canvas_width, 
                        height=canvas_height,bg='black',highlightthickness=0)
                canvas_trial.pack()
                canvas_trial.configure(background='black')

                pilImage = pilImage.resize((1200,1200), Image.ANTIALIAS)

                #img = ImageTk.PhotoImage(Image.open("/Users/hanya_wahdan/Downloads/Hair_I_Want_To_Try.jpeg"))
                img = ImageTk.PhotoImage(pilImage)


                #canvas_trial.create_image(50,50, anchor=NW, image=img)
                canvas_trial.create_image(1100,650,image=img)

                root.after(500, rotate_through_image)

                root.mainloop()

            # else:
            #     print("second outfit")
    else:
        if(counter % 3 == 1):
            #second photo
            pilImage = Image.open("/Users/hanya_wahdan/Downloads/thesis-demo-photo-orange.png")

            root1 = Tk()
            root1.wm_attributes('-fullscreen','true')
            canvas_width, canvas_height = root1.winfo_screenwidth(), root1.winfo_screenheight()

            canvas_trial = Canvas(root1, 
                        width=canvas_width, 
                        height=canvas_height,bg='black',highlightthickness=0)
            canvas_trial.pack()
            #img1 = ImageTk.PhotoImage(Image.open("/Users/hanya_wahdan/Downloads/thesis-demo-photo-orange.png"))

            pilImage = pilImage.resize((1050,1050), Image.ANTIALIAS)
            
            img1 = ImageTk.PhotoImage(pilImage)

            canvas_trial.create_image(1080,575, image=img1)

            root1.after(500, rotate_through_image1)
            root1.mainloop()

        if(counter % 3 == 0):
            # first photo
            pilImage = Image.open("/Users/hanya_wahdan/Downloads/thesis-demo-photo-blue.png")

            root2 = Tk()
            root2.wm_attributes('-fullscreen','true')
            canvas_width, canvas_height = root2.winfo_screenwidth(), root2.winfo_screenheight()

            canvas_trial = Canvas(root2, 
                        width=canvas_width, 
                        height=canvas_height,bg='black',highlightthickness=0)
            canvas_trial.pack()
            canvas_trial.configure(background='black')

            pilImage = pilImage.resize((1200,1200), Image.ANTIALIAS)
            
            #img3 = ImageTk.PhotoImage(Image.open("/Users/hanya_wahdan/Downloads/Star_Trek_hello.jpeg"))
            img3 = ImageTk.PhotoImage(pilImage)


            #canvas_trial.create_image(200,200, anchor=NW, image=img3)
            canvas_trial.create_image(1100,650,image=img3)


            root2.after(500, rotate_through_image2)
            root2.mainloop()

        if(counter % 3 == 2):
            # first photo
            pilImage = Image.open("/Users/hanya_wahdan/Downloads/thesis-demo-photo.png")

            root3 = Tk()
            root3.wm_attributes('-fullscreen','true')
            canvas_width, canvas_height = root3.winfo_screenwidth(), root3.winfo_screenheight()

            canvas_trial = Canvas(root3, 
                        width=canvas_width, 
                        height=canvas_height,bg='black',highlightthickness=0)
            canvas_trial.pack()

            pilImage = pilImage.resize((1050,1050), Image.ANTIALIAS)

            img4 = ImageTk.PhotoImage(pilImage)


            canvas_trial.create_image(1070,590, image=img4)

            root3.after(500, rotate_through_image3)
            root3.mainloop()
