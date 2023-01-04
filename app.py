import secrets

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["text_field"]
        bad_chars = check_ascii(input_text)

        session['input_text'] = input_text
        session['bad_chars'] = bad_chars

        return redirect('/result')
    return render_template("index.html")


def check_ascii(testable_string):
    bad_chars = {}
    for i, symbol in enumerate(testable_string):
        if not (ord(symbol) in range(0, 127)):
            bad_chars[i] = symbol
    return bad_chars


@app.route("/result")
def result():
    if len(session['bad_chars']) > 0:
        return render_template('result.html', bad_chars=session['bad_chars'].items(), input_text=session['input_text'])
    else:
        return render_template('no_chars.html', input_text=session['input_text'])


if __name__ == "__main__":
    app.run(debug=True)
