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
  "imageURL": "/static/img/users/shanil.jpg",
  "linkedinURL": "https://www.linkedin.com/in/shaniljasani/",
  "bio": "Autem ipsum nam porro sldjfasdjflasjdlfkj rerum. Quis eos dolorem eos itaque inventore commodi labore quia quia. Exercitationem repudiandae officiis neque suscipit non officia eaque itaque enim. Voluptatem officia accusantium nesciunt est omnis tempora consectetur dignissimos. Sequi nulla at esse enim cum deserunt eius."
}

demoprofile = {
    "name": "Kabir Barday",
    "title": "CEO of OneTrust",
    "imageURLs": ["https://media.bizj.us/view/img/11897004/kabirbardayheadshot1creditpeytonfulford*1200xx4059-2283-0-942.jpg", "/static/img/users/shanil.jpg"],
    "linkedinURL": "https://www.linkedin.com/in/kbarday/",
    "bio": """Kabir is the Founder, President, and CEO of OneTrust. In under five years, Kabir has grown the company into the #1 fastest growing company on the Inc. 500 and category-defining enterprise technology platform to operationalize trust. According to TCV, OneTrust is the fastest growing enterprise software company in history. OneTrust has largely pioneered the trust technology market, has been awarded 150 patents, and acquired 7 companies along the way.

OneTrust's mission is simple: Use technology to help companies be more trusted, and turn trust into a competitive advantage. Today, OneTrust is used by more than 9,000 companies, both big and small, including over half of the Fortune 500. OneTrust employs 2,000 people in 13 global offices across North America, South America, Asia, Europe, and Australia.

OneTrust has raised $920 million funding round a $5.3 billion valuation from investors Insight Partners, Coatue, TCV, SoftBank Vision Fund 2, and Franklin Templeton.

Kabir oversees all aspects of OneTrust’s product development, operations, and sales internationally. Kabir holds a Fellow of Information Privacy with the IAPP, the highest designation of a privacy professional, and sits on the advisory boards for the Future of Privacy Forum (FPF), the Center of Information Policy Leadership (CIPL), The International Association of Privacy Professionals (IAPP), the Cloud Security Alliance (CSA), and Shared Assessments (known for the SIG third-party risk standard). He has spoken at hundreds of leading industry events globally including Gartner Symposium, Gartner Security & Risk, IAPP Global Privacy Summit, RSA Conference and Infosecurity Europe.

In 2019, Kabir received the National EY Entrepreneur of the Year Award and was named a Most Admired CEO by the Atlanta Business Chronicle. In 2020, with a 48,337% three-year growth rate, OneTrust was named the #1 fastest growing company in America on the Inc. 500.

He holds a B.S. in Computer Science with a certificate in Entrepreneurship from Georgia Institute of Technology. As an Eagle Scout, Kabir has an appreciation for the outdoors, and is also passionate about giving back through the Aga Khan Foundation in their mission to end global poverty."""

}

@app.route('/c/<connector_name>')
def connector_profile(connector_name):
    return render_template("connector.html", connector=demoprofile)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)