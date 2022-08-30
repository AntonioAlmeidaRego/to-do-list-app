def serialize_by_sales(sales: []):
    cars = []
    for sale in sales:
        cars.append(sale.car)

    return cars
