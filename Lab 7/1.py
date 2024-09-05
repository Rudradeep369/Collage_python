import numpy as np
import matplotlib.pyplot as plt

def gaussian_distribution(x, mean, variance):
    return (1 / (np.sqrt(2 * np.pi * variance))) * np.exp(-((x - mean) ** 2) / (2 * variance))

x_values = np.linspace(-10, 10, 100)
means = [0, 0, 1]
variances = [1, 2, 1]

plt.figure(figsize=(10, 6))
for mean, variance in zip(means, variances):
    plt.plot(x_values, gaussian_distribution(x_values, mean, variance), label=f'Mean={mean}, Variance={variance}')

plt.title('Effect of Mean and Variance on Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
