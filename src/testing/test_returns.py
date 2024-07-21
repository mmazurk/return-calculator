import pandas as pd
from numpy import average
from src.methods.generate_returns import generate_value


def test_returns(n):
    returns = []
    previous_value = 0
    for _ in range(n):
        current_value = generate_value(previous_value)
        returns.append(current_value)
        previous_value = current_value

    # returns = [x * 100 for x in returns]
    df = pd.DataFrame(returns, columns=["Returns"], index=None)
    return df


df = test_returns(120)
df.to_clipboard()
