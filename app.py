from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        bad_chars = check_ascii(input_text)

        return render_template("index.html", input_text=input_text, bad_chars=bad_chars)
    return render_template("index.html", input_text=None, bad_chars=None)


def check_ascii(testable_string):
    bad_chars = []
    for i, symbol in enumerate(testable_string):
        if not (ord(symbol) in range(0, 127)):
            bad_chars.append((i, symbol))
        print(ord(symbol))
    return bad_chars


@app.route("/result")
def result():
    pass


if __name__ == "__main__":
    app.run(debug=True)
