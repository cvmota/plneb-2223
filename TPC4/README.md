# Aula prática nº4
## Extração de informação com Expressões Regulares de documentos PDF convertidos para XML.

O ficheiro [process_dictionary_data.py](https://github.com/cvmota/plneb-2223/tree/main/TPC4/process_dictionary_data.py) contém:
Exercícios efectuados na aula:
1. Criação de uma a função que faz o parser do ficheiro XML [dicionario_medico.xml](https://github.com/cvmota/plneb-2223/tree/main/TPC4/dicionario_medico.xml) e devolve um dicionário com os termos e repectiva descrição.
2. Após a obtenção do dicionário de termos é gerado um ficheiro json com dicionário de termos.

Realização do trabalho de casa no [ficheiro process_pdf.py](https://github.com/cvmota/plneb-2223/tree/main/TPC4/ficheiro process_pdf.py):

1. Processamento do XML do ficheiro [LIVRO-Doenças-do-Aparelho-Digestivo.xml](https://github.com/cvmota/plneb-2223/tree/main/TPC4/LIVRO-Doenças-do-Aparelho-Digestivo.xml)
2. Anotação do texto com os termos do dicionário.
    ![output_1](https://github.com/cvmota/plneb-2223/blob/main/TPC4/output/output_1.png)
3. Geração de um ficheiro HTML com o texto anotado [LIVRO-Doenças-do-Aparelho-Digestivo.html](https://htmlpreview.github.io/?https://github.com/cvmota/plneb-2223/tree/main/TPC4/output/LIVRO-Doenças-do-Aparelho-Digestivo.html).


Dificuldades encontradas:
1. Ao processar as anotações, não criar anotações dentro de uma anotação. Se um termo estiver na descrição do termo, não criar a anotação.
2. Processamento das anotações muito lento.
    - feito o re.compile da expressão regular para melhorar o desempenho
3. Após o processamento das anotações, foi possível verificar que alguns termos foram mal processado na fase inicial, por exemplo, o termo "e", aparece no [dicionário de termos](https://github.com/cvmota/plneb-2223/tree/main/TPC4/terms.json) com a descrição:
    "e": "corruptela de ec (evacuação, evaporação).",
No entanto parece que foi problema foi adicionado pelas quebras de página no pdf (os \f)
    ![output_2](https://github.com/cvmota/plneb-2223/blob/main/TPC4/output/output_2.png)