import json

import requests
from bs4 import BeautifulSoup

base_url = "https://reference.medscape.com/guide/anatomy"


def extract_info(link):
    soup = get_soup(link)
    divs = soup.find("div", class_="refsection_content")
    content = divs.find_all("p")
    descr = ""
    for p in content:
        descr += p.text.strip() + ' '

    image_urls = []
    img_tags = divs.find_all("img")
    for img in img_tags:
        img_url = img["src"]
        image_urls.append(img_url)

    return {"descr": descr.strip(), "img_urls": image_urls}


def get_soup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")


def extract_data():
    dict = {}
    soup = get_soup(base_url)
    divs = soup.find_all("div", class_="topic-alpha-wrap")
    for div in divs:
        ul = div.find("ul")
        lis = ul.find_all("li", class_="alpha-item")
        for li in lis:
            term = li.find("a").text.strip()
            url = li.find("a")["href"]
            dict[term] = extract_info(url)
    write_file(dict)


def write_file(dict):
    with open("anatomia.json", "w", encoding="utf-8") as file:
        json.dump(dict, file, ensure_ascii=False, indent=4)


extract_data()
