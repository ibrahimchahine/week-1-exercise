def weather_by_precipitation(precipitation):
    if precipitation < 20:
        return 'low'
    elif precipitation in range(20, 50):
        return 'medium'
    elif precipitation in range(50, 100):
        return 'high'
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
        if self.weather == weather:
            num+=1
        if self.water == water:
            num+=1
        if self.wind == wind:
            num+=1
        if self.snow_level == snow_level:
            num+=1
        return num

tree = Plant('tree' ,'clouds', 'medium', 'no', 'high')
shrubs = Plant('shrubs' , 'sun','high','yes', 'medium')
herb = Plant('herb', 'sun','low','no', 'high')

weather = input("How is the weather today? sun or clouds: ")
precipitation = input("What is the precipitation number? ")
windy = input("Is it windy? yes or no: ")

best_match = tree
tree_data = (tree.compare_plants(weather, precipitation, windy, None), tree.name)
shrubs_data = (shrubs.compare_plants(weather, precipitation, windy, None), shrubs.name)
herb_data =  (herb.compare_plants(weather, precipitation, windy, None), herb.name)
arr = [tree_data, shrubs_data, herb_data]

arr.sort();
print(arr[len(arr)-1][1])
