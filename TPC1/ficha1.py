# 1. Programa que pergunta ao utilizador o nome e imprime em maiúsculas.
nome = input("Qual é o seu nome?\n")
print(nome.upper())


# 2. Função que recebe array de números e imprime números pares.
def printEven(list):
    print([x for x in list if x % 2 == 0])


printEven([1, 2, 3, 4, 5, 6])


# 3. Função que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa.
def printReverseLines(filename):
    file = open(filename, encoding="UTF-8")
    lines = file.readlines()
    print(lines[::-1])
    file.close()


printReverseLines("file.txt")


# 4. Função que recebe nome de ficheiro e imprime número de ocorrências das 10 palavras mais frequentes no ficheiro
def order(item):
    return item[1]


def occurrences(filename):
    file = open(filename, encoding="UTF-8")
    frequency = {}
    for line in file:
        words = line.split()
        for word in words:
            total = frequency.get(word, 0)
            total += 1
            frequency[word] = total
    file.close()
    ordered = sorted(frequency.items(), key=order, reverse=True)
    print(ordered[0:10])


occurrences("file.txt")


# 5. Função que recebe um texto como argumento e o ”limpa”:
# separa palavras e pontuação com espaços,
# converte para minúsculas,
# remove acentuação de caracteres, etc.

def clean_text(text):
    # converte para minúsculas
    text.lower()
    # remove acentuação de caracteres, etc
    accents = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a',
               'é': 'e', 'è': 'e', 'ê': 'e',
               'í': 'i', 'ì': 'i',
               'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o',
               'ú': 'u', 'û': 'u', 'ù': 'u',
               'ç': 'c'}
    for accent, letter in accents.items():
        text = text.replace(accent, letter)

    # separa palavras e pontuação com espaços
    # ??? é para substituir a pontuação por espaços ou apenas fazer o split por espaços?

    p = [".", ",", ";", ":", "!", "?"]
    for c in p:
        text = text.replace(c, " ")

    return text.split()


print(clean_text("Este é um exemplo de um texto com pontuação, carateres com acentos, letras Maiúsculas, etc."))


# Create a function that:
# 1. given a string “s”, reverse it.
def reverse(s):
    return s[::-1]


print(reverse("oirártnoc oa esarf amu é otsI"))


# 2. given a string “s”, returns how many “a” and “A” characters are present in it.
def count_aA(s):
    total = 0
    for c in s:
        if c == "a" or c == "A":
            total += 1
    return total


frase = 'O tempo perguntou ao tempo, quanto tempo ele tem! O tempo tem TANTO tempo, que nem tempo o tempo tem.'
print('A frase "{}" tem {} aA(s).'.format(frase, count_aA(frase)))


# 3. given a string “s”, returns the number of vowels there are present in it.
def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for c in s.lower():
        if c in vowels:
            total += 1
    return total


print("A frase \"{}\" tem {} vogais".format(frase, count_vowels(frase)))


# 4. given a string “s”, convert it into lowercase.
def lowercase(s):
    return s.lower()


print(lowercase(frase))


# 5. given a string “s”, convert it into uppercase.
def uppercase(s):
    return s.upper()


print(uppercase(frase))
