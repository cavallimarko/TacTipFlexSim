import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from numpy import argmax
cam = cv2.VideoCapture(1)#0-ta kamera
threshold=60
kernel_size=4
x_centar_kruga=0
y_centar_kruga=4
Oblik = [#V-visina,A-stranica,B-stranica,R-radijus,
        "FlatR100V0",
        "KvadarV10A9B27",
        "Polozena3StraaPrizmaV10A16B27",
        "ValjakR4V10",
        "ValjakR8V10",
]

img_width,img_height=640,480
target_img_width,target_img_height=320,240
dots=True
if dots:
    loaded_modelRealName='real'+'Dots'+'Model.h5'
    loaded_modelSimName='unreal'+'Dots'+'Model.h5'
else:
    loaded_modelRealName = 'realModel.h5'
    loaded_modelSimName = 'unrealModel.h5'
loaded_modelSim = load_model(loaded_modelSimName)
loaded_modelReal = load_model(loaded_modelRealName)
#loaded_model = load_model('model_h_V8.h5')
cv2.namedWindow('parametri')

#cap2 = cv2.VideoCapture('output.avi')#load video
w=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH ))#sirina
h=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT ))#visina

def nothing(x):
    pass

cv2.createTrackbar('threshold', 'parametri', threshold, 255, nothing)  # slider za threshold
cv2.createTrackbar('kernel_size', 'parametri', kernel_size, 10, nothing)  # slider za kernel
cv2.createTrackbar('x_centar_kruga', 'parametri', x_centar_kruga, 50, nothing)  # slider za threshold
cv2.createTrackbar('y_centar_kruga', 'parametri', y_centar_kruga, 50, nothing)  # slider za kernel
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
    cv2.circle(mask_circle, (round(cols / 2) +y_centar_kruga, round(rows / 2) + x_centar_kruga), 145, (255, 255, 255), -1)
    mask_circle = cv2.cvtColor(mask_circle, cv2.COLOR_BGR2GRAY)
    mask = cv2.bitwise_and(frame_gray_initial, frame_binary, mask=mask_circle)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # 3,3 za sample 4,4 za input1
    morph_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # dosta dobar
    #morph_open = morph_open[114:414, 182:482]
    ret, morph_open = cv2.threshold(morph_open, threshold, 255, cv2.THRESH_BINARY)
    global dots
    if dots is True:
        cnts = cv2.findContours(morph_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[1]
        dots = np.zeros((rows, cols, 1), np.uint8)
        # dots = cv2.cvtColor(cv2.zero(image), cv2.COLOR_GRAY2BGR)
        # loop over the contours
        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)
            if (M["m00"] != 0):
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # draw the contour and center of the shape on the image
                # print(cv2.contourArea(c))
                # cv2.drawContours(opening, [c], -1, (0, 255, 0), 2)
                cv2.circle(dots, (cX, cY), 4, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        return dots
    else:
        return  morph_open

while True:
    ret, frame =cam.read()#procitaj frame
    rows, cols, channels = frame.shape
    #cv2.imshow('frame', frame)
    morph_open=obrada_slike(frame)

    cv2.imshow('morph_open', morph_open)
    
    #predict
    img = cv2.resize(morph_open, (target_img_width, target_img_height))
    cv2.imshow('resized', img)
    cv2.imwrite('resized.png', img)
    img = img.astype("float") / 255.0
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)

    predictionSim=loaded_modelSim.predict(img)
    predictionReal=loaded_modelReal.predict(img)

    #(37-(visina+18)->19-ans
    udubljenjeReal=float(predictionReal[0])
    udubljenjeSim=float(predictionSim[0])

    print('Udubljenje Real= '+str(round(udubljenjeReal, 2))+' mm. '+"Unreal= "+str(round(udubljenjeSim, 2))+' mm'+" Razlika="+str(abs(udubljenjeReal-udubljenjeSim)))

    if cv2.waitKey(300) & 0xFF==ord('q'):#zatvori na tipku q
        break

cam.release()

cv2.destroyAllWindows()