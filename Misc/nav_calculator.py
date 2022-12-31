from geopy import distance


class Navigation:

    def __init__(self):
        return

    def calculate(self):
        # EARTH_RAD = 6370.97327862273
        # calculates distance between two given points.
        coords_1 = (-30.988137, -64.07792)
        coords_2 = (-32.389563, -63.258858)

        print(distance.distance(coords_1, coords_2).nm)


my_nav = Navigation()
my_nav.calculate()
