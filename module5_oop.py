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


def main():
    n = int(input("Enter N: "))

    number_list = NumberList()

    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        number_list.insert(number)

    x = int(input("Enter X: "))

    print(number_list.search(x))


if __name__ == "__main__":
    main()
