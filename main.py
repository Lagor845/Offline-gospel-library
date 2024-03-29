import requests
from bs4 import BeautifulSoup

def fix_spanish_text(text):
    text = text.replace("Ã¼","ü").replace("Ã©","é").replace("Ã³","ó").replace("Ã¡","á").replace("Â¡","¡").replace("±","ñ").replace("Ã","í")
    return text

while True:
    language = int(input("What language would you like? \n1. English \n2. Spanish \n"))
    if language == 1:
        language_plugin = "eng"
        break

    elif language == 2:
        language_plugin = "spa"
        break

    else:
        print("Not a valid language")

html = requests.get(f"https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/1?lang={language_plugin}")
soup = BeautifulSoup(html.text,"html.parser")

dominant = soup.find("span", {"class": "dominant"}).text

subtitle = soup.find("p", {"class": "subtitle"}).text

chapter_title = soup.find("p", {"class": "title-number"}).text

intro = soup.find("p", {"class": "study-summary"}).text
intro = intro.replace("â"," — ").replace("Â","")

for verse in soup.find_all("p", {"class": "verse"}):
    for tag in verse.find_all("sup", {"class": "marker"}):
        tag.decompose()
    verse_num = verse.find("span", {"class": "verse-number"}).text
    verse.find("span", {"class": "verse-number"}).decompose()
    
    if language_plugin == "spa":
        verse = fix_spanish_text(verse.text)
    print(verse)