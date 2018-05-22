from tkinter import Tk, Entry, Button, INSERT, Message, Label, LEFT, RIGHT, TOP, BOTTOM
import cv2

pathlist=[]

root = Tk()
root.geometry("500x500")
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
entry.insert(INSERT, 'Load path: folder1!')

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
entry2.insert(INSERT, 'Load path: folder2!')
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
entry3.insert(INSERT, 'Load path: folder3!')
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
# Insert some default text
entry4.insert(INSERT, 'Load path: folder4!')

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

from opencvsoft import softdisplay

path1 = pathlist[0] + '/*.png'
path2 = pathlist[1] + '/*.png'
path3 = pathlist[2] + '/*.png'
path4 = pathlist[3] + '/*.png'

softdisplay(path1, path2, path3, path4)

print("End")
