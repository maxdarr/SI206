# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

# goes through the links on the side menu and replaces where it says students with AMAZING students
for menu_item in soup.find_all(class_="menu__link"):
	if "students" in menu_item.text:
		menu_item.string = menu_item.string.replace("students", "AMAZING students")
	
#goes through the main body of the page and changes the video to the picture of me, and also replaces
#any instance of students with AMAZING students
for texts in soup.find_all(class_="field-item even"):
	if texts.p:
		texts.iframe['src']="media/me.png"
		if "student" in texts.text:
			texts_string = texts.prettify()
			texts = texts_string.replace("student", "AMAZING student")

#replaces the logos with the local version of the logos
for pic in soup.find_all(class_="logo"):
	if pic.img:
		pic.img['src'] = "media/logo.png"
for pic1 in soup.find_all(class_="footer-logo"):
	if pic1.img:
		pic1.img['src'] = "media/logo.png"
#opens up an html file and writes the soup into it
f = open('bshw3.html','w')
f.write(soup.prettify())
f.close()
		
