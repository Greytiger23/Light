Script.js// script.js
const signupForm = document.getElementById('signup-form');
const loginForm = document.getElementById('login-form');
const likeSongForm = document.getElementById('like-song-form');
const likedSongsList = document.getElementById('liked-songs-list');
const recommendedSongsList = document.getElementById('recommended-songs-list');

signupForm.addEventListener('submit', (e) => {
	e.preventDefault();
	const username = document.getElementById('username').value;
	const password = document.getElementById('password').value;
	fetch('/signup', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ username, password })
		        })
	   .then(response => response.json())
	   .then(data => console.log(data))
	   .catch(error => console.error(error));
});

loginForm.addEventListener('submit', (e) => {
	e.preventDefault();
	const username = document.getElementById('username').value;
	const password = document.getElementById('password').value;
fetch('/login', {
	method: 'POST',
	headers: { 'Content-Type': 'application/json' },
	body: JSON.stringify({ username, password })
})
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(error => console.error(error));
});

likeSongForm.addEventListener('submit', (e) => {
	e.preventDefault();
	const user_id = 1; // Replace with actual user ID
	const song_id = document.getElementById('song-id').value;
fetch('/like_song', {
	method: 'POST',
	headers: { 'Content-Type': 'application/json' },
	body: JSON.stringify({ user_id, song_id })
})
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(error => console.error(error));
});
fetch('/get_recommendations?user_id=1') // Replace with actual user ID
	.then(response => response.json())
	.then(data => {
const recommendations = data.recommendations;
recommendedSongsList.innerHTML = '';
recommendations.forEach((song) => {
	const li = document.createElement('li');
	li.textContent = song.name + 'y ' song.artist;
	recommendedSongsList.appendChild(li);
			        });
	     })
  .catch(error => console.error(error));
  
const animatedBackground = document.querySelector('.animated-background');

function updateBackground() {
		const time = new Date();
		const hour = time.getHours();
		const minute = time.getMinutes();
		const second = time.getSeconds();

		const hourRotation = 30 * hour + minute / 2;
		const minuteRotation = 6 * minute;
		const secondRotation = 6 * second;

animatedBackground.style.backgroundPosition = `${secondRotation}deg ${hourRotation}deg`;
}
setInterval(updateBackground, 1000);
