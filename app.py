from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",       # will change to Cloud SQL later
    user="bookadmin",
    password="bookadmin",
    database="bookstore"
)
cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
