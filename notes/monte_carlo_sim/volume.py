import random
import math

def monte_carlo_volume_estimate(xmin, xmax, ymin, ymax, zmin, zmax, num_samples):
    count = 0

    for _ in range(num_samples):
        x = random.uniform(xmin, xmax)
        y = random.uniform(ymin, ymax)
        z = random.uniform(zmin, zmax)

        if x**2 + y**2 + z**2 <= 1:
            count += 1

    total_volume = (xmax - xmin) * (ymax - ymin) * (zmax - zmin)
    estimated_volume = total_volume * (count / num_samples)
    return estimated_volume

def actual_volume(radius):
    return (4/3) * math.pi * radius**3

# Define the bounds of the unit sphere
xmin, xmax = -1, 1
ymin, ymax = -1, 1
zmin, zmax = -1, 1

# Number of samples for Monte Carlo integration
num_samples = 1000000

estimated_volume = monte_carlo_volume_estimate(xmin, xmax, ymin, ymax, zmin, zmax, num_samples)
actual_vol = actual_volume(1)  # Actual volume of a unit sphere

print("Estimated volume:", estimated_volume)
print("Actual volume:", actual_vol)
print("Accuracy",100-(estimated_volume/actual_vol))