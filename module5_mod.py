class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        for index, number in enumerate(self.numbers):
            if number == x:
                return index + 1
        return -1
