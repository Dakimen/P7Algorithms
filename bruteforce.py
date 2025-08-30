""""Bruteforce module."""

import time
import itertools
from csv_reader import get_raw_actions
from data_manager import DataManager
from actions import convert_actions

def bruteforce(actions):
    """Bruteforce algorithm.
    Args:
    actions: array of action class instances."""
    all_combinations = []
    for r in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, r):
            all_combinations.append(combination)
    best_returns = all_combinations[0]
    best_returns_value = 0
    for combination in all_combinations:
        total_price = sum(each["price"] for each in combination)
        if total_price <= 500:
            combination_value = sum(each["profit"] for each in combination)
            if combination_value > best_returns_value:
                best_returns = combination
                best_returns_value = combination_value
    return best_returns


def transform_to_dict(best):
    """Transform bruteforce results into a dictionary.
    Args:
    best: combination of actions generate by bruteforce().
    """
    best_dict = {}
    best_dict["Cost"] = sum(each["price"] for each in best)
    best_dict["Returns"] = sum(each["profit"] for each in best)
    best_dict["Solution"] = "Bruteforce"
    return best_dict


def main():
    """Main function"""
    start_time = time.time()
    data_manager = DataManager()
    raw_actions, fieldname = get_raw_actions()
    actions = convert_actions(raw_actions, fieldname)
    best = bruteforce(actions)
    best_dict = transform_to_dict(best)
    data_manager.save(best_dict)
    print(f"{time.time() - start_time} seconds")


main()
