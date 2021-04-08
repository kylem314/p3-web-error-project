class primeCheck:

    def __init__(self, input):
        self._input = input
        self._primes = []
        self._composites = []

    @property
    def checking(self):
        cycles = self._number
        # We must check every number in the range input
        for i in range(cycles):
            # Start counting at 2, as 1 is neither prime nor composite
            if i >= 2:
                for x in range(2, i):
                    # If the checked number has a factor, append to composite list
                    if (i % x) == 0:
                        self._composites.append(i)
                        break
                    else:
                        # If the checked number does not have a factor other than 1, append to prime list
                        self._primes.append(i)

    @property
    def count(self):
        return self._input

    @property
    def primes(self):
        return self._primes

    @property
    def composites(self):
        return self._composites

if __name__ == "__main__":
    n = 1
    primeCheck = primeCheck(1)