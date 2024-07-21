import numpy as np
import pandas as pd
from scipy.stats import skewnorm, norm


def simulate_returns(n_months, mu=0.0095, sigma=0.044194, skew=0.37754):

    returns = np.zeros(n_months)

    for i in range(1, n_months):
        returns[i] = skewnorm.rvs(skew, loc=mu, scale=sigma)

    # Convert to percentage
    returns = returns * 100
    return pd.DataFrame({'Month': range(1, n_months+1), 'Return (%)': returns}, index=None)


def simulate_returns_excel(n_months):

    returns = np.zeros(n_months)

    for i in range(1, n_months):
        if np.random.rand() < 0.05:
            returns[i] = norm.ppf(np.random.rand(), loc=0, scale=0.1)
        else:
            scale = .025*(1 + 0.5*abs(returns[i-1]))
            returns[i] = norm.ppf(np.random.rand(), loc=0.008, scale=scale)

    return pd.DataFrame({'Month': range(1, n_months+1), 'Return (%)': returns}, index=None)


# Example usage 1
df_returns = simulate_returns(n_months=120)
df_returns.to_clipboard()
df_returns.describe()

# Example returns 2
df_returns = simulate_returns_excel(n_months=120)
df_returns["Return (%)"].to_clipboard()
df_returns.describe()
