from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pyshorteners

app = Flask(__name__)
    

@app.route("/", methods=['POST', 'GET'])
def index():
     if request.method == "POST":
           url_received = request.form["url_request"]
           if url_received:
               shurl = pyshorteners.Shortener()
               shorten_url = shurl.tinyurl.short(url_received)
               return render_template("urlsh.html", sh_url=shorten_url)
           else:
               return render_template("index.html")
     else:
         return render_template("index.html")
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)