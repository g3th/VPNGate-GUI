import concurrent.futures
import servers
import shutil
import os

from servers import download_ovpn_config

open_vpn = download_ovpn_config()
shutil.rmtree('config')
os.makedirs('config')

class download_ovpn_configuration_files:

	def __init__(self):
		
		self.vpngate = 'https://www.vpngate.net/en/'
		self.futures_list=[]
		self.downloading_urls=[]
		self.configuration_number=0
		
	def create_ovpn_download_list(self):
	
		with open('config/openvpn_config_url_list','a') as openvpn_urls:
			for link in open_vpn.get_all_page_links():
				openvpn_urls.write(self.vpngate + link + "\n")
		openvpn_urls.close()

		
	def download_ovpn_files(self):		

		with concurrent.futures.ThreadPoolExecutor() as executor:
				
				with open('config/openvpn_config_url_list','r') as configs:
					
					for line in configs.readlines():
						thread = executor.submit(servers.get_ovpn_configuration_link, line)
						self.futures_list.append(thread)
					
					for returned_value in self.futures_list:
						result = returned_value.result()
						self.downloading_urls.append(result)
						
					for url in self.downloading_urls:
						executor.submit(servers.download_config, url, str(self.configuration_number))
						self.configuration_number += 1
