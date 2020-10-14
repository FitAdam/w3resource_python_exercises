""" 8. Write a Python program to get the top stories from Google news. """

import requests
from bs4 import BeautifulSoup

URL = 'https://www.freecodecamp.org/news/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

for title in soup.find_all('a'):
    print(title.get_text())