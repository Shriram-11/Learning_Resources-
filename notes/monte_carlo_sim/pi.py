import random

def estimate_pi(num_samples):
    count = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            count += 1

    estimated_area = count / num_samples
    estimated_pi = 4 * estimated_area
    return estimated_pi

# Number of samples for Monte Carlo integration
num_samples = 1000000*2*2

estimated_pi = estimate_pi(num_samples)
print("Estimated value of pi:", estimated_pi)
print("Actual value of pi:",3.1415926536)