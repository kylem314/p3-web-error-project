import random
"""List of heroes"""
herolist1 = ["Spider-Man", "Captain America", "Iron Man", "The Hulk", "Thor", "Antman", "Black Widow", "Deadpool", "Wolverine", "Black Panther", "Star Lord", "Hawkeye"]

"""Algorithm of selecting heroes in a class"""
class Marvel:
    """Initializer of class takes series parameter and returns class objects"""
    def __init__(self, series):

        """Built in validation and exception"""
        if series < 0 or series > 11:
            raise ValueError('Series has to be between 1 and 11')
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0

        self.hero_series()

    """Algorithm for building sequence, this id called from __init__"""
    def hero_series(self):
        limit = self._series
        f = [(random.sample((herolist1), k=self._series))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= self.series

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]

# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    a = 1
    '''Constructor of Class object'''
    heroes = Marvel(a/a)
    print(f"A great superhero from Marvel is {heroes.list}")