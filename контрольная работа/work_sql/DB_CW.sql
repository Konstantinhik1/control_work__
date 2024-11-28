USE mans_friends;

CREATE TABLE AllAnimals (
    id SERIAL PRIMARY KEY,
    original_id INT,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    age VARCHAR(50) NOT NULL,
    breed VARCHAR(100),
    commands TEXT,
    origin_table VARCHAR(50),
    type VARCHAR(50)
);


CREATE TABLE YoungAnimals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    age VARCHAR(50) NOT NULL
);

CREATE TABLE PackAnimalsUnified (
id SERIAL PRIMARY KEY,
pack_animal_id INT REFERENCES PackAnimals(id),
type VARCHAR(50),
breed VARCHAR(100),
commands TEXT
); 

 CREATE TABLE YoungAnimals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    age_in_months INT NOT NULL
);

CREATE TABLE YoungAnimals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    age VARCHAR(50) NOT NULL
);

CREATE TABLE AllAnimals (
    id SERIAL PRIMARY KEY,
    original_id INT,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    age VARCHAR(50) NOT NULL,
    breed VARCHAR(100),
    commands TEXT,
    origin_table VARCHAR(50),
    type VARCHAR(50)
);



CREATE TABLE Donkeys (
    id SERIAL PRIMARY KEY,
    pack_animal_id INT REFERENCES PackAnimals(id),
    breed VARCHAR(100),
    commands TEXT
);

INSERT INTO Donkeys (pack_animal_id, breed, commands)
VALUES 
    (3, 'Miniature', 'Carry,Walk');


   CREATE TABLE Animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL
);

INSERT INTO Animals (name, species, date_of_birth)
VALUES 
    ('Rex', 'Dog', '2020-03-01'),
    ('Mittens', 'Cat', '2019-06-12'),
    ('Hammy', 'Hamster', '2021-07-24'),
    ('Thunder', 'Horse', '2018-05-18'),
    ('Cammie', 'Camel', '2017-09-30'),
    ('Donny', 'Donkey', '2016-11-05');


CREATE TABLE PetAnimals (
    id SERIAL PRIMARY KEY,
    animal_id INT REFERENCES Animals(id)
);

INSERT INTO PetAnimals (animal_id)
VALUES 
    (1), -- Rex
    (2), -- Mittens
    (3); -- Hammy

CREATE TABLE PackAnimals (
    id SERIAL PRIMARY KEY,
    animal_id INT REFERENCES Animals(id)
);

INSERT INTO PackAnimals (animal_id)
VALUES 
    (4), -- Thunder
    (5), -- Cammie
    (6); -- Donny

CREATE TABLE Dogs (
    id SERIAL PRIMARY KEY,
    pet_animal_id INT REFERENCES PetAnimals(id),
    breed VARCHAR(100),
    commands TEXT
);

INSERT INTO Dogs (pet_animal_id, breed, commands)
VALUES 
    (1, 'Labrador', 'Sit,Stay,Fetch');

CREATE TABLE Cats (
    id SERIAL PRIMARY KEY,
    pet_animal_id INT REFERENCES PetAnimals(id),
    breed VARCHAR(100),
    commands TEXT
);

INSERT INTO Cats (pet_animal_id, breed, commands)
VALUES 
    (2, 'Siamese', 'Jump,Climb');

CREATE TABLE Hamsters (
    id SERIAL PRIMARY KEY,
    pet_animal_id INT REFERENCES PetAnimals(id),
    breed VARCHAR(100),
    commands TEXT
);

INSERT INTO Hamsters (pet_animal_id, breed, commands)
VALUES 
    (3, 'Syrian', 'Run in wheel');

CREATE TABLE Horses (
    id SERIAL PRIMARY KEY,
    pack_animal_id INT REFERENCES PackAnimals(id),
    breed VARCHAR(100),
    commands TEXT
);

INSERT INTO Horses (pack_animal_id, breed, commands)
VALUES 
    (1, 'Arabian', 'Gallop,Jump');

CREATE TABLE Camels (
    id SERIAL PRIMARY KEY,
    pack_animal_id INT REFERENCES PackAnimals (id),
    breed VARCHAR(100)
);

INSERT INTO Camels (pack_animal_id, breed, commands)
VALUES 
    (2, 'Dromedary', 'Sit,Stand');
    



