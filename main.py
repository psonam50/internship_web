from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add')
def add():
    y=10
    z=2200
    x=y+z
    return str(x)

# TypeError: The view function did not return a valid response. \
# The return type must be a string, dict, tuple, Response instance, or WSGI\
#  callable, but it was a int.

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=3000, debug=True)
