from unittest.mock import patch

#
# class NavigatorTests(unittest.TestCase):
#     def setUp(self):
#         self.mock_dist_provider = patch('')
#
#     def test_when_created_distance_is_always_zero(self):
#         loc = Location('London')
#         nav = Navigator(loc, self.mock_dist_provider)
#         distance = nav.getDistanceFromDestination()
#         self.assertEqual(distance.inKm(), 0)
#
#     # 2500 miles = 4000 kms
#    def test_distance_is_calculated_in_km(self):
#         self.create_mock_distance(2500)
#         startingPoint = Location("New York City")
#         destination = Location("Los Angeles")
#         nav = Navigator(startingPoint, self.mockDistService)
#         nav.setDestination(destination)
#         distance = nav.get_distance()
#         self.assertEqual(distance.inKm(), 4000)
#
# if __name__ == '__main__':
#     unittest.main()
