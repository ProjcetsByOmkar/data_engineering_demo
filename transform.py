def calculate_total_revenue(sales):

    total = 0

    for row in sales:
        total += row["price"] * row["qty"]

    return total


if __name__ == "__main__":

    sales = [
        {"price": 100, "qty": 2},
        {"price": 50, "qty": 4}
    ]

    print(calculate_total_revenue(sales))