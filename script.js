fetch('/get_user_data')
   .then(response => response.json())
   .then(data => {
        document.getElementById('username').textContent = data.username;
        document.getElementById('profile-pic').src = data.profile_pic;
    });

fetch('/get_liked_songs')
   .then(response => response.json())
   .then(data => {
        const likedSongsList = document.getElementById('liked-songs-list');
        data.forEach(song => {
            const listItem = document.createElement('li');
            listItem.textContent = song.song_name;
            likedSongsList.appendChild(listItem);
        });
    });

fetch('/get_playlist')
   .then(response => response.json())
   .then(data => {
        const playlistList = document.getElementById('playlist-list');
        data.forEach(playlist => {
            const listItem = document.createElement('li');
            listItem.textContent = playlist.playlist_name;
            playlistList.appendChild(listItem);
        });
    });

fetch('/get_recommended_songs')
   .then(response => response.json())
   .then(data => {
        const recommendedSongsList = document.getElementById('recommended-songs-list');
        data.forEach(song => {
            const listItem = document.createElement('li');
            listItem.textContent = song.song_name;
            recommendedSongsList.appendChild(listItem);
        });
    });
