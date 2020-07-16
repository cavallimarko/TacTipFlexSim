import random
from tkinter import *
import cv2
import numpy as np
import csv
import glob
def compareTwoImages(img1,img2):
	#img1=cv2.imread("DatasetSim/0_edgeprobe_0_0.0.png")
	(rows,cols,channels) = img1.shape
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	ret, img1 = cv2.threshold(img1, 40, 255,cv2.THRESH_BINARY)
	ret, img2 = cv2.threshold(img2, 40, 255,cv2.THRESH_BINARY)
	#img2=cv2.imread("DatasetReal/FlatR100V0/0_FlatR100V0_1.png")
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	numpy_horizontal_concat = np.concatenate((img1, img2), axis=1)
	img3=img2-img1
	numpy_vertical_concat = np.concatenate((numpy_horizontal_concat, img3), axis=1)

	cv2.imshow('Numpy Horizontal Concat', numpy_vertical_concat)
	diff = compareimages(img1, img2)
	print ("Total distance between centroids= " +str(diff))
	diffInPixels =np.sum(img3 ) /255
	print("Number of different pixels=  " +str(diffInPixels))

	print("Image difference= " +str(round(diffInPixels /(rows *cols ) *100 ,2) ) +"%")

def findCentroids(image,height,saveFolder):
	(rows, cols) = image.shape
	points=[]
	# find contours in the thresholded image
	cnts = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[1]
	opening = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
	dots=np.zeros((rows, cols, 1), np.uint8)
	#dots = cv2.cvtColor(cv2.zero(image), cv2.COLOR_GRAY2BGR)
	# loop over the contours
	for c in cnts:
		# compute the center of the contour
		M = cv2.moments(c)
		if (M["m00"] != 0):
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])

			# draw the contour and center of the shape on the image
			#print(cv2.contourArea(c))
			#cv2.drawContours(opening, [c], -1, (0, 255, 0), 2)
			cv2.circle(dots, (cX, cY), 4, (255, 255, 255), -1, lineType=cv2.LINE_AA)
			cv2.circle(opening, (cX, cY), 2, (255, 255, 255), -1, lineType=cv2.LINE_AA)

			points.append((cX, cY))
	#print(points)
	cv2.imshow("dots"+str(points[0][0]), dots)
	if(height is not -1):
		cv2.imwrite(saveFolder+"/" + str(random.randint(0,1000))+"_"+saveFolder+ "_0_"+str(height) + ".png", dots)
		print("saving dots"+str(height))
	return np.array(points)

def compareimages(image1,image2):
	points1=findCentroids(image1,-1,0)
	points2=findCentroids(image2,-1,0)
	sum=0
	minDistance=10000
	for i in range(len(points1)):
		sum+=findnearestNeighbourDistance(points1[i],points2)
	return sum
def findnearestNeighbourDistance(point1,points2):
	nearestpoint=points2[0]
	minDistance=100000;
	for j in range(len(points2)):
		if(euclideanPointDistance(point1, points2[j])<minDistance):
			minDistance=euclideanPointDistance(point1, points2[j])
			nearestpoint=points2[j]
	#print("nearest point to ",point1," is ",nearestpoint,"with distance",minDistance)
	return minDistance


def euclideanPointDistance(point1, point2):
	dist = np.linalg.norm(point1 - point2)
	return dist

def manhattanPointDistance(point1,point2):
	sum=0
	sum += abs(point1[0] - point2[0])
	sum += abs(point1[1] - point2[1])
	return sum

saveFolder="DotsSim"
filelist = glob.glob('DatasetSim/*.png')
for file in  filelist:
	height=float(str(file).split("\\")[1].split('_')[3][:3])
	img1=cv2.imread(file)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	ret, img1 = cv2.threshold(img1, 40, 255, cv2.THRESH_BINARY)
	#findCentroids(img1,height,saveFolder)
saveFolder="DotsReal"
filelist = glob.glob('DatasetReal/FlatR100V0/*.png')
for file in  filelist:
	height=float(str(file).split("\\")[1].split('_')[3][:-3])
	img1 = cv2.imread(file)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	ret, img1 = cv2.threshold(img1, 40, 255, cv2.THRESH_BINARY)
	#findCentroids(img1,height,saveFolder)

# img1=cv2.imread("DotsSim/00_DotsSim_0_0.0.png")
# img2=cv2.imread("DotsReal/89_DotsReal_0_0.0.png")
img1=cv2.imread("DatasetReal/FlatR100V0/5_FlatR100V0_0_0.png")
img2=cv2.imread("DatasetSim/466_edgeprobe_0_0.0.png")
# img1=cv2.imread("DatasetReal/FlatR100V0/28_FlatR100V0_0_1.png")
# img2=cv2.imread("DatasetSim/603_edgeprobe_0_1.0.png")
# img1=cv2.imread("DatasetReal/FlatR100V0/31_FlatR100V0_0_2.png")
# img2=cv2.imread("DatasetSim/490_edgeprobe_0_2.0.png")
# img1=cv2.imread("DatasetReal/FlatR100V0/61_FlatR100V0_0_3.png")
# img2=cv2.imread("DatasetSim/135_edgeprobe_0_3.0.png")
# img1=cv2.imread("DatasetReal/FlatR100V0/73_FlatR100V0_0_4.png")
# img2=cv2.imread("DatasetSim/295_edgeprobe_0_4.0.png")

compareTwoImages(img1,img2)
cv2.waitKey(0)#close on button
cv2.destroyAllWindows()
