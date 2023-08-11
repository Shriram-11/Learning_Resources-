import random
import pandas as pd

# Generate random data
random.seed(42)  # For reproducibility
num_entries = 60
student_names = [f"Student_{i}" for i in range(1, num_entries + 1)]
scores = [random.randint(35, 100) for _ in range(num_entries)]

# Create a DataFrame
data = pd.DataFrame({'Student': student_names, 'Score': scores})

# Save the DataFrame to a CSV file
csv_file = 'exam_scores.csv'
data.to_csv(csv_file, index=False)

print(f"Generated data and saved to {csv_file}.")
