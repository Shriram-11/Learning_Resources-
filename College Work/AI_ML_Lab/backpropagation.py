
import numpy as np

# Activation function: Sigmoid


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function


def sigmoid_derivative(x):
    return x * (1 - x)


class SimpleNeuralNetwork:
    def __init__(self, weights, X, y, lr=1):
        # Weights between input layer and hidden layer
        self.X = X
        self.y = y
        self.lr = lr
        self.w13 = weights['w13']
        self.w14 = weights['w14']
        self.w23 = weights['w23']
        self.w24 = weights['w24']

        # Weights between hidden layer and output layer
        self.w35 = weights['w35']
        self.w45 = weights['w45']

    def forward(self):
        # Forw
        a3 = self.X[0]*self.w13 + self.X[1]*self.w23
        self.y3 = sigmoid(a3)
        a4 = self.X[0]*self.w14 + self.X[1]*self.w24
        self.y4 = sigmoid(a4)
        a5 = self.y3*self.w35 + self.y4*self.w45
        self.y5 = sigmoid(a5)
        return self.y5

    def backward(self, output):
        # Calculate the error
        error = self.y - output
        d5 = error * sigmoid_derivative(output)

        # Calculate error for hidden layer
        d3 = d5*self.w35*sigmoid_derivative(self.y3)
        d4 = d5*self.w45*sigmoid_derivative(self.y4)

        # Update weights
        self.w35 += self.y3*d5*self.lr
        self.w45 += self.y4*d5*self.lr
        # hidden layer
        self.w13 += self.X[0]*d3*self.lr
        self.w14 += self.X[0]*d4*self.lr
        self.w23 += self.X[1]*d3*self.lr
        self.w24 += self.X[1]*d4*self.lr

    def train(self, epochs=10000):
        for epoch in range(epochs):
            # Forward pass
            output = self.forward()

            # Backward pass
            self.backward(output)

            # Print loss and weights
            loss = np.mean((self.y - output) ** 2)
            print(f'Epoch {epoch}, Loss: {loss:.4f}')
            print(f"Weights: w13: {self.w13}, w14: {self.w14}, w23: {self.w23}, w24: {
                  self.w24}, w35: {self.w35}, w45: {self.w45}, \n{output}")


# Example usage
if __name__ == "__main__":
    X = [0.35, 0.7]
    y = 0.5

    # Define initial weights
    initial_weights = {
        'w13': 0.2,
        'w14': 0.3,
        'w23': 0.2,
        'w24': 0.3,
        'w35': 0.3,
        'w45': 0.9
    }

    nn = SimpleNeuralNetwork(initial_weights, X, y, 1)
    nn.train(epochs=10)

    # Test the network
    # Print predictions
    print("Predictions:")
    print(nn.forward())
