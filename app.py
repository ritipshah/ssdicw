from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# create database
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sapid TEXT,
        age INTEGER,
        marks INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        sapid = request.form["sapid"]
        age = request.form["age"]
        marks = request.form["marks"]

        conn = sqlite3.connect("students.db")
        c = conn.cursor()

        c.execute(
        "INSERT INTO students(name,sapid,age,marks) VALUES(?,?,?,?)",
        (name,sapid,age,marks)
        )

        conn.commit()
        conn.close()

    return render_template("app.html")


@app.route("/search", methods=["POST"])
def search():

    name = request.form["search_name"]

    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    c.execute("SELECT * FROM students WHERE name=?", (name,))
    data = c.fetchall()

    conn.close()

    return render_template("app.html", data=data)


if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app.html")

@app.route("/search", methods=["POST"])
def search():
    name = request.form["search_name"]

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", (name,))
    data = cursor.fetchall()
    conn.close()

    return render_template("app.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)