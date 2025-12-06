from flask import Flask, render_template, request, redirect, session
from models import db, User, Book
import requests

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if not User.query.filter_by(username="admin").first():
        user = User(username="admin", password="admin")
        db.session.add(user)
        db.session.commit()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if user:
            session["user_id"] = user.id
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect("/")

    if request.method == "POST":
        isbn = request.form["isbn"]
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(url)
        data = response.json()

        try:
            book_info = data["items"][0]["volumeInfo"]
            title = book_info.get("title", "N/A")
            author = book_info.get("authors", ["N/A"])[0]
            pages = book_info.get("pageCount", 0)
            rating = book_info.get("averageRating", 0)

            book = Book(
                title=title,
                author=author,
                page_count=pages,
                rating=rating,
                user_id=session["user_id"]
            )

            db.session.add(book)
            db.session.commit()

        except:
            pass

    books = Book.query.filter_by(user_id=session["user_id"]).all()
    return render_template("dashboard.html", books=books)

@app.route("/delete/<int:id>")
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
