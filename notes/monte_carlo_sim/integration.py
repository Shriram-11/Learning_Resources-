import random
import math

def monte_carlo_integral_estimate(func, xmin, xmax, num_samples):
    integral_sum = 0

    for _ in range(num_samples):
        x = random.uniform(xmin, xmax)
        integral_sum += func(x)

    total_range = xmax - xmin
    average_value = integral_sum / num_samples
    estimated_integral = total_range * average_value
    return estimated_integral

def example_function(x):
    # Replace this function with the equation for the integrand
    return math.sin(x)

# Define the bounds of integration
xmin, xmax = 0, math.pi

# Number of samples for Monte Carlo integration
num_samples = 100000

estimated_integral = monte_carlo_integral_estimate(example_function, xmin, xmax, num_samples)
actual_integral = 2.0  # The actual integral value for the example function

print("\nEstimated integral:", estimated_integral)
print("Actual integral:", actual_integral,'\n')