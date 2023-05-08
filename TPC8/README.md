# Aula prática nº8
## Biblioteca spaCy para o processamento avançado de linguagem natural


**TPC**

Procurar os melhores amigos num livro recebido como argumento e devolver o top 30.

Para cada frase, verificar se existem duas entidades na mesma linha.
- Se tiver, cria o par (ent1, ent2) e incrementa o contador correspondente.


**Implementação:** [best_friends.py](https://github.com/cvmota/plneb-2223/blob/main/TPC8/best_friends.py)

**Exemplo de um output**
>\>python best_friends.py .\books\harry_potter_pedra_filosofal.txt

>Top 30 best friends: [(('Harry', 'Ron'), 90), (('Hagrid', 'Harry'), 49), (('Harry', 'Hermione'), 44), (('Hermione', 'Ron'), 31), (('Harry', 'Vernon'), 19), (('Harry', 'Quirrell'), 18), (('Dudley', 'Harry'), 15), (('Harry', 'Malfoy'), 14), (('Dumbledore', 'Harry'), 12), (('Harry', 'Snape'), 10), (('Dudley', 'Vernon'), 9), (('Dudley', 'tia Petúnia'), 9), (('Harry', 'Neville'), 9), (('Harry', 'Wood'), 9), (('Harry', Hogwarts'), 8), (('Dumbledore', 'Mc_Gonagall'), 7), (('Dumbledore', 'Hagrid'), 7), (('Vernon', 'tia Petúnia'), 7), (('Harry', 'Quidditch'), 7), (('Gryffindor', 'Harry'), 7), (('Dursleys', 'Harry'), 6), (('Fred', George'), 6), (('Crabbe', 'Goyle'), 6), (('Harry', 'Mc_Gonagall'), 6), (('Harry', 'Slytherin'), 6), (('Hagrid', 'Ron'), 6), (('Hagrid', 'Hermione'), 6), (('Dudley', 'Piers'), 5), (('Crabbe', 'Malfoy'), 5), (('Harry', 'Natal'), 5)]


