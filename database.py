import sqlite3

# Create a connection to the database
conn = sqlite3.connect('music_recommendations.db')
        cursor = conn.cursor()

# Create tables for users, liked songs, playlists, and recommended songs
cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        profile_pic TEXT
    )
    ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS liked_songs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        song_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS playlists (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        playlist_name TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommended_songs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        song_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
     )
    ''')

# Function to store user data from signup form
def store_user_data(username, password, profile_pic):
    cursor.execute('INSERT INTO users (username, password, profile_pic) VALUES (?, ?, ?)', (username, password, profile_pic))
    conn.commit()

# Function to store liked songs
def store_liked_song(user_id, song_id):
    cursor.execute('INSERT INTO liked_songs (user_id, song_id) VALUES (?, ?)', (user_id, song_id))
    conn.commit()

# Function to store playlist
def store_playlist(user_id, playlist_name):
    cursor.execute('INSERT INTO playlists (user_id, playlist_name) VALUES (?, ?)', (user_id, playlist_name))
    conn.commit()

# Function to store recommended songs
def store_recommended_song(user_id, song_id):
    cursor.execute('INSERT INTO recommended_songs (user_id, song_id) VALUES (?, ?)', (user_id, song_id))
    conn.commit()

# Function to get user data from database
def get_user_data(username):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    return cursor.fetchone()

# Function to get liked songs from database
def get_liked_songs(user_id):
    cursor.execute('SELECT * FROM liked_songs WHERE user_id = ?', (user_id,))
    return cursor.fetchall()

# Function to get playlist from database
def get_playlist(user_id):
    cursor.execute('SELECT * FROM playlists WHERE user_id = ?', (user_id,))
    return cursor.fetchall()

def get_recommended_songs(user_id):
    cursor.execute('SELECT * FROM recommended_songs WHERE user_id = ?', (user_id,))
    return cursor.fetchall()
