from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/direct')
def direct():
    return render_template('direct.html')

@app.route('/anchor')
def anchor():
    return render_template('anchor.html')

@app.route('/paper')
def paper():
    return render_template('paper.html')

if __name__ == "__main__":
    app.run(debug=True)  


