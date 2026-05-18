import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Read N
N = int(input("Enter N: "))

# Read k
k = int(input("Enter k: "))

# Initialize NumPy arrays
X_train = np.empty((N, 1))
y_train = np.empty(N)

# Read N points
for i in range(N):
    x = float(input(f"Enter x value for point {i + 1}: "))
    y = float(input(f"Enter y value for point {i + 1}: "))

    X_train[i, 0] = x
    y_train[i] = y

# Read input X for prediction
X = float(input("Enter X for prediction: "))

# Check if k <= N
if k <= N:
    # Create and train k-NN regression model
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Predict Y
    X_test = np.array([[X]])
    y_pred = model.predict(X_test)

    # Calculate variance of labels
    variance = np.var(y_train)

    print("Predicted Y:", y_pred[0])
    print("Variance of labels:", variance)
else:
    print("Error: k cannot be greater than N.")
