"""csv reader module
Functions:
    get_raw_actions(filename='actions.csv'):
    Transform csv file data into an array of dictionaries.
        Args:
            filename: stringified name of file to read.
"""

import csv


def get_raw_actions(filename="actions.csv"):
    """Transform csv file data into an array of dictionaries.
    Args:
    filename: stringified name of file to read.
    """
    with open(f"{filename}", "r", newline='', encoding="utf-8") as csvfile:
        dict_reader = csv.DictReader(csvfile)
        column_names = dict_reader.fieldnames
        name = column_names[0]
        profits = column_names[2]
        actions = []
        for each in dict_reader:
            benefit = each[f"{profits}"]
            price = each[f"{column_names[1]}"]
            percent = "%"
            dot = "."
            if percent in benefit:
                benefit = benefit.split("%")
                benefit = benefit[0]
            if dot in benefit:
                benefit = float(benefit)
            else:
                benefit = int(benefit)
            if dot in price:
                price = float(price)
            else:
                price = int(price)
            action = {
                "name": each[f"{name}"],
                "price": price,
                f"{profits}": benefit
                }
            actions.append(action)
        return (actions, profits)
