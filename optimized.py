"""
This is the optimized algorithm module for calculating best profits from a dataset of actions.
"""

import time
from action import initialise_actions
from csv_reader import get_raw_actions
from data_manager import DataManager
from input import get_user_input


def optimized(actions, budget=500, scale=100):
    """Optimized algorithm for best profit calculation.
    Args:
    actions: array of action objects with price and profit_value attributes.
    budget=500: int or float.
    scale=100: int, multiple of 10, used to fine-tune precision.
    """
    nonnegatives = [a for a in actions if a.price >= 0]
    negatives = [a for a in actions if a.price < 0]
    base_profit = sum(a.profit_value for a in negatives) * scale
    extra_budget = sum(-a.price for a in negatives) * scale
    price_profit_pair = ((int(a.price * scale), int(a.profit_value * scale)) for a in nonnegatives)
    budget = int(extra_budget + (budget * scale))

    dp = [0] * (budget + 1)

    for price, profit in price_profit_pair:
        for j in range(budget, price - 1, -1):
            dp[j] = max(dp[j], dp[j - price] + profit)
    best = max(dp)
    return (best + base_profit) / scale


def transform_to_dict(best):
    """Transform best results to a dictionary.
    Args: best profit value
    """
    best_dict = {"profit": best}
    return best_dict


def main():
    """Main function"""
    data_manager = DataManager()
    filenames = ["actions.csv", "actions1.csv", "actions2.csv"]
    storage_names = ["best_value.json", "data_set1.json", "data_set2.json"]
    file, storage = get_user_input(filenames, storage_names)
    raw_actions, fieldname = get_raw_actions(file)
    actions = initialise_actions(raw_actions, fieldname)
    start_time = time.time()
    best2 = optimized(actions)
    best_dict2 = transform_to_dict(best2)
    data_manager.save(best_dict2, storage)
    print(f"{time.time() - start_time} seconds")

main()
