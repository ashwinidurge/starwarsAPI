"""
Create a generator class to produce random numbers
"""

import random


class ProduceChars:
    """Generator class to produce random numbers in a given range"""

    def _init_(self, start, end, limit):
        self.start = start
        self.end = end
        self.limit = limit

    def _iter_(self):
        current = self.start
        while current <= self.limit:
            yield random.randint(self.start, self.end)
            current += 1