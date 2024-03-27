import datetime
import calendar


# SETTINGS VAR
PERIOD = 50  # years
FIAT = "€"

# Stocks preferences
MONTHLY_STOCKS_PAYMENT = 200  # € or $
YEARLY_STOCKS_PERFORMANCE = 0.07  # %
STARTING_STOCKS_CAPITAL = 0  # € or $

# Deposit preference
MAX_DEPOSIT_VALUE = 50000  # € or $
MONTHLY_DEPOSIT_PAYMENT = 650  # € or $
YEARLY_DEPOSIT_PERFORMANCE = 0.04  # %
STARTING_DEPOSIT_CAPITAL = 0  # € or $
# ----------------------------------


def investment_simulator(
    yearly_performance: float,
    monthly_payment: float,
    starting_capital: float = 0.0,
    max_investment_value: float = float("inf"),
):
    """
    Generator function for simulate monthly interesting in a
    investments

    Yields:
        (float, float): return total capital and monthly interest
    """

    monthly_performance = yearly_performance / 12
    total_capital = starting_capital
    interest = 0

    while True:
        total_capital += monthly_payment
        capital_without_interest = total_capital

        if total_capital < max_investment_value:
            total_capital += capital_without_interest * monthly_performance
            interest = total_capital - capital_without_interest
        else:
            interest = max_investment_value * monthly_performance
            total_capital += interest

        yield total_capital, interest


def capitalFormat(capital: float) -> str:
    """
    Format the cash value with fiat type.

    Args:
        capital (float)

    Returns:
        str: the formatted value
    """
    return FIAT + "{:,.2f}".format(capital)


if __name__ == "__main__":
    stock_generator = investment_simulator(
        YEARLY_STOCKS_PERFORMANCE,
        MONTHLY_STOCKS_PAYMENT,
    )
    deposit_generator = investment_simulator(
        YEARLY_DEPOSIT_PERFORMANCE,
        MONTHLY_DEPOSIT_PAYMENT,
        max_investment_value=MAX_DEPOSIT_VALUE,
    )

    actual_year = datetime.date.today().year

    # Simulation through the years
    for year in range(actual_year, actual_year + PERIOD):
        for month in calendar.month_name[1:]:
            stocks_value, stocks_interest = next(stock_generator)
            deposit_value, deposit_interest = next(deposit_generator)

            total_value = stocks_value + deposit_value
            interest = stocks_interest + deposit_interest

            date = f"{year} {month}"

            total_value = capitalFormat(total_value)
            interest = capitalFormat(interest)

            print(f"{date}\t\tInterest = {interest} \tCapital = {total_value}")
