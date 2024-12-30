from flask import Flask
import webbrowser
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Я той, хто вам потрібний ))</h1>"

def open_browser():
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(host="0.0.0.0", port=5000)
