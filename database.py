import sqlite3, hashlib

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		phone TEXT
		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		num INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')

conn.execute('''CREATE TABLE orders
		(orderId INTEGER PRIMARY KEY,
		userId INTEGER,
		productId INTEGER,
		num INTEGER
		)''')



conn.close()

with sqlite3.connect('database.db') as conn:
    cur = conn.cursor()
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (1, 'Men\'s'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (2, 'Women\'s'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (3, 'HeadPhones'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (4, 'Computers'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (5, 'CellPhones'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (6, 'Snacks'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (7, 'Drinks'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (8, 'CookedFoods'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (9, 'Basketball'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (10, 'Tennis'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (11, 'Golf'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (12, 'Clothing'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (13, 'Camping'))
    cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (14, 'Cycling'))
    password = '12345678'
    email = '1023553676@qq.com'
    firstName = 'Admin'
    lastName = 'Tony'
    phone = '10101010'
    cur.execute('''INSERT INTO users (password, email, firstName, lastName, phone) VALUES (?, ?, ?, ?, ?)''', (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, phone))
    password = '12345678'
    email = '1354178359@qq.com'
    firstName = 'Admin2'
    lastName = 'Ben'
    phone = '1010101'
    cur.execute('''INSERT INTO users (password, email, firstName, lastName, phone) VALUES (?, ?, ?, ?, ?)''',
                (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, phone))
    conn.commit()
conn.close()
