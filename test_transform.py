from transform import calculate_total_revenue


def test_total_revenue():

    sales = [
        {"price": 100, "qty": 2},
        {"price": 50, "qty": 4}
    ]

    assert calculate_total_revenue(sales) == 400