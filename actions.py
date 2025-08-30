"""Module containing function for converting action dictionaries into treatable format"""

def convert_actions(raw_actions, fieldname):
    """Create action dictionaries from raw dictionaries.
    
    Args:
    raw_actions (array): list of dictionaries containing:
        'name' (string)
        'price' (int)
        'benefit' (int)
    Returns: actions (array of dictionaries with price and profit keys)
    """
    actions = []
    if fieldname == "Benefit":
        for raw_action in raw_actions:
            profit = (raw_action["price"] * raw_action["Benefit"]) / 100
            new_action = {
                "price": raw_action["price"],
                "profit": profit
                }
            actions.append(new_action)
        return actions
    if fieldname == "profit":
        for raw_action in raw_actions:
            new_action = {
                "price": raw_action["price"],
                "profit": raw_action["profit"]
                }
            actions.append(new_action)
        return actions
    raise ValueError("No case for this fieldname: {fieldname}")
