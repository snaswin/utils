from tkinter import Tk, Entry, Button, INSERT, Message, Label, LEFT, RIGHT, TOP, BOTTOM
import cv2
import glob
import cv2
import numpy as np

#opencv funcs that ll be used in the end
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
	n = min(len(glob.glob(path1)),len(glob.glob(path2)),len(glob.glob(path3)),len(glob.glob(path4)) )
	cv2.createTrackbar('R','image',0,n-1,nothing)

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


#end of opencv funcs
##############






pathlist=[]

root = Tk()
root.geometry("600x600")
# header text
msg = Message(root, text="AIPC analysis!")
msg.config(font=('times', 28, 'italic bold underline'))
msg.pack()
##--------
Label(root,text=""" """, justify = LEFT, padx = 20).pack()
Label(root,text=""" """, justify = LEFT, padx = 20).pack()
Label(root,text="""Enter the paths & click load for each link in order:""", justify = LEFT, padx = 20).pack()
Label(root,text=""" """, justify = LEFT, padx = 20).pack()


# Create single line text entry box
entry = Entry(root)
entry.pack()
# Insert some default text
Label(root,text="""Load path: folder1!""", justify = LEFT, padx = 20).pack()
entry.insert(INSERT, '')

# Print the contents of entry widget to console
def print_content1():
	val = entry.get()
	print('\nDocked path for 1- ',val)
	pathlist.append(val)

# Create a button that will print the contents of the entry
button = Button(root, text='Load 1', command=print_content1)
button.pack()
##-----------------------------#


# Create single line text entry box
entry2 = Entry(root)
entry2.pack()
Label(root,text="""Load path: folder2!""", justify = LEFT, padx = 20).pack()
entry2.insert(INSERT, '')
def print_content2():
	val = entry2.get()
	print('\nDocked path for 2-',val)
	pathlist.append(val)
button2 = Button(root, text=' Load 2', command=print_content2)
button2.pack()
##-----------------------------#


# Create single line text entry box
entry3 = Entry(root)
entry3.pack()
Label(root,text="""Load path: folder3!""", justify = LEFT, padx = 20).pack()
entry3.insert(INSERT, '')
def print_content3():
	val = entry3.get()
	print('\nDocked path for 3-',val)
	pathlist.append(val)
button3 = Button(root, text=' Load 3', command=print_content3)
button3.pack()
##-----------------------------#

##-----------------------------#

# Create single line text entry box
entry4 = Entry(root)
entry4.pack()
Label(root,text="""Load path: folder4!""", justify = LEFT, padx = 20).pack()
# Insert some default text
entry4.insert(INSERT, '')

# Print the contents of entry widget to console
def print_content4():
	val = entry4.get()
	print('\nDocked path for 4-',val)
	pathlist.append(val)

# Create a button that will print the contents of the entry
button4 = Button(root, text=' Load 4', command=print_content4)
button4.pack()
##-----------------------------#



msg2 = Message(root, text="ash alpha.")
msg2.config(font=('times', 5, 'italic bold underline'))
msg2.pack()
##------

##transition to opencv program
# Create a button that will destroy the main window when clicked

Label(root,text=""" """, justify = LEFT, padx = 20).pack()
Label(root,text="""Close this window to open the Interface (Close it ONLY after loading all paths) """, justify = LEFT, padx = 20).pack()
Label(root,text=""" Note: This will load .png images only""", justify = LEFT, padx = 20).pack()

root.mainloop()
#end of tkinter
##########################################################################################
print("\nThe Images are from:")
for p in pathlist:
	print(p)

#from opencvsoft import softdisplay

path1 = pathlist[0] + '/*.png'
path2 = pathlist[1] + '/*.png'
path3 = pathlist[2] + '/*.png'
path4 = pathlist[3] + '/*.png'

softdisplay(path1, path2, path3, path4)

print("End")
