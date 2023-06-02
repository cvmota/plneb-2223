import requests
from bs4 import BeautifulSoup
import json

url = "https://reference.medscape.com/guide/anatomy"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

def extract_description(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find("div", class_="refsection_content")
    content = divs.find_all("p")
    description = " ".join([p.text.replace('\xa0', ' ').strip() for p in content])
    image_urls = []

    img_tags = divs.find_all("img")
    for img in img_tags:
        img_url = img["src"]
        image_urls.append(img_url)

    return description, image_urls

def extract_data(soup, lista):
    divs = soup.find_all("div", class_="topic-alpha-wrap")
    for div in divs:
        ul = div.find("ul")
        lis = ul.find_all("li", class_="alpha-item")
        for li in lis:
            term = li.find("a").text.strip()
            url = li.find("a")["href"]
            descr, img_urls = extract_description(url)
            lista.append({ term: {"description": descr.strip(), "image_urls": img_urls}})

lista = []
extract_data(soup, lista)

with open("../database_files/anatomia_img.json", "w", encoding="utf-8") as file:
    json.dump(lista, file, ensure_ascii=False, indent=4)
