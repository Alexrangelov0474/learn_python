movies = {}

while True:
    line = input().split()
    if line[0] == 'end':
        break
    movie = line[0]
    rating = int(line[1])
    if movie not in movies:
        movies[movie] = rating
    elif rating > movies[movie]:
        movies[movie] = rating

highest_score = max(movies.values())
total_movies = len(movies)
print('Players')
for movie, rating in movies.items():
    print(f'{movie}: {rating}')
print(f'Highest score: {highest_score}')
print(f'Total movies: {total_movies}')