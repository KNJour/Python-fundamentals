-- Query: Create 3 new dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Cobra Kai", NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("Johnny Quest's Mystery School", NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("Coding Hobo's Coding Dojo", NOW(), NOW());
 -- Query: Delete the 3 dojos you just created
 DELETE FROM dojos WHERE id = 1 or id = 2 or id = 3;
-- Query: Create 3 more dojos
INSERT INTO dojos (name, created_at, updated_at) VALUES ("Totally Real DOJO", NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("banana School", NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("Shattered Dreams dojo for gifted youngsters", NOW(), NOW());
-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Fred", "FlintStone", "40", 5, NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("George", "Pancakes", "22", 5, NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Jimminy", "Cricket", "31", 5, NOW(), NOW());
-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Charlie", "Chaplin", "63", 4, NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Mark", "Twain", "82", 4, NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Ricky", "Bobby", "24", 4, NOW(), NOW());
-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Edgar", "Poe", "28", 6, NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Larry", "Davis", "21", 6, NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES ("Daniel", "Brewsbury", "18", 6, NOW(), NOW());
-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 4;
-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 6;
-- Query: Retrieve the last ninja's dojo
SELECT name FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id 
WHERE ninjas.id = 9;
SELECT * FROM dojos
SELECT * FROM ninjas