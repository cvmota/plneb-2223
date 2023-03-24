import json

# 1. Ler o ficheiro termos_traduzidos
# 2. Fazer parse do ficheiro e construir uma estrutura com os termos traduzidos
# Exemplo: {key: {'en': tradução}}
with open("termos_traduzidos.txt", encoding="UTF8") as file:
    dict = {term[0]: {'en': term[1].strip()} for term in (line.split(' @ ') for line in file)}
    print(dict)

#
with open("termos_traduzidos.json", "w", encoding="UTF8") as fw:
    json.dump(dict, fw, ensure_ascii=False, indent=4)
