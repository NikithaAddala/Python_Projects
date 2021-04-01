# Web_Scraping

Personal_Project_1 on web scraping using python. 

This file contains detailed explanation of each line used in the code.

1. "import requests <!-- pip install requests >
from bs4 import BeautifulSoup as bs" <!-- pip install beautifulsoup4 >

2 Libraries have been imported: requests and BeautifulSoup (as bs).

library requests: this library allows a user to send HTTP requests easily. It is one of the most downloaded Python package. 

Library BeautifulSoup: it is used for pulling data out HTML and XML files. A parser is used to navigate, search and modify parse tree.

Read more about bs4 here: https://www.datacamp.com/community/tutorials/amazon-web-scraping-using-beautifulsoup?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1007743&gclid=CjwKCAjw3pWDBhB3EiwAV1c5rAX48KGax5fT3qluyqpSYtZLWxzzvB4Y59Z7f9r77LqjDiKtvEkuaBoCBlcQAvD_BwE

2. github_user = input('Input Github User:')
A username is taken as the input.

3. url = 'https://github.com/'+github_user
'+github_user' is given for a dynamaic approach.

4. r = requests.get(url)
to request (get) data from the server using requests package.

5. soup = bs(r.content, 'html.parser')

6. profile_image = soup.find('img', {'alt' : 'Avatar'})['src']

7. print(profile_image)
displays the profile image of the requested github user