import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('exam_scores.csv')

def stats():
    mean=data['Score'].mean()
    median=data['Score'].median()
    std=data['Score'].std()
    tot=len(data['Score'])
    print(f"Mean: {mean}\nMedian: {median}\nStandard Deviation: {std}\n Total Students: {tot}")

def analyze():
    plt.figure(figsize=(10,8))
    plt.hist(data['Score'],bins=6,edgecolor='Black',alpha=0.7)
    plt.title('Exam score distribution')
    plt.xlabel('Frequency')
    plt.ylabel('Students')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10,8))
    toppers=data[data['Score']>90]
    plt.bar(toppers['Student'],toppers['Score'],color='Black',alpha=0.7)
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.show()

def main():
    stats()
    analyze()

if __name__ == '__main__':
    main()