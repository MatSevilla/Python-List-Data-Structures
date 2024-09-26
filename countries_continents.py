countries_continents = [("United States", "North America"), ("Canada", "North America"), ("Brazil", "South America"), ("United Kingdom", "Europe"), ("Germany", "Europe"), ("China", "Asia"), ("India", "Asia"), ("Australia", "Australia"), ("South Africa", "Africa"), ("Nigeria", "Africa"), ("Russia", "Asia/Europe"), ("Japan", "Asia"), ("Mexico", "North America"), ("Argentina", "South America"), ("Egypt", "Africa")]
print(countries_continents)
print("the 9th index is",countries_continents[8])
countries_continents[9] = "australia"
print(countries_continents)
del countries_continents[-3]
print(countries_continents)
print("the last index is",countries_continents[-1])