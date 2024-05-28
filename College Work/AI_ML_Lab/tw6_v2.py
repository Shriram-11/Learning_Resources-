import numpy as np
'''
Tried to something different, not advisable for termwork
'''

class Perceptron:
    def __init__(self, num_features, learning_rate=0.2, epochs=100):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.epochs = epochs
        # Initializing weights randomly between -1 and 1
        self.weights = np.array([-0.2, 0.4])

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights)
        return self.activation_function(summation)

    def fit(self, X, y):
        mse_history = []
        print("Initial Weights:", self.weights)
        for epoch in range(self.epochs):
            total_error = 0
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                error = label - prediction
                total_error += error ** 2
                self.weights += self.learning_rate * error * inputs
            mse = total_error / len(y)
            mse_history.append(mse)
            print(f"Epoch {epoch + 1}: MSE = {mse}")
            if mse == 0:
                print("Training converged. Stopping early.")
                break
        return mse_history


# Define the training data for the OR function
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 1, 1, 1])  # OR logic gate

# Create a Perceptron instance
perceptron = Perceptron(num_features=2)

# Train the perceptron and get MSE history
mse_history = perceptron.fit(X, y)

# Test the perceptron with the training data
print("\nPredictions on the training data:")
for inputs in X:
    print(f"Input: {inputs}, Predicted Output: {perceptron.predict(inputs)}")

# Print the final state of the neural network
print("\nFinal Neural Network Weights:")
print(perceptron.weights)
