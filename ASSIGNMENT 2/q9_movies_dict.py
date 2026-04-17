"""
This program stores details of 3 movies in a dictionary.
"""

movies = {}

for i in range(3):
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    year = input("Enter release year: ")
    rating = input("Enter rating: ")

    movies[title] = {
        "Director": director,
        "Year": year,
        "Rating": rating
    }

for title, details in movies.items():
    print("\nTitle:", title)
    for key, value in details.items():
        print(key + ":", value)