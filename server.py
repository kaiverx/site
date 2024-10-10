from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Kayn", "URL": "/Kayn" },
    { "title": "Malzahar", "URL": "/Malzahar" },
    { "title": "Nunu and Willump", "URL": "/Nunu" },
    { "title": "Глоссарий League of Legend", "URL": "/glossary" },
    { "title": "Сведения об авторе", "URL": "/about_me" }

]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.route("/")
def main():
    return render_template("main.html", name="Главная")

@app.route("/Kayn")
def zeus():
    return render_template("Kayn.html", name="Kayn")


@app.route("/Malzahar")
def wd():
    return render_template("Malzahar.html", name="Malzahar")

@app.route("/Nunu")
def sm():
    return render_template("Nunu.html", name="Nunu and Willump")

@app.route("/glossary")
def glossary():
    return render_template("glossary.html", name="Глоссарий League of Legend")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html", name="Сведения об авторе")

if __name__ == '__main__':
    app.run(debug=True)