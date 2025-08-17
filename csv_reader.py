import csv


def get_raw_actions():
    with open("actions.csv", "r", newline='') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        actions = []
        for each in dict_reader:
            benefit = each["Benefit"]
            benefit = benefit.split("%")
            action = {
                "name": each["Actions #"],
                "price": int(each["Price"]),
                "benefit": int(benefit[0])
                }
            actions.append(action)
        return actions
