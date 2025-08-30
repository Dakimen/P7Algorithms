

class Action:
    """Action class.
    Used to store action information.
    
    Attributes:
    name (string): action name.
    price (int or float): action price.
    profit_percent (int or float): action profit after two years.
    profit_value (int or float): action's profit in true numbers.
    """
    def __init__(self, action_name, action_price, action_2_year_profit=None, profit_value=None):
        """Initialise action class.
        Args:
        name (string).
        price (int or float).
        profit_percent (int or float) representing expected profit after two years.
        """
        self.name = action_name
        self.price = action_price
        self.profit_percent = action_2_year_profit
        if action_2_year_profit is not None:
            one_percent_of_value = self.price / 100
            self.profit_value = one_percent_of_value * self.profit_percent
        elif profit_value is not None:
            self.profit_value = profit_value


def initialise_actions(raw_actions, fieldname):
    """Initialise action objects from raw dictionaries.
    
    Args:
    raw_actions (array): list of dictionaries containing:
        'name' (string)
        'price' (int)
        'benefit' (int)
    """
    actions = []
    if fieldname == "Benefit":
        for raw_action in raw_actions:
            new_action = Action(raw_action["name"],
                                raw_action["price"],
                                raw_action["Benefit"])
            actions.append(new_action)
        return actions
    if fieldname == "profit":
        for raw_action in raw_actions:
            new_action = Action(raw_action["name"],
                                raw_action["price"],
                                None,
                                raw_action[f"{fieldname}"])
            actions.append(new_action)
        return actions
    raise ValueError(f"No case for this fieldname: {fieldname}")
