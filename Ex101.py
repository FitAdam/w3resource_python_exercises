"""101. Write a Python program to access and print a URL's content to the console."""

import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.freecodecamp.org/news/devops-prerequisites-course/"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

selected_lines = soup.select("p")


for elem in selected_lines:
    print(elem.text)
