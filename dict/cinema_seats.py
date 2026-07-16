movies = {}
while True:
    movie_and_people = input().split()
    if movie_and_people[0] == 'end':
        break
    movie = movie_and_people[0]
    people = movie_and_people[1]

    movie_exist = False
    for current_movie in movies.keys():
        if current_movie.lower() == movie.lower():
            movie_exist = True
            movie = current_movie
            break

    if not movie_exist:
        movies[movie] = []

    people_exist = False
    for current_people in movies[movie]:
        if current_people.lower() == people.lower():
            people_exist = True
            break

    if not people_exist:
        movies[movie].append(people)

total_movies = len(movies)
total_reservations = sum(len(peoples) for peoples in movies.values())

print('Movies:')
for movie, people in movies.items():
        print(f'{movie} -> {", ".join(people)}')

print(f'Total movies: {total_movies}')
print(f'Total reservations: {total_reservations}')
