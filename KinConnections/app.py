from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

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

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)