from module5_mod import NumberList


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
