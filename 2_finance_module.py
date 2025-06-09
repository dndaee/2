def calculate_parent_support(stipend, expenses, months=10, inflation_rate=0.05):

    total_shortfall = 0
    current_expenses = expenses

    for _ in range(months):
        shortfall = current_expenses - stipend
        total_shortfall += shortfall
        current_expenses *= (1 + inflation_rate)

    return total_shortfall
