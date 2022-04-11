from flask import Flask, request, render_template, url_for



app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

from .utils import find_content

@app.route("/<name>")
def hello(name):
    return "hello " +name

@app.route("/")
@app.route("/index/")
def index():
    description = "Connecte-toi à Facebook afin de connaître les résultats !"
    return render_template('index.html',
                       
                         user_name = "TOM",
                        user_image = url_for('static',filename='tmp/cover_111823112767411.jpg'),
                        description = description,
                        blur=True)

@app.route('/result/')
def result():
    gender = request.args.get('gender')
    description= find_content(gender).description
    
    uid = request.args.get('id')
    user_name = request.args.get('first_name')
    user_image = 'http://graph.facebook.com/'+uid+'/picture?type=large'
    return render_template('result.html',
                        user_name = user_name,
                        user_image = user_image,
                        description = description,
                        blur = True
                        )

@app.route('/contents/<content_id>/')
def content(content_id):
    return content_id


if __name__ == "__main__":
    app.run(debug=True)