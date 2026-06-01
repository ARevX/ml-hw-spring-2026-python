import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Read N
    N = int(input("Enter N: "))

    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Initialize NumPy arrays
    y_true = np.zeros(N, dtype=int)
    y_pred = np.zeros(N, dtype=int)

    # Read N pairs of (x, y)
    for i in range(N):
        x = int(input(f"Enter ground truth class label X for point {i + 1}: "))
        y = int(input(f"Enter predicted class Y for point {i + 1}: "))

        if x not in [0, 1] or y not in [0, 1]:
            print("Error: X and Y must be either 0 or 1.")
            return

        y_true[i] = x
        y_pred[i] = y

    # Compute precision and recall using Scikit-learn
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # Output results
    print("Precision:", precision)
    print("Recall:", recall)

if __name__ == "__main__":
    main()
