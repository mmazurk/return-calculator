import numpy as np
from scipy.stats import norm


def generate_value(previous_value):
    if np.random.rand() < 0.05:
        value = norm.ppf(np.random.rand(), loc=0, scale=0.1)
    else:
        scale = .02*(1 + 0.5*abs(previous_value))
        print(scale)
        value = norm.ppf(np.random.rand(), loc=0.0138, scale=scale)

    return float(value)


def generate_returns(n):
    returns = []
    previous_value = 0  # initial value (m8 = 0)
    for _ in range(n):
        current_value = generate_value(previous_value)
        returns.append(current_value)
        previous_value = current_value
    return returns
