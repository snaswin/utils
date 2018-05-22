import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
	pass

def stich(r, img, path1, path2, path3, path4, resize):

	files1 = glob.glob(path1)
	files2 = glob.glob(path2)
	files3 = glob.glob(path3)
	files4 = glob.glob(path4)
	
	I = cv2.imread(files1[r],0)
	J = cv2.imread(files2[r],0)
	K = cv2.imread(files3[r],0)
	L = cv2.imread(files4[r],0)
	
	if resize == True:			
		I = cv2.resize(I, (1250,1250), 0,0,cv2.INTER_AREA)
		J = cv2.resize(J, (1250,1250), 0,0,cv2.INTER_AREA)
		K = cv2.resize(K, (1250,1250), 0,0,cv2.INTER_AREA)
		L = cv2.resize(L, (1250,1250), 0,0,cv2.INTER_AREA)
		
		
	tmp1 = np.hstack((I,J))
	tmp2 = np.hstack((K,L))
	tmpz = np.vstack((tmp1, tmp2))
	img[:,:] = tmpz
	#plt.imshow(img)
	#plt.show()
	
	return img

def softdisplay(path1, path2, path3, path4):
		

	# Create a black image, a window
	img = np.zeros((1250*2,1250*2), np.uint8)
	cv2.namedWindow('image',0)
	cv2.resizeWindow('image', 625,625)

	# create trackbars for color change
	cv2.createTrackbar('R','image',0,498,nothing)

	# create switch for ON/OFF functionality
	switch = '0 : OFF \n1 : ON'
	cv2.createTrackbar(switch, 'image',0,1,nothing)
	
	while cv2.getWindowProperty('image', 0) >= 0:
		# the abv loop condn is unique- closes the window if x<close> is pressed, since that event ll return a -1
		cv2.imshow('image',img)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
		#get current position of trackbar
		r= cv2.getTrackbarPos('R','image')
		s= cv2.getTrackbarPos(switch, 'image')
		if s == 0:
			img[:] = 0
		else:
			img[:] = stich(r, img, path1, path2, path3, path4, resize=True)
		
		keyCode = cv2.waitKey(50)
		
			
	cv2.destroyAllWindows()
	


	
#path1= 'reshape_S3/*.png'
#path2= 'reshape_S3/*.png'
#path3= 'reshape_Gcode/*.png'
#path4= 'reshape_S3_bgremoved\subtract\subG/*.png'
#softdisplay(path1, path2, path3, path4)
