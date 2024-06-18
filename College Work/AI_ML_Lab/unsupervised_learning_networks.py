import numpy as np

# Define the AND gate inputs and expected outputs
inputs = np.array([
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1]
])

# Expected outputs for AND gate
expected_output = np.array([1, -1, -1, -1])

# Initialize weights and bias (random small values or zeros)
weights = np.array([0.0, 0.0])
bias = 0.0
print(f"Initial weights: {weights}, Initial bias: {bias}")

# Define learning rate
learning_rate = 1

# Hebbian learning rule with bias: Δw = η * x * y and Δb = η * y


def hebbian_learning(inputs, expected_output, weights, bias, learning_rate, epochs=4):
    for epoch in range(epochs):
        print(f"\nEpoch {epoch+1}")
        for i, x in enumerate(inputs):
            y = expected_output[i]

            # Compute weight change and bias change
            delta_w = learning_rate * x * y
            delta_b = learning_rate * y

            # Update weights and bias
            weights += delta_w
            bias += delta_b

        # Print weights and bias after each epoch
        print(f"  Weights after epoch {epoch+1}: {weights}")
        print(f"  Bias after epoch {epoch+1}: {bias}")

        # Print truth table after each epoch
        print_truth_table(inputs, weights, bias)

    return weights, bias

# Function to print the truth table


def print_truth_table(inputs, weights, bias):
    print("Truth Table")
    print("Input | Predicted Output")
    for input_vector in inputs:
        output = predict(input_vector, weights, bias)
        print(f" {input_vector}  |         {output}")

# Testing the trained weights and bias


def predict(inputs, weights, bias):
    # Compute weighted sum with bias
    weighted_sum = np.dot(inputs, weights) + bias
    # Apply step function with threshold for AND gate
    # Adjusted to match the binary output scheme
    return np.where(weighted_sum >= 0.0, 1, -1)


# Train the network using Hebbian learning
final_weights, final_bias = hebbian_learning(
    inputs, expected_output, weights, bias, learning_rate)

print(f"\nFinal weights after training: {
      final_weights}, Final bias: {final_bias}")
