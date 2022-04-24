from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "Install", "url": "install-flask"},
       {"name": "The first site", "url": "first-app"},
       {"name": "Feedback", "url": "contact"}]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html',  menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", title="About website", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def profile():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", title="Feedback", menu=menu )


if __name__ == '__main__':
    app.run(debug=True)