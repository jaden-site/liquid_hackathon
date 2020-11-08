from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template('my-form.html')

@app.route('/', methods = ['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = int(text)
    lunch_time = processed_text + 5
    return str(lunch_time)

if __name__ == "__main__":
    app.run(debug=True)
