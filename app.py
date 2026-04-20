

from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="product_reviews"
)

@app.route('/')
def home():
    return render_template("mainpage.html")


@app.route('/addreview', methods=['POST'])
def add_review():
    rating = request.form.get('rating')
    comment = request.form.get('comment')

    cursor = db.cursor()
    query = "INSERT INTO reviews (rating, comment) VALUES (%s, %s)"
    cursor.execute(query, (rating if rating else None, comment if comment else None))
    db.commit()

    return redirect('/reviews')


@app.route('/reviews')
def get_reviews():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    return render_template("reviews.html", reviews=reviews)


@app.route('/delete/<int:id>')
def delete_review(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM reviews WHERE id = %s", (id,))
    db.commit()
    return redirect('/reviews')

@app.route('/edit/<int:id>')
def edit_review(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reviews WHERE id = %s", (id,))
    review = cursor.fetchone()
    return render_template("edit.html", review=review)


@app.route('/update/<int:id>', methods=['POST'])
def update_review(id):
    rating = request.form.get('rating')
    comment = request.form.get('comment')

    cursor = db.cursor()
    query = "UPDATE reviews SET rating=%s, comment=%s WHERE id=%s"
    cursor.execute(query, (rating, comment, id))
    db.commit()

    return redirect('/reviews')


if __name__ == "__main__":
    app.run(debug=True)

