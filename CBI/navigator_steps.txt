# We want to build a navigator
# It can tell us the distance between where we are and we want to go
# It reports the distance in km
# We can tell it to drive there
# We have a dependency on 3rd party distance calculator that reports the distance in miles

class Location:
    def __init__(self, city):
        self.city = city

class Navigator:

    def __init__(self, distance_provider):
        self.distance_provider = distance_provider

    def set_origin(self, city):
        self.origin = Location(city)

    def get_distance_to(self, destination)
        distance_in_miles = self.calculate_distance(destination)
        distance_in_km = self.convert_to_km(distance_in_miles)
        return distance_in_km

    def calculate_distance(self, distance_provider, destination):
        pass

    def convert_to_km(self, distance_in_miles):
        pass



# start with get_distance
# local locations
# origin, target should be strings first, then location objects
# ctor == __init__
# calculate functions, then make them self. Leave empty
# decide where to set origin, could be ctor or changable
# decide where to set destination
# decide where to pass distance_provider
