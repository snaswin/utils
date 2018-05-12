import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
import pathlib


def renameFiles(path,outfold):
	files = glob.glob(path)
	pathlib.Path(outfold).mkdir(parents=True, exist_ok=True)
	#Assumption: Folder has a stage pic
	for n in range(1,len(files)):
		img = cv2.imread(files[n])
		outname= outfold + "{0:0=3d}".format(n) + ".png"
		cv2.imwrite(outname, img)
		print("File appended-",outname)
	
	print("Done!")
	print("Check-",outfold)


path=r"D:\Additive Mini Factory Project\X-Y layer from RpiCam\Toplay_Simulation\classes\Ash\print500_script\print500_04172018\data\*.jpg"
outfold = r"C:\Users\anirmaleswaran\Desktop\Report\1_OriginalImage\\"

renameFiles(path,outfold)	

	


