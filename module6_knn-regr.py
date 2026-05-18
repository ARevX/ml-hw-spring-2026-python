import numpy as np


class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.points = None

    def insert_data(self, points):
        self.points = np.array(points, dtype=float)

    def predict(self, x_input):
        x_values = self.points[:, 0]
        y_values = self.points[:, 1]

        distances = np.abs(x_values - x_input)

        nearest_indices = np.argsort(distances)[:self.k]

        nearest_y_values = y_values[nearest_indices]

        prediction = np.mean(nearest_y_values)

        return prediction


def main():
    N = int(input("Enter N: "))
    k = int(input("Enter k: "))

    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    if k <= 0:
        print("Error: k must be a positive integer.")
        return

    points = np.empty((N, 2))

    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))

        points[i, 0] = x
        points[i, 1] = y

    X = float(input("Enter X for prediction: "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    model = KNNRegression(k)
    model.insert_data(points)

    Y = model.predict(X)

    print("Predicted Y:", Y)


main()
