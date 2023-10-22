import sqlite3

# Membuka koneksi ke database
conn = sqlite3.connect('premium_users.db')
c = conn.cursor()

# Membuat tabel premium_users
c.execute('''CREATE TABLE premium_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT,
                join_date DATE
            )''')

# Menyimpan perubahan ke database
conn.commit()

# Menutup koneksi ke database
conn.close()
