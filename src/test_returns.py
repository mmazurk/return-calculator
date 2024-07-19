from numpy import average
from returns_module import generate_value


def test_returns(n):
    returns = []
    previous_value = 0
    for _ in range(n):
        current_value = generate_value(previous_value)
        returns.append(current_value)
        previous_value = current_value

    ten_year = float(average(returns[0:120]))*100
    twenty_year = float(average(returns[0:240]))*100
    return ten_year, twenty_year


test_returns(300)
