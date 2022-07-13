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
		self.progressbar.pack(padx=20,pady=140)#grid(column=0, row=0, columnspan=2, padx=100, pady=100)
		
	def create_ovpn_download_list(self,root):
		root.update_idletasks()		
		with open('config/openvpn_config_url_list','a') as openvpn_urls:	
			for link in open_vpn.get_all_page_links():
				self.progressbar.start()				
				openvpn_urls.write(self.vpngate + link + "\n")
				self.progressbar['value']+=1
				self.progressbar.stop()
		openvpn_urls.close()
		
	def download_ovpn_files(self, root):
		root.update_idletasks()
		with concurrent.futures.ThreadPoolExecutor() as executor:
				
				with open('config/openvpn_config_url_list','r') as configs:
					
					for line in configs.readlines():
						thread = executor.submit(servers.get_ovpn_configuration_link, line)
						self.progressbar['value']+=1
						self.futures_list.append(thread)

						
					for returned_value in self.futures_list:
						result = returned_value.result()
						self.progressbar['value']+=1
						self.downloading_urls.append(result)
						
					for url in self.downloading_urls:
						executor.submit(servers.download_config, url, str(self.configuration_number))	
						self.configuration_number += 1
						self.progressbar['value']+= 1
						self.progressbar.stop()
						
