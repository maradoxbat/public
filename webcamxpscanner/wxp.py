#!/usr/bin/env python3
__author__ = "maradoxbat"
__version__ = "1.0"

from random import randint
from bs4 import BeautifulSoup
import requests
import time

start=time.time()
def randomipcheck(numofran):
	listofurls=[]
	
	for i in range(numofran):
		ipaddr=""
		ipaddr+=str(randint(1,254))+"."+str(randint(1,254))+"."+str(randint(1,254))+"."+str(randint(1,254))
		
		
		try:
			urlip = "http://"+str(ipaddr)+":8080/"
			req = requests.get(str(urlip),timeout=5)
			soup = BeautifulSoup(req.content, 'html.parser')
			webcampxptitle = 'my webcamXP server!'
			if soup.title.text == webcampxptitle:
				listofurls.append(urlip)
		except:
			pass
	return listofurls

numofran=int(input("Enter an integer:"))
print(randomipcheck(numofran))
print("total time: "+str(round((time.time()-start)))+" seconds.")
