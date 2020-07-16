from tkinter import *
import cv2
import numpy as np
import csv

brojac=1
threshold=60
kernel_size=4
x_centar_kruga=0
y_centar_kruga=4
cam = cv2.VideoCapture(1)
ret, frame = cam.read()
rows, cols, channels = frame.shape

def nothing(x):
    pass
cv2.namedWindow('parametri')
cv2.createTrackbar('threshold', 'parametri', threshold, 255, nothing)  # slider za threshold
cv2.createTrackbar('kernel_size', 'parametri', kernel_size, 10, nothing)  # slider za kernel
cv2.createTrackbar('x_centar_kruga', 'parametri', x_centar_kruga, 50, nothing)  # slider za threshold
cv2.createTrackbar('y_centar_kruga', 'parametri', y_centar_kruga, 50, nothing)  # slider za kernel
root=Tk()
f = open('csvfile.csv','w')
Oblik = [#V-visina,A-stranica,B-stranica,R-radijus,
"FlatR100V0",
"KvadarV10A9B27",
"PiramidaV10A14",
"Polozena3StranaPrizmaV5A16B27",
"Polozena3StranaPrizmaV10A16B27",
"PolozeniValjakR8B27",
"PoluSferaR12",
"StozacR12V10",
"ValjakR4V10",
"ValjakR8V10",

]
def OptionMenu_SelectionEvent(event):
   global brojac
   brojac=1

variable = StringVar(root)
variable.set(Oblik[0])  # default value

w = OptionMenu(root, variable, *Oblik,command=OptionMenu_SelectionEvent)
w.pack()
def save():
    global brojac
    oblik=variable.get()
    visina=E1.get()
    zapis=visina+"_"+oblik
    print ("Visina[mm]: "+visina+" Oblik:" + variable.get()+" Redni broj: "+str(brojac))
    f.write(visina+","+oblik+"\n")  # Give your csv text here.
    image_save(zapis.split("_")[1],visina)
def obrada_slike(frame):
    threshold = cv2.getTrackbarPos('threshold', 'parametri')
    kernel_size = cv2.getTrackbarPos('kernel_size', 'parametri')
    x_centar_kruga = cv2.getTrackbarPos('x_centar_kruga', 'parametri')
    y_centar_kruga = cv2.getTrackbarPos('y_centar_kruga', 'parametri')

    rotationMatrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 29, 1)  # rotacija
    frame = cv2.warpAffine(frame, rotationMatrix, (cols, rows))
    frame_gray_initial = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_gray = cv2.equalizeHist(frame_gray_initial)  # histogram contrast
    ret, frame_binary = cv2.threshold(frame_gray, threshold, 255,cv2.THRESH_BINARY)
    mask_circle = np.zeros((rows, cols, 3), np.uint8)  # maska krug
    cv2.circle(mask_circle, (round(cols / 2) +y_centar_kruga, round(rows / 2) + x_centar_kruga), 140, (255, 255, 255), -1)
    mask_circle = cv2.cvtColor(mask_circle, cv2.COLOR_BGR2GRAY)
    mask = cv2.bitwise_and(frame_gray_initial, frame_binary, mask=mask_circle)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # 3,3 za sample 4,4 za input1
    morph_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # dosta dobar
    #morph_open = morph_open[114:414, 182:482]
    ret, morph_open = cv2.threshold(morph_open, threshold, 255, cv2.THRESH_BINARY)
    return  morph_open

def image_save(oblik,visina):
    global brojac
    ret, frame = cam.read()
    #cv2.imshow('frame', frame)
    morph_open=obrada_slike(frame)


    cv2.imwrite('DatasetReal/'+oblik+'/'+str(brojac)+"_"+oblik+'_0_'+str(visina)+'.png', morph_open)  # spremanje slike
    brojac+=1
def video():
    ret, frame = cam.read()
    cv2.imshow('frame', obrada_slike(frame))
    root.after(100, video)
L1 = Label(root, text="Visina")
L1.pack()
E1 = Entry(root, bd =2)
E1.pack()

button = Button(root, text="Spremi", command=save)
button.pack()
video()
mainloop()
f.close()