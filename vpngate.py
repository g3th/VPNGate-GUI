import config_download as config

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class vpngate_client:

	def __init__(self):
	
		self.vpngate_gui = Tk()
		self.vpngate_gui.title('VPN Gate Client')
		self.vpngate_gui.resizable(False,False)
		self.vpngate_gui.geometry('375x450')
		
	def gui_logo(self):
		open_image = (Image.open('logo.jpg'))
		resized= open_image.resize((363,100))
		image = ImageTk.PhotoImage(resized)		
		canvas = Canvas(self.vpngate_gui, width = 100, height = 100)
		canvas.image = image
		canvas.create_image(5,5,anchor=NW,image=image)
		canvas.place(x=1,y=1)
		
	def create_lists_download_configs(self):
		configs = config.download_ovpn_configuration_files()
		configs.create_ovpn_download_list()
		message_label = Label(self.vpngate_gui, text = configs.download_ovpn_files())
		message_label.pack(padx=30, pady=100)
		
	def WindowLoop(self):
		
		self.vpngate_gui.mainloop()
		
vpngate = vpngate_client()
vpngate.create_lists_download_configs()
vpngate.gui_logo()
vpngate.WindowLoop()
