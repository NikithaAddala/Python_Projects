# Web_Scraping

Personal_Project_1 using Python.

This file contains detailed explanation of each line used in the code.

1. "import requests 
from bs4 import BeautifulSoup as bs" 

Libraries have been imported: requests and BeautifulSoup (as bs).
Library requests: this library allows a user to send HTTP requests easily. It is one of the most downloaded Python package. 
Library BeautifulSoup: it is used for pulling data from HTML and XML files. A parser is used to navigate, search and modify the parse tree.

2. github_user = input('Input Github User:')
A username is taken as the input.

3. url = 'https://github.com/'+github_user
'+github_user' is given for a dynamaic approach.

4. r = requests.get(url)
to request (get) data from the server using requests package.

5. soup = bs(r.content, 'html.parser')

6. profile_image = soup.find('img', {'alt' : 'Avatar'})['src']

7. print(profile_image)
Displays the profile image of the requested github user.
