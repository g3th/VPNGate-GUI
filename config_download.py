import concurrent.futures
import servers
import shutil
import os

from tkinter import *
from tkinter import ttk
from servers import download_ovpn_config

open_vpn = download_ovpn_config()
shutil.rmtree('config')
os.makedirs('config')

class download_ovpn_configuration_files:

	def __init__(self,root):
		
		self.vpngate = 'https://www.vpngate.net/en/'
		self.futures_list=[]
		self.downloading_urls=[]
		self.configuration_number=0
		self.progressbar = ttk.Progressbar(root, orient = 'horizontal', mode = 'determinate', length = 280)
		self.progressbar.place(height=45,width=300,x=40,y=130)
		self.downloadbar = ttk.Progressbar(root, orient = 'horizontal', mode = 'determinate', length = 280)
		self.message_label = Label(text = 'Starting Download')
		
	def create_ovpn_download_list(self,root):	
		with open('config/openvpn_config_url_list','a') as openvpn_urls:	
			for link in open_vpn.get_all_page_links():	
				openvpn_urls.write(self.vpngate + link + "\n")
				self.message_label.place(x=120,y=185)
				root.update()
		openvpn_urls.close()
		
	def download_ovpn_files(self, root):
		with concurrent.futures.ThreadPoolExecutor() as executor:
				
				with open('config/openvpn_config_url_list','r') as configs:
					
					for line in configs.readlines():
						thread = executor.submit(servers.get_ovpn_configuration_link, line)
						self.futures_list.append(thread)
											
					for returned_value in self.futures_list:
						result = returned_value.result()
						self.message_label['text']='Fetching Config URLs' 
						self.progressbar['value']+=1						# This Progress bar is working
						self.downloading_urls.append(result)
						root.update_idletasks()
											
					for url in self.downloading_urls:
								
						self.message_label['text']='Downloading Open-VPN Config Files'
						self.progressbar['value']+=1						# This progress bar isnt working
						thread = executor.submit(servers.download_config, url, str(self.configuration_number))
						self.futures_list.append(thread)												
						self.configuration_number+= 1
						root.update_idletasks()
