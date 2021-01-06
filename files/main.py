from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello There!</h1><img src=\"https://i.ytimg.com/vi/SwB3Bj1NgA8/maxresdefault.jpg\">"

if __name__ == "__main__":
    app.run(host='0.0.0.0')