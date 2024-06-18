import csv
import numpy as np

# Load the dataset


def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([float(value) for value in row])
    data = np.array(data)
    return data[:, :-1], data[:, -1]

# Calculate prior probabilities


def calculate_priors(y):
    classes, counts = np.unique(y, return_counts=True)
    priors = dict(zip(classes, counts / len(y)))
    return priors

# Calculate conditional probabilities


def calculate_conditional_probabilities(X, y):
    conditional_probs = {}
    for cls in np.unique(y):
        X_cls = X[y == cls]
        feature_probs = []
        for col in range(X.shape[1]):
            values, counts = np.unique(X_cls[:, col], return_counts=True)
            probs = dict(zip(values, counts / len(X_cls)))
            feature_probs.append(probs)
        conditional_probs[cls] = feature_probs
    return conditional_probs

# Classify a new sample


def classify(sample, priors, conditional_probs):
    probabilities = {}
    for cls in priors:
        prior = priors[cls]
        likelihood = 1.0
        for col, value in enumerate(sample):
            feature_probs = conditional_probs[cls][col]
            # Smoothing for unseen feature values
            likelihood *= feature_probs.get(value, 1e-6)
        probabilities[cls] = prior * likelihood
    return max(probabilities, key=probabilities.get), probabilities

# Evaluate the classifier on a dataset


def evaluate(X, y, priors, conditional_probs):
    predictions = [classify(sample, priors, conditional_probs)[0]
                   for sample in X]
    accuracy = np.mean(predictions == y)
    return accuracy

# Predict function for interactive use


def predict(input_features, priors, conditional_probs):
    input_array = np.array(input_features, dtype=float)
    prediction, probabilities = classify(
        input_array, priors, conditional_probs)
    for cls in probabilities:
        print(f'P({cls}) = {probabilities[cls]:.6f}')
    return prediction

# Main function


def main(file_path):
    X, y = load_data(file_path)

    # Discretize data (optional, if features are continuous)
    X_discrete = np.floor(X)  # Simple discretization, adjust as needed

    priors = calculate_priors(y)
    conditional_probs = calculate_conditional_probabilities(X_discrete, y)

    # Evaluate the model on the dataset
    accuracy = evaluate(X_discrete, y, priors, conditional_probs)
    print(f'Accuracy: {accuracy * 100:.2f}%')

    # Prediction loop
    while True:
        try:
            input_str = input(
                "\nEnter new sample (comma-separated values) or 'exit' to quit: ")
            if input_str.lower() == 'exit':
                break
            input_features = [float(x) for x in input_str.split(',')]
            if len(input_features) != X.shape[1]:
                print(f"Please enter exactly {X.shape[1]} feature values.")
                continue
            input_features_discrete = np.floor(input_features)
            prediction = predict(input_features_discrete,
                                 priors, conditional_probs)
            print(f'Predicted class: {prediction}')
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


'''
in the datset we have
Outlook: Rainy = 1, Overcast = 0, Sunny = 2
Temperature: Hot = 1, Mild = 2, Cool = 0
Humidity: High = 1, Normal = 0
Windy: False = 0, True = 1
Play Golf: No = 0, Yes = 1
'''

if __name__ == "__main__":
    main('naive_bayes_dataset.csv')
