space_missions = ["Apollo 11", "Voyager 1", "Mars Rover Curiosity", "Hubble Space Telescope", "International Space Station (ISS)", "Chandra X-ray Observatory", "Mars Pathfinder", "New Horizons", "Gemini Program", "Space Shuttle Program"]
print(space_missions)
print("the 7th index is",space_missions[6])
space_missions[3] = "Apollo 11"
print(space_missions)
del space_missions[5]
print(space_missions)
print("the last index is",space_missions[-1]