# Use http://collemc.people.si.umich.edu/data/bshw3StarterFile.html as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

#test change

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urlopen(base_url).read()
soup = BeautifulSoup(html, "html.parser")
mainpic = "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg" ##link to main pic that needs to be replaced
counter = 0

for student in soup.find_all(text = re.compile('student')):
	placeholder = str(student) ##needed a string placeholder because the navigable string was acting weird...
	placeholder = placeholder.replace("student","AMAZING student")
	student.replace_with(placeholder)



for pic in soup.findAll("img"):
	if pic["src"] == mainpic:
		pic["src"] = "chilldude.jpg"
		
	else:
		pic["src"] = "media/logo.png"



html = soup.prettify("utf-8") ##found on stackoverlow on how to write html file from python
with open("output.html", "wb") as file: ##http://stackoverflow.com/questions/14369447/how-to-save-back-changes-made-to-a-html-file-using-beautifulsoup-in-python
    file.write(html)