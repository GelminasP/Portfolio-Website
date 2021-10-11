from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)
Bootstrap(app)

# set current year for footer
current_year = datetime.now().year


@app.route('/')
def home():
    return render_template("index.html", current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
