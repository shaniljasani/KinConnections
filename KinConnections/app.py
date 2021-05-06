from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('kc_template.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)