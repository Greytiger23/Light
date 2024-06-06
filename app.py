#!/usr/bin/python3


from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from database import store_user_data, store_liked_song, store_playlist, store_recommended_song, get_user_data, get_liked_songs, get_playlist, get_recommended_songs

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    profile_pic = request.form['profile_pic']
    store_user_data(username, password, profile_pic)
    return jsonify({'message': 'User created successfully'})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_data = get_user_data(username)
    if user_data and user_data['password'] == password:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    username = request.args.get('username')
    user_data = get_user_data(username)
    return jsonify(user_data)

@app.route('/get_liked_songs', methods=['GET'])
def get_liked_songs():
    user_id = request.args.get('user_id')
    liked_songs = get_liked_songs(user_id)
    return jsonify(liked_songs)

@app.route('/get_playlist', methods=['GET'])
def get_playlist():
    user_id = request.args.get('user_id')
    playlist = get_playlist(user_id)
    return jsonify(playlist)

@app.route('/get_recommended_songs', methods=['GET'])
def get_recommended_songs():
    user_id = request.args.get('user_id')
    recommended_songs = get_recommended_songs(user_id)
    return jsonify(recommended_songs)


if __name__ == '__main__':
    app.run(debug=True)
