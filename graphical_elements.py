import config_download as config

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class interface_graphical_elements:

	def __init__(self):
	
		self.open_image = (Image.open('logo.jpg'))
		
		
	def gui_logo(self, root):
		
		resized= self.open_image.resize((363,100))
		image = ImageTk.PhotoImage(resized)		
		canvas = Canvas(root, width = 365, height = 110)
		canvas.image = image
		canvas.create_image(5,5,anchor=NW,image=image)
		canvas.place(x=1,y=1)
	
