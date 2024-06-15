import csv

# Define a function to read data from the CSV file


def read_data_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


# Read data from the CSV file
filename = "data.csv"
data = read_data_from_csv(filename)


def classify_instance(instance, hypothesis):
    # Classify the instance based on the hypothesis
    for i in range(len(instance) - 1):
        if hypothesis[i] != '?' and hypothesis[i] != instance[i]:
            return 'No'  # If any attribute doesn't match, classify as 'No'
    return 'Yes'  # If all attributes match, classify as 'Yes'


def find_s(data):
    # Step 1: Initialize h to the most specific hypothesis in H
    # Initialize hypothesis with most specific constraints
    h = ['0'] * (len(data[0]) - 1)
    print("Initial Hypothesis\t", h)

    # Step 2: For each positive training instance x
    for instance in data:
        if instance[-1] == 'Yes':  # Check if instance is positive
            for i in range(len(instance) - 1):  # For each attribute constraint a, in h
                if h[i] == '0':  # If constraint a is not yet set
                    # Set constraint a to the attribute value from the instance
                    h[i] = instance[i]
                elif h[i] != instance[i]:  # If constraint a is not satisfied by x
                    h[i] = '?'  # Replace a in h by the next more general constraint
        print("Hypothesis after another instance\t", h)

    # Step 3: Output hypothesis h
    return h


# Example usage:
col_heads = ['Sky', 'AirTemp', 'Humidity',
             'Wind', 'Water', 'Forecast', 'Enjoy Sport']

print("Column Headers:")
print(", ".join(col_heads))
print("Sample Data:")
for instance in data:
    print(", ".join(instance))

hypothesis = find_s(data)
print("\nFinal hypothesis:", hypothesis)

while True:
    # Take input from the user to classify a new instance
    new_instance = input(
        "\nEnter a new instance (comma-separated attributes): ").split(',')
    classification = classify_instance(new_instance, hypothesis)
    print("Classification:", classification)
