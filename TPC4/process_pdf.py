import json
import re


def parse_xml_file(filename):
    with open(filename, 'r', encoding='UTF8') as f:
        text = f.read()
        text = re.sub(r'<page.*?>', '', text)
        text = re.sub(r'</page>', '<hr>', text)
        text = re.sub(r'<fontspec.*?/>', '', text)
        text = re.sub(r'<image.*?/>', '', text)
        text = re.sub(r'<text[^>]+>(<b>.*</b>)</text>', r'<p>\1</p>', text)
        text = re.sub(r'<text[^>]+>(.*)</text>', r'\1', text)
        text = re.sub(r'.*<pdf2xml.*?>(.*)</pdf2xml>', r'\1', text, flags=re.DOTALL)

        # substituir espaços seguidos de \n
        text = re.sub(r'(\n)(\s\n)+', r'\1', text)

        return text


# Primeira versão mas muito lenta, o re.sub é muito lento a processar
def annotate_terms_1(text, terms):
    words = set(re.findall(r'\b(?!<.*?>)[\w-]+\b', text))
    filtered_words = words.intersection(terms)

    for word in filtered_words:
        descr = terms.get(word)
        text = re.sub(r'(\b' + word + r'\b)(?!(?:(?!<span>).)*</span>)',
                      r'<div class="tooltip">\1<span class="tooltiptext">' + descr + '</span></div>', text)
    return text


# Segunda versão com a compilação da expressão regular usando re.compile.
# Isso evita a necessidade de recompilar a expressão regular a cada iteração do loop,
# melhorando a performance do processamento
def annotate_terms(text, terms):
    words = set(re.findall(r'\b(?!<.*?>)[\w-]+\b', text))
    filtered_words = words.intersection(terms)

    pattern = re.compile(r'\b(' + '|'.join(filtered_words) + r')\b')
    return pattern.sub(lambda match: '<div class="tooltip">' + match.group() + '<span class="tooltiptext">' + terms[
        match.group()] + '</span></div>', text)


def xml_to_html_with_annotations(filename, terms_filename):
    text = parse_xml_file(filename)

    with open(terms_filename) as file:
        terms = json.load(file)
    text = annotate_terms(text, terms)

    # get the filename without the extension
    fname = re.sub(r'^(\.?[\w-]+)+\.\w+$', r'\1', filename)

    with open('output/' + fname + '.html', 'w', encoding='UTF8') as fw:
        fw.write('''<!DOCTYPE html>
            <html>
                <head>
                   <meta charset='utf-8'/>
                   <style>
                        .tooltip {
                          position: relative;
                          display: inline-block;
                          text-decoration: underline; 
                          color: blue; 
                          cursor: pointer;
                        }
                        
                        .tooltip .tooltiptext {
                          visibility: hidden;
                          width: 120px;
                          background-color: black;
                          color: #fff;
                          text-align: center;
                          border-radius: 6px;
                          padding: 5px 0;
                        
                          /* Position the tooltip */
                          position: absolute;
                          z-index: 1;
                        }
                        
                        .tooltip:hover .tooltiptext {
                          visibility: visible;
                        }
                        </style>
                </head>
            <body>''')
        fw.write(text)
        fw.write('</body></html>')


xml_to_html_with_annotations("LIVRO-Doenças-do-Aparelho-Digestivo.xml", "terms.json")
