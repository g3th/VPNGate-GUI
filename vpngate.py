import config_download as config

from tkinter import *
from tkinter import ttk
from graphical_elements import interface_graphical_elements as graphics

class vpngate_client:

	def __init__(self):
	
		self.vpngate_gui = Tk()
		self.vpngate_gui.title('VPN Gate Client')
		self.vpngate_gui.resizable(False,False)
		self.vpngate_gui.geometry('375x450')
		self.configs = config.download_ovpn_configuration_files(self.vpngate_gui)
		
	def elements(self):
	
		graphics().gui_logo(self.vpngate_gui)
		
	def download(self):
		
		self.configs.create_ovpn_download_list(self.vpngate_gui)		
		self.configs.download_ovpn_files(self.vpngate_gui)
		
	def WindowLoop(self):
		
		self.vpngate_gui.mainloop()
	
vpngate = vpngate_client()
vpngate.elements()
vpngate.download()
vpngate.WindowLoop()
