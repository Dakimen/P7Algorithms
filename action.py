

class Action:
    """Action class.
    Used to store action information.
    
    Attributes:
    name (string): action name.
    price (int or float): action price.
    profit_percent (int or float): action profit after two years.
    profit_value (int or float): action's profit in true numbers.
    """
    def __init__(self, action_name, action_price, action_2_year_profit):
        """Initialise action class.
        Args:
        name (string).
        price (int or float).
        profit_percent (int or float) representing expected profit after two years.
        """
        self.name = action_name
        self.price = action_price
        self.profit_percent = action_2_year_profit
        one_percent_of_value = self.price / 100
        self.profit_value = one_percent_of_value * self.profit_percent

    def to_dict(self):
        """Return dictionary of this action's data."""
        action_dictionary = {
            "name": self.name,
            "price": self.price,
            "profit_percent": self.profit_percent,
            "profit_value": self.profit_value
        }
        return action_dictionary


def initialise_actions(raw_actions):
    """Initialise action objects from raw dictionaries.
    
    Args:
    raw_actions (array): list of dictionaries containing:
        'name' (string)
        'price' (int)
        'benefit' (int)
    """
    actions = []
    for raw_action in raw_actions:
        new_action = Action(raw_action["name"],
                            raw_action["price"],
                            raw_action["benefit"])
        actions.append(new_action)
    return actions