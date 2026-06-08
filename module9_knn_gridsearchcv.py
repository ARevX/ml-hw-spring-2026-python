import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Read training set size
N = int(input("Enter N, the number of training pairs: "))

# Initialize training data
X_train = np.empty((N, 1), dtype=float)
y_train = np.empty(N, dtype=int)

# Read training pairs
for i in range(N):
    x = float(input(f"Enter x value for training pair {i + 1}: "))
    y = int(input(f"Enter y value for training pair {i + 1}: "))

    X_train[i, 0] = x
    y_train[i] = y

# Read test set size
M = int(input("Enter M, the number of test pairs: "))

# Initialize test data
X_test = np.empty((M, 1), dtype=float)
y_test = np.empty(M, dtype=int)

# Read test pairs
for i in range(M):
    x = float(input(f"Enter x value for test pair {i + 1}: "))
    y = int(input(f"Enter y value for test pair {i + 1}: "))

    X_test[i, 0] = x
    y_test[i] = y

best_k = 1
best_accuracy = 0.0

# Try k values from 1 to 10
# k cannot be larger than the number of training samples
max_k = min(10, N)

for k in range(1, max_k + 1):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

print("Best k:", best_k)
print("Test accuracy:", best_accuracy)
