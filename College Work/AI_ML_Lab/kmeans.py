import csv
from math import sqrt
import random
from collections import defaultdict
import matplotlib.pyplot as plt


def euclid(p1, p2):
    a = (p1[0] - p2[0])**2
    b = (p1[1] - p2[1])**2
    return sqrt(a + b)


def initialize_centroids(points, k):
    return random.sample(points, k)


def closest_centroid(point, centroids):
    closest = centroids[0]
    mind = euclid(point, centroids[0])
    for c in centroids[1:]:
        d = euclid(point, c)
        if d < mind:
            mind, closest = d, c
    return closest


def assign_clusters(points, centroids):
    clusters = defaultdict(list)
    for point in points:
        closest = closest_centroid(point, centroids)
        clusters[tuple(closest)].append(point)
    return clusters


def update_centroids(clusters):
    new_centroids = []
    for c, points in clusters.items():
        if points:
            new_centroid = [sum(p[dim] for p in points) / len(points)
                            for dim in range(len(points[0]))]
            new_centroids.append(new_centroid)
        else:
            new_centroids.append(list(c))
    return new_centroids


def has_converged(old, new, tol=1e-4):
    for i in range(len(old)):
        if euclid(old[i], new[i]) > tol:
            return False
    return True


def print_d(centroids, clusters):
    print('Centroids:', centroids)
    for centroid, cluster_points in clusters.items():
        print(f"Cluster around centroid {centroid}: ")
        for p in cluster_points:
            print(p)
        print('-----------------------')


def k_means(filename, k, max_iterations=5, tol=1e-4):
    # Read points from CSV file
    points = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            points.append([float(value) for value in row])

    # Initialize centroids
    centroids = initialize_centroids(points, k)

    for _ in range(max_iterations):
        clusters = assign_clusters(points, centroids)
        new_centroids = update_centroids(clusters)
        print("************************\n")
        print_d(centroids, clusters)

        if has_converged(centroids, new_centroids, tol):
            break

        centroids = new_centroids

    return centroids, clusters


def plot_clusters(centroids, clusters):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    plt.figure(figsize=(8, 6))

    for i, (centroid, points) in enumerate(clusters.items()):
        color = colors[i % len(colors)]
        points = list(zip(*points))  # Transpose to get x and y separately
        plt.scatter(points[0], points[1], c=color, label=f'Cluster {i+1}')
        plt.scatter(*centroid, c=color, marker='x', s=200)  # Centroid marker

    plt.title('K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
centroids, clusters = k_means('dataset.csv', 2)
print("************************\n")
print_d(centroids, clusters)
plot_clusters(centroids, clusters)
