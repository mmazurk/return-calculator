from returns_module import generate_returns


def make_returns():

    number_months = input("Enter number of months: ")
    number_months = int(number_months)

    portfolio_value = input("Enter portfolio value: ")
    portfolio_value = int(portfolio_value)

    monthly_stipend = input("Enter monthly stipend: ")
    stipend = int(monthly_stipend)

    value = portfolio_value
    return_list = generate_returns(number_months)

    for month, item in enumerate(return_list):
        prev_value = value
        value = value + (value * item) - stipend

        print(f"Month", month, round(prev_value, 2), "total *",
              item, "Interest -", stipend, "expenses equals", round(value, 2), "total value")

        if value < 0:
            print("You ran out of money!")
            break

    value = round(value, 2)
    print("---------------------")
    print("Your final value is", value)
