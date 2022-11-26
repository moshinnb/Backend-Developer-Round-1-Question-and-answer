import re
import requests
from bs4 import BeautifulSoup

url='https://ful.io/'
resp=requests.get(url)
if resp.status_code==200:
  soup=BeautifulSoup(resp.text,'html.parser')	
  l=soup.find("div",{"class":"flex my-2 -mx-1 justify-center"})
  print("Social links -")
  for i in l.findAll("a"):
      print(i.get('href'))
  e="flex-grow flex flex-wrap md:pl-20 -mb-10 md:mt-0 mt-10 md:text-left text-center"
  em_c=soup.find("div",{"class":e})

  em=[i.get('href') for i in em_c.contents[3].findAll("a") ]
  print("Email/s-\n",em[0])
  print("Contact:\n",(em[1])[4:])