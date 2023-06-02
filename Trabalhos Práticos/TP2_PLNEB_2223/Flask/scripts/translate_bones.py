import json
import re

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='pt', target='en')

BONES_FILE = "../database_files/bones.json"

with open("../database_files/database.json", encoding="UTF8") as file:
    db = json.load(file)


def translate_bones():
    processed_bones = {}

    for key, value in db['bones'].items():
        if value.get('imgs') and value.get('ids'):
            # Extrai a categoria pelos ":"
            matches = re.findall(r'(\d+(?:\.\d+)+?)\s(([^:]+):?[^:]*?)$', key)
            if matches:
                category = matches[0][2]
                category, title = translate_bone_section_data(category, key, value)
                if category in processed_bones:
                    processed_bones[category][title] = value
                else:
                    processed_bones[category] = {title: value}

    with open(BONES_FILE, "w") as fw:
        json.dump(processed_bones, fw, indent=4, ensure_ascii=False)


def translate_bone_section_data(category, key, value):
    en_category = translator.translate(category)
    en_title = translator.translate(key)
    for id, idData in value["ids"].items():
        descr = idData.get("descr")
        if descr:
            idData["descr"] = translator.translate(descr).capitalize()
    return en_category, en_title


translate_bones()
