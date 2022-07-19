from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', name='no name')

@app.route("/<username>")
def hello_world2(username=None):
    return render_template('index.html', name=username)

if __name__ == '__main__':
    Flask.run(app)