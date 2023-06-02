import json
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

base_url = "https://www.imaios.com"
url_list = ["https://www.imaios.com/en/e-anatomy/anatomical-structure/bones-of-cranium-1536890620?from=2",
            "https://www.imaios.com/en/e-anatomy/anatomical-structure/nasal-surface-of-maxilla-1536897696?from=2",
            "https://www.imaios.com/en/e-anatomy/anatomical-structure/nasal-bone-130148?from=1"]

bones_definition_file = "../database_files/bones_definition.json"


def extract_bones_info():
    bones = {}
    for url in url_list:
        soup = getSoup(url)
        ul = soup.find_all("ul", class_="list-children-hierarchy list-unstyled")
        for ul in ul:
            # existem duas ul identicas, vamos extrair apenas a primeira
            if ul["data-taid"] == "1":
                ul_extract_info(bones, ul)
    with open(bones_definition_file, "w", encoding="utf-8") as file:
        json.dump(bones, file, ensure_ascii=False, indent=4)
    print("Created the file:", bones_definition_file)


def ul_extract_info(bones, ul):
    for li in ul.find_all("li"):
        link = li.a["href"]
        name = li.a.text.strip()
        bones[name] = extract_bone_info(base_url + link)
        # verificar se dentro de uma li temos novamente uma lista de item e se existir, processar recursivamente
        # esta parte não está a funcionar porque seria preciso simular o click no botão
        if li.ul:
            ul_extract_info(bones, li.ul)


def getSoup(url):
    headers = {'User-Agent': UserAgent().random}
    html = requests.get(url, headers=headers).text
    time.sleep(1)  # Atraso de 1 segundo
    return BeautifulSoup(html, "html.parser")


# /en/e-anatomy/anatomical-structure/parietal-bone-1536890708?from=2
def extract_bone_info(link):
    soup_info = getSoup(link)
    source = soup_info.find_all("source", media="(max-width:1200px)")
    img_link = None
    if source:
        if len(source) == 1:
            img_link = source[0]["srcset"]
        elif len(source) == 2:
            img_link = source[1]["srcset"]

    div = soup_info.find("div", id="structure-definitionText")
    descr = div.p.text.strip()
    quoted_note = div.div.text.strip()
    return {"descr": descr, "quoted_note": quoted_note, "img_link": img_link}


print("Starting...")
extract_bones_info()
print("End!")
