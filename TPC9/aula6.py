import json
import re

from flask import Flask, render_template, request

app = Flask(__name__)


def sort_items(db):
    return dict(sorted(db.items(), key=lambda x: x[0].lower()))


with open("terms.json", encoding="UTF8") as file:
    db = json.load(file)

db = sort_items(db)


@app.route("/")
def home():
    return render_template("home.html", title="Welcome!!")


'''
@app.route('/pesquisa')
def search():
    return render_template('pesquisa.html', title='Terms Search')
'''


@app.route('/terms/search', methods=['GET', 'POST'])
def search():
    search_text = request.form.get('termo')
    if search_text:
        search_text = request.form['termo']
        results = {}
        no_results = {}
        if search_text:
            for term, descr in db.items():
                # if search_text in term or search_text in descr:
                if re.search(search_text, term, flags=re.I) or re.search(search_text, descr, flags=re.I):
                    results[term] = descr
            if not results:
                no_results = {'No search results for': search_text}
        else:
            no_results = {'No search results for': search_text}

        return render_template('pesquisa.html', title='Search', results=results, no_results=no_results)
    else:
        return render_template('pesquisa.html', title='Search')


@app.route('/terms/table')
def table():
    return render_template('tabela.html', title='Medical Terms', terms=db)


@app.route('/terms')
def terms_api():
    return render_template('terms.html', title='Dictionary of terms', designations=db.keys())


@app.route('/terms/<term>')
def terms(term):
    descr = db.get(term, 'Does not exist!')
    return render_template('term.html', title="Description", designation=term, description=descr)


@app.route('/term', methods=["POST"])
def add_terms():
    global db  # Declarar a variável db como global
    term = request.form["designation"]
    descr = request.form["description"]

    if term not in db:
        info_message = "Designation added successfully!"
    else:
        info_message = "The designation '" + term + "' already exists!"

    db[term] = descr
    db = sort_items(db)
    with open("terms.json", 'w') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

    return render_template('terms.html', title='Dictionary of terms', info_message=info_message,
                           designations=db.keys())


@app.route('/term/<term>', methods=["DELETE"])
def delete_term(term):
    desc = db[term]
    if term in db:
        del db[term]
        with open("terms.json", 'w') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)
    else:
        raise KeyError("The term " + term + " does not exist!")
    return {'designation': desc}


app.run(host="localhost", port=3000, debug=True)
