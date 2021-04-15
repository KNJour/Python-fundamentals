-- Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
INSERT INTO authors (name, created_at, updated_at) VALUES ("Jane Austen", NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at) VALUES ("Emily Dickenson", NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at) VALUES ("Fyodor Dostoevsky", NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at) VALUES ("William Shakespeare", NOW(), NOW());
INSERT INTO authors (name, created_at, updated_at) VALUES ("Lau Tzu", NOW(), NOW());
-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (name, created_at, updated_at, num_of_pages) VALUES ("C Sharp", NOW(), NOW(), 100);
INSERT INTO books (name, created_at, updated_at, num_of_pages) VALUES ("Java", NOW(), NOW(), 150);
INSERT INTO books (name, created_at, updated_at, num_of_pages) VALUES ("Python", NOW(), NOW(), 200);
INSERT INTO books (name, created_at, updated_at, num_of_pages) VALUES ("PHP", NOW(), NOW(), 176);
INSERT INTO books (name, created_at, updated_at, num_of_pages) VALUES ("Ruby", NOW(), NOW(), 30);
INSERT INTO books.favorites(author_id, book_id)
-- VALUES (1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(4,5);
-- Query: Change the name of the C Sharp book to C#
UPDATE books SET name = "C#" WHERE id = 1;
-- Query: Change the first name of the 4th author to Bill
UPDATE authors SET name = "Bill Shakespeare" WHERE id = 4;
-- Query: Have the first author favorite the first 2 books
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (1, 1, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (1, 2, NOW(), NOW());
-- Query: Have the second author favorite the first 3 books
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (2, 1, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (2, 2, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (2, 3, NOW(), NOW());
-- Query: Have the third author favorite the first 4 books
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (3, 1, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (3, 2, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (3, 3, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (3, 4, NOW(), NOW());
-- Query: Have the fourth author favorite all the books
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (4, 1, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (4, 2, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (4, 3, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (4, 4, NOW(), NOW());
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (4, 5, NOW(), NOW());
-- Query: Retrieve all the authors who favorited the 3rd book
SELECT authors.name AS 'author name' FROM authors
JOIN book_favorites ON authors.id = book_favorites.author_id
JOIN books ON books.id = book_favorites.book_id
WHERE book_id= 3;

DELETE FROM users WHERE id = 4;

-- Query: Remove the first author of the 3rd book's favorites
DELETE FROM book_favorites WHERE book_id = 3 AND author_id = 2;

-- Query: Add the 5th author as an other who favorited the 2nd book
INSERT INTO book_favorites (author_id, book_id, created_at, updated_at) VALUES (5,2,NOW(),NOW());

-- Find all the books that the 3rd author favorited
SELECT books.name AS "3rd authors favorites" FROM books
JOIN book_favorites ON books.id = book_favorites.book_id
JOIN authors on authors.id = book_favorites.author_id
WHERE author_id = 3;

-- Query: Find all the authors that favorited to the 5th book
SELECT authors.name AS "authors Name" FROM authors
JOIN book_favorites ON authors.id = book_favorites.author_id
JOIN books ON books.id = book_favorites.book_id
WHERE book_id = 5;