class Location:
    pass


class DistanceCalculator:
    pass


class Navigator:
    def get_distance(self,  distance_provider):
        origin = Location("New York")
        target = Location("Los Angeles")
        distance_calculator =  DistanceCalculator()
        distance_calculator.setStartPoint(origin)
        distance_calculator.setDestination(target)
        distance_in_miles = distance_provider.get_distance()
        return distance_calculator.get_in_km(distance_in_miles)

    def setStartPoint(self, origin):
        pass

    def setDestination(self, target):
        pass

    # start with get_distance
    # origin, target should be strings first, then location objects
    # then set origin, then decide if you want it here, or as part of navigate
    # provider is external service, in miles
    # get the calculator from outside?
