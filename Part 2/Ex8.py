""" 8. Write a Python program to get the top stories from Google news. """

import requests
from bs4 import BeautifulSoup

URL = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pIUWlnQVAB?hl=en-GB&gl=GB&ceid=GB%3Aen'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)