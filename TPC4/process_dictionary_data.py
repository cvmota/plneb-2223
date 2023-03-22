import json
import re


def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()


def parse_xml_file(filename):
    with open(filename, 'r', encoding='UTF8') as f:
        text = f.read()
        text = re.sub(r'</?page.*>', '', text)
        text = re.sub(r'\n\n', r'', text)
        # .*? -> lazy, apanha até o primeiro > e para
        text = re.sub(r'</?text.*?>', r'', text)
        terms_descriptions = re.findall(r'<b>(.+)</b>([^<]+)', text)

        # limpar todos os \n e espaços no inicio e fim da descrição
        terms_descriptions = [(desig, clean_text(descr)) for (desig, descr) in terms_descriptions]

        # retornar um dicionário com os termos
        return dict(terms_descriptions)


terms_descr = parse_xml_file("dicionario_medico.xml")
print(terms_descr)

## guardar os dados em json
with open('terms.json', 'w', encoding='UTF8') as f:
    json.dump(terms_descr, f, ensure_ascii=False, indent=4)
