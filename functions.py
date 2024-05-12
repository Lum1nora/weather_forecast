def get_data(days):
    dates = ["1", "2", "3"]
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature
