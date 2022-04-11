from flask import Flask



app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route("/<name>")
def hello(name):
    return "hello " +name



if __name__ == "__main__":
    app.run(debug=True)