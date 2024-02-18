def weather_by_precipitation(precipitation):
    if precipitation < 20:
        return "low"
    elif precipitation in range(20, 50):
        return "medium"
    elif precipitation in range(50, 100):
        return "high"
    return 0


class Plant:
    def __init__(self, name, weather, water, wind, snow_level):
        self.name = name
        self.weather = weather
        self.water = water
        self.wind = wind
        self.snow_level = snow_level

    def compare_plants(self, weather, water, wind, snow_level):
        num = 0
        is_dead = False
        if self.weather == weather:
            num += 1
        if self.water == water:
            num += 1
        if self.wind == wind:
            num += 1
        if self.snow_level >= snow_level:
            is_dead = True
        return num, is_dead


tree = Plant("tree", "clouds", "medium", "no", 3)
shrubs = Plant("shrubs", "sun", "high", "yes", 2)
herb = Plant("herb", "sun", "low", "no", 3)

weather = input("How is the weather today? sun or clouds: ")
precipitation = input("What is the precipitation number? ")
windy = input("Is it windy? yes or no: ")
snow_level = int(input("Is it snowing? how much from 1 to 3? "))

best_match = tree
rank, is_dead = tree.compare_plants(weather, precipitation, windy, snow_level)
tree_data = (rank, is_dead, tree.name)
rank, is_dead = t = shrubs.compare_plants(weather, precipitation, windy, snow_level)
shrubs_data = (rank, is_dead, shrubs.name)
rank, is_dead = herb.compare_plants(weather, precipitation, windy, snow_level)
herb_data = (rank, is_dead, herb.name)
arr = [tree_data, shrubs_data, herb_data]
arr.sort()
print("The best match is " + arr[len(arr) - 1][2])
for plant in arr:
    if plant[1]:
        print(plant[2] + " will die from snow")
