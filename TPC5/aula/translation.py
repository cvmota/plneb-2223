import json

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='pt', target='en')

file_in = open("dicionario_medico_aula.json")
dicio = json.load(file_in)
file_in.close()

new_dicio = {}
for designation, description in dicio.items():
    en_translation = translator.translate(designation)
    print(en_translation)
    new_dicio[designation] = {
        'des': description,
        'en': en_translation
    }

with open('dicionario_translation.json', 'w') as file_out:
    json.dump(new_dicio)
