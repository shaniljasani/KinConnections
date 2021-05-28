import os

from flask import Flask, render_template, session
from auth.auth import auth_bp
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.getenv("APP_SECRET")
app.register_blueprint(auth_bp)

# redirect on trailing slashes
@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path 
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# the home/main page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

shaniluser = {
  "name": "Shanil Jasani",
  "title": "Super Cool Dude",
  "imageURL": "/shanil.jpg",
  "linkedinURL": "https://www.linkedin.com/in/shaniljasani/",
  "bio": "Autem ipsum nam porro sldjfasdjflasjdlfkj rerum. Quis eos dolorem eos itaque inventore commodi labore quia quia. Exercitationem repudiandae officiis neque suscipit non officia eaque itaque enim. Voluptatem officia accusantium nesciunt est omnis tempora consectetur dignissimos. Sequi nulla at esse enim cum deserunt eius."
}

@app.route('/c/<connector_name>')
def connector_profile(connector_name):
    return render_template("connector.html", connector=shaniluser)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)