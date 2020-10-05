import sqlite3
import pathlib

db_name = 'cards.db'
db_file = pathlib.Path(db_name)

if db_file.exists():
    db_file.unlink()
conn = sqlite3.connect(db_name)


c = conn.cursor()

# Create Cards
c.execute('''
CREATE TABLE cards
(id INTEGER ,
 name TEXT,
 img_path TEXT
 )

''')

c.execute(" INSERT INTO cards VALUES(0, 'yamauchi', 'yamauchi.png') ")


# Create Users
c.execute('''
CREATE TABLE users
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 mail TEXT,
 password TEXT
 )

''')
c.execute(" INSERT INTO users VALUES(0, 'yamauchi', 'mews@mews-base.com', 'hoge') ")


# Create Decks
c.execute('''
CREATE TABLE decks
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 owner_id INTEGER,
 card_id INTEGER,
 count INTEGER
 )

''')
c.execute("INSERT INTO decks VALUES(0, 0, 0, 40)")

conn.commit()
conn.close()
