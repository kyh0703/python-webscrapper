from flask import Flask, render_template, request, redirect

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/<username>")
def potato(username):
    return f"Hello {username} how are you doing?"


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word)


app.run()
