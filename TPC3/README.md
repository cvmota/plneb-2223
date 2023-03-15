# Aula prática nº3
## Extração de informação com Expressões Regulares de documentos PDF convertidos para texto.

O ficheiro [dicionario_medico.ipynb](https://github.com/cvmota/plneb-2223/tree/main/TPC3/dicionario_medico.ipynb) contém:
Exercícios efectuados na aula:
1. Criação de uma a função que faz o parser do ficheiro [dicionario_medico.txt](https://github.com/cvmota/plneb-2223/tree/main/TPC3/dicionario_medico.txt) e devolve um tuplo com o cabeçalho do ficheiro e uma lista de tuplos com a "Palavra" ou designação médica e respectivo "Significado".
2. Criação de uma função que gera um ficheiro HTML resultante do output da função anterior, com o cabeçalho e todas as designações com a respectiva descrição.

Realização do trabalho de casa:

1. Resolver o problema do \f com o \n entre a designação e a designação e a descrição.
2. Refazer a função parse_file com separação das designações e descrição por etiquetas.

    Por exemplo:
    - @ para idenfiticar os termos
    - \# para a designação
3. Geração do ficheiro HTML em formato de uma tabela com utilização de CSS.


Ficheiros HTML com as designações e respectiva descrição gerados a partir da execução do ficheiro [dicionario_medico.ipynb](https://github.com/cvmota/plneb-2223/tree/main/TPC3/dicionario_medico.ipynb):
- [dicionario_medico_1.html](https://htmlpreview.github.io/?https://github.com/cvmota/plneb-2223/blob/main/TPC3/output/dicionario_medico_1.html)

  ![output_1](https://github.com/cvmota/plneb-2223/blob/main/TPC3/output/img_output_1.jpg)
- [dicionario_medico_2.html](https://htmlpreview.github.io/?https://github.com/cvmota/plneb-2223/blob/main/TPC3/output/dicionario_medico_2.html)

  ![output_2](https://github.com/cvmota/plneb-2223/blob/main/TPC3/output/img_output_2.jpg)
  