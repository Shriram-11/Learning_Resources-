import pandas as pd
import matplotlib.pyplot as plt



# Calculate and display key statistics
def stats(data):
    mean_score = data['Score'].mean()
    median_score = data['Score'].median()
    std_deviation = data['Score'].std()
    min_score = data['Score'].min()
    max_score = data['Score'].max()
    print("Key Statistics:")
    print(f"Mean Score: {mean_score:.2f}")
    print(f"Median Score: {median_score}")
    print(f"Standard Deviation: {std_deviation:.2f}")
    print(f"Minimum Score: {min_score}")
    print(f"Maximum Score: {max_score}")
    print(f"Number of Students: {len(data)}")


# Create a histogram of scores
def visualize(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['Score'], bins=6, edgecolor='black', alpha=0.7)
    plt.title('Exam Score Distribution')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    toppers=data[data['Score']>=90]
    plt.figure(figsize=(10,6))
    plt.bar(toppers['Student'],toppers['Score'],color='black',alpha=0.7)
    plt.title('Top performing students')
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def main():
    # Read the CSV file
    csv_file = 'exam_scores.csv'  # Replace with your file path
    data = pd.read_csv(csv_file)
    stats(data)
    visualize(data)

if __name__ == '__main__':
    main()
