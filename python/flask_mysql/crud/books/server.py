from flask import Flask, render_template, request,session,redirect, flash

from mysqlconnection  import connectToMySQL
app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."
#SHOW
## ADD TO BOOKS
@app.route('/add_favorite_from_books', methods = ['POST'])
def add_favorite_from_books():
    query = "INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (%(author_id)s, %(book_id)s, NOW(),NOW());"
    data ={
        "book_id": request.form['id'],
        "author_id": request.form['author']
    }
    result = connectToMySQL("authors_books").query_db(query, data)
    print("HHEEEEEERRREE")
    print(data)
    return redirect (f"/bookShow/{request.form['id']}")

@app.route('/add_favorite_from_author', methods = ['POST'])
def add_favorite_from_author():
    query = "INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (%(author_id)s, %(book_id)s, NOW(),NOW());"
    data ={
        "book_id": request.form['book'],
        "author_id": request.form['id']
    }
    result = connectToMySQL("authors_books").query_db(query, data)
    print("HHEEEEEERRREE")
    print(data)
    return redirect (f"/authorshow/{data['author_id']}")


#SHOW AUTHORS FAVORITES
@app.route('/authorshow/<int:author_id>')
def authorShow(author_id):
    query = "SELECT * FROM books JOIN book_favorites ON books.id = book_favorites.book_id JOIN authors ON authors.id = book_favorites.author_id WHERE author_id = %(author_id)s;"
    data = {
        "author_id": author_id
    }
    query3 = "SELECT * FROM authors WHERE id = %(author_id)s;"
    author = connectToMySQL("authors_books").query_db(query3,data)
    query2 = "SELECT * FROM books"
    books = connectToMySQL("authors_books").query_db(query2,data)

    favorites = connectToMySQL("authors_books").query_db(query,data)
    print(favorites)
    return render_template("author_show.html", favorites = favorites, books = books, author = author)

#SHOW BOOKS 
@app.route('/bookShow/<int:book_id>')
def bookShow(book_id):
    data = {
        "book_id": book_id
    }
    query = "SELECT authors.name AS 'author_name' FROM authors JOIN book_favorites ON authors.id = book_favorites.author_id JOIN books ON books.id = book_favorites.book_id WHERE book_id = %(book_id)s;"
    query2 = "SELECT * FROM authors"
    authors = connectToMySQL("authors_books").query_db(query2,data)
    authorFavorites = connectToMySQL("authors_books").query_db(query,data)
    print(authorFavorites)

    #just book name
    query3 = "SELECT * FROM books WHERE id = %(book_id)s"
    book_name = connectToMySQL("authors_books").query_db(query3,data)
    print(book_name)

    return render_template("book_show.html", authorFavorites = authorFavorites, authors = authors, book_name = book_name)

# ROUTE FOR DISPLAYING AND CREATING AUTHORS
@app.route('/create_author', methods=['POST'])
def create_author():
    mysql = connectToMySQL("authors_books")
    query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());"
    print(query)
    data = {
        "name": request.form['author_name']
    }
    new_author_id = mysql.query_db(query, data)
    return redirect ("/author")

@app.route('/author')
def author():
    query = "SELECT * FROM authors;"
    authors = connectToMySQL('authors_books').query_db(query)
    return render_template("authors.html", all_authors = authors)

# ROUTE FOR DISPLAYING AND CREATING BOOKS
@app.route('/create_book', methods=['POST'])
def create_book():
    mysql = connectToMySQL("authors_books")
    query = "INSERT INTO books (name, created_at, updated_at, num_of_pages) VALUES (%(name)s,NOW(),NOW(), %(pages)s);"
    print(query)
    data = {
        "name": request.form['book_name'],
        "pages": request.form['pages']
    }
    new_book_id = mysql.query_db(query, data)
    return redirect ("/books")

@app.route('/books')
def books():
    query = "SELECT * FROM books;"
    books = connectToMySQL('authors_books').query_db(query)
    return render_template("books.html", all_books = books)

if __name__=="__main__":
    app.run(debug=True)