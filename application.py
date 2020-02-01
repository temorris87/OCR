from flask import Flask

application = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    application.run(debug=True)
