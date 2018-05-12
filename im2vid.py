###############################################
## Images to video
##############################################

import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

def Im2Vid(folderIN='olap/*.jpg',outfile='olapvideo.avi'):

	files=glob.glob(folderIN)

	img0=cv2.imread(files[0],0)
	img0=img0*255

	
	#xshift=45
	#yshift=-335
	#img1=img0[230+xshift:940+xshift,605+yshift:1305+yshift]
	#img1=img0[650:1900,650:1900]
	img1=img0
	if len(img1.shape) ==3:
		height , width , ch =  img1.shape
	elif len(img1.shape) ==2:
		height , width =  img1.shape
	
	video = cv2.VideoWriter(outfile, cv2.VideoWriter_fourcc(*"XVID"),2,(width,height))

	for f in files:		
		img0 = cv2.imread(f)
		print("Image ",f," read.")
		img0 = img0
		#img1=img0[650:1900,650:1900]
		#img1=(img0>0).astype(int)*255

		img1=img0
		#print(type(img1))
		video.write(img1)
		#cv2.waitKey(50)
		
	cv2.destroyAllWindows()
	video.release()
		
	
	print("Video saved")

#Im2Vid(folderIN='centered/LowRes_centered_G/*.png',outfile='lowres_centeredG.avi')
#Im2Vid(folderIN='centered/centered_G/GcodeS/*.png',outfile='G_video.avi')
folderIN= r'D:\Additive Mini Factory Project\X-Y layer from RpiCam\Toplay_Simulation\classes\Ash\print500_script\print500_04172018\Analysis\BGrem_SkelGcode\skel_bgrem_rotscale_OVERLAP/*.png'
Im2Vid(folderIN ,outfile='Combine_video_normal.avi')
