def test_no_negative_price():

    sales = [
        {"price": 100, "qty": 2},
        {"price": -50, "qty": 4}
    ]

    for row in sales:
        assert row["price"] >= 0