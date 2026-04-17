"""
This program searches for a country in a list.
"""

def search_country(countries, target):
    if target in countries:
        return countries.index(target)
    else:
        return "Not Found in List"

countries = input("Enter countries separated by comma: ").split(",")
target = input("Enter country to search: ")

print(search_country(countries, target))