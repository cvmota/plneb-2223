#!/usr/bin/env python3
import sys

import spacy
from collections import Counter

# Procurar os melhores amigos: criar um tuplo com (p1, p2) e devolver o top 30.
# Para cada frase, verifica se tem 2 entidades na mesma linha.
# Se tiver, cria um par (ent1, ent2) e incrementa o contador correspondente.
nlp = spacy.load('pt_core_news_md')

#  sys.argv[0]
#  sys.argv[1] -> primeiro argumento
filename = sys.argv[1]

with open(filename, encoding='UTF8') as f:
    document = f.read()

# Obtem a árvore do documento
av = nlp(document)

# Cria um contador de pares de amigos
bestFriends = Counter()

for s in av.sents:
    same_line_entities = Counter()
    for ent in s.ents:
        same_line_entities[ent.text] += 1
    top2 = same_line_entities.most_common(2)
    # se só existir uma entidade na linha, não vamos criar um tuplo de melhor amigo
    if len(top2) >= 2:
        # Para tratar, por exemplo, ('Harry', 'Ron') e ('Ron', 'Harry') como o mesmo par de amigos,
        # ordenamos os nomes alfabeticamente antes de criar o tuplo.
        pair = tuple(sorted([top2[0][0], top2[1][0]]))
        bestFriends[pair] += 1

print("Top 30 best friends:", bestFriends.most_common(30))
