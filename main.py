import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def mean_absolute_error(actual, predicted):
    return np.mean(np.abs(actual - predicted))


def gradient_descent(data, target, learning_rate, num_iterations):
    features = np.column_stack((np.ones_like(data), data))  # Add a column of ones for the intercept
    weights = np.zeros(features.shape[1])  # Initialize weights with zeros

    # Plot the initial state
    plt.scatter(data, target, label='Actual')
    initial_predictions = weights[1] * data + weights[0]
    line, = plt.plot(data, initial_predictions, color='red', label='Predicted')
    plt.title('Actual vs. Predicted values with Best Fit Line')
    plt.xlabel('Data')
    plt.ylabel('Target')
    plt.legend()
    plt.pause(0.1)

    for _ in range(num_iterations):
        predictions = np.dot(features, weights)
        errors = predictions - target

        # Update weights using gradients
        gradient = (2 / len(target)) * np.dot(errors, features)
        weights -= learning_rate * gradient

        # Update the line in the plot
        line.set_ydata(weights[1] * data + weights[0])
        plt.pause(0.01)

    plt.show()

    return weights


# Generate synthetic data
np.random.seed(0)
data = np.random.rand(100) * 10
target = 2 * data + 1 + np.random.randn(100) * 2  # y = 2x + 1 + noise

# Hyperparameters
learning_rate = 0.01
num_iterations = 100

# Apply gradient descent to find the best fit line
weights = gradient_descent(data, target, learning_rate, num_iterations)

# Make final predictions using the learned weights
final_predictions = weights[1] * data + weights[0]
# Calculate MAE
mae_value = mean_absolute_error(target, final_predictions)

print(f'Mean Absolute Error (MAE) = {mae_value:.2f}')

