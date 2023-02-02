import sqlite3

def create_db():
    conn = sqlite3.connect("glycemic_index.db")
    c = conn.cursor()

    c.execute(
        "CREATE TABLE IF NOT EXISTS meals (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)"
    )

    c.execute(
        "CREATE TABLE IF NOT EXISTS ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, glycemic_index INTEGER NOT NULL)"
    )

    c.execute(
        "CREATE TABLE IF NOT EXISTS meal_ingredients (meal_id INTEGER NOT NULL, ingredient_id INTEGER NOT NULL, quantity INTEGER NOT NULL, FOREIGN KEY (meal_id) REFERENCES meals(id), FOREIGN KEY (ingredient_id) REFERENCES ingredients(id), PRIMARY KEY (meal_id, ingredient_id))"
    )

    c.execute(
        "CREATE TABLE panier ( id INTEGER PRIMARY KEY,meal_id INTEGER NOT NULL,quantity INTEGER NOT NULL,glycemic_index REAL NOT NULL,FOREIGN KEY (meal_id) REFERENCES meals (id));"
    )

    conn.commit()
    conn.close()

create_db()

def insert_data():
    conn = sqlite3.connect("glycemic_index.db")
    c = conn.cursor()

    c.execute("INSERT INTO meals (name) VALUES ('Pizza')")
    c.execute("INSERT INTO meals (name) VALUES ('Lasagne')")
    c.execute("INSERT INTO meals (name) VALUES ('Bolognaise')")

    c.execute("INSERT INTO ingredients (name, glycemic_index) VALUES ('Bread', 75)")
    c.execute("INSERT INTO ingredients (name, glycemic_index) VALUES ('Rice', 73)")
    c.execute("INSERT INTO ingredients (name, glycemic_index) VALUES ('Potatoes', 85)")

    c.execute("INSERT INTO meal_ingredients (meal_id, ingredient_id, quantity) VALUES (1, 1, 2)")
    c.execute("INSERT INTO meal_ingredients (meal_id, ingredient_id, quantity) VALUES (2, 2, 1)")
    c.execute("INSERT INTO meal_ingredients (meal_id, ingredient_id, quantity) VALUES (3, 3, 3)")

    c.execute("INSERT INTO panier (id, meal_id, quantity, glycemic_index) VALUES (1, 1, 2, 40)")
    c.execute("INSERT INTO panier (id, meal_id, quantity, glycemic_index) VALUES (2, 2, 4, 192)")
    c.execute("INSERT INTO panier (id, meal_id, quantity, glycemic_index) VALUES (3, 3, 1, 32)")

    conn.commit()
    conn.close()

insert_data()

