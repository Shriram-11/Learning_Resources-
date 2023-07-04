import random

def estimate_pi(num_points):
    points_inside_circle = 0
    points_inside_square = 0

    for _ in range(num_points):
        # Generate random x and y coordinates within the square [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

        points_inside_square += 1

    # Estimate pi using the ratio of points inside the circle to the total points inside the square
    pi_estimate = 4 * (points_inside_circle / points_inside_square)
    return pi_estimate

# Perform the Monte Carlo simulation to estimate pi
num_simulations = 10000000

estimated_pi = estimate_pi(num_simulations)

print("Estimated value of π:", estimated_pi)
