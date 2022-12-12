from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "helloworld this is nagalakshmi"

if __name__ == "__main__":
    app.run()
