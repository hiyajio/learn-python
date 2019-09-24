playlist = {
	'title': 'Indie',
	'author': 'jiyooo',
	'songs': [
		{'title': 'Sweet Disposition', 'artist': ['The Temper Trap'], 'duration': 3.51},
		{'title': 'Painting (Masterpiece)', 'artist': ['Lewis Del Mar'], 'duration': 4.04},
		{'title': 'broken', 'artist': ['lovelytheband'], 'duration': 3.25},
		{'title': 'Anna Sun', 'artist': ['WALK THE MOON'], 'duration': 5.21}
	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']

print(total_length)