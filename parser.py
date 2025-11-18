import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

titles = soup.select(".titleline > a")

for t in titles:
    print(t.get_text())

"""
AUFGABEN:
1. Nur titles mit einem bestimmten Keyword printen
keyword = input("keyword: ").lower()
for t in titles:
    if keyword in t.get_text().lower():
        print(t.get_text())

2. Titles in einer .txt-Datei abspeichern
with open("titles.txt", "w") as f:
    for t in titles:
        f.write(t.get_text() + "\n")

        
"""