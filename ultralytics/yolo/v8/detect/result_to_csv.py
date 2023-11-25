import pandas as pd

def result_to_csv(file_name, car, quantity_car, average_speed_car, van, quantity_van, average_speed_van, bus, quantity_bus, average_speed_bus):
    init_keys = ["file_name", "car", "quantity_car", "average_speed_car", "van", "quantity_van", "average_speed_van", "bus", "quantity_bus", "average_speed_bus"]

    try:
        df = pd.read_csv('vehicles_data.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=init_keys)

    new_row = {key: [value] for key, value in zip(init_keys, [file_name, car, quantity_car, average_speed_car, van, quantity_van, average_speed_van, bus, quantity_bus, average_speed_bus])}
    df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)
    df.to_csv('result.csv', index=False)


