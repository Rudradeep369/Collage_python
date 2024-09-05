import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x + 4

def df(x):
    return 2*x - 4

def gradient_descent(initial_x, learning_rate, num_iterations):
    x = initial_x
    x_history = [x]
  
    for i in range(num_iterations):
        gradient = df(x)
        x = x - learning_rate * gradient
        x_history.append(x)
      
    return x, x_history

initial_x = 0
learning_rate = 0.1
num_iterations = 50

x, x_history = gradient_descent(initial_x, learning_rate, num_iterations)

print("Local minimum: {:.2f}".format(x))

x_vals = np.linspace(-1, 5, 100)

plt.plot(x_vals, f(x_vals), label='f(x) = x^2 - 4x + 4')

plt.plot(x_history, f(np.array(x_history)), 'rx', label='Iterations')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent')
plt.legend()

plt.show()
