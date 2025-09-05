"""
This is the optimized algorithm module for calculating best profits from a dataset of actions.
"""

import time
from csv_reader import get_raw_actions
from data_manager import DataManager
from input_output import get_user_input
from actions import convert_actions


def optimized(actions, budget=500):
    """Optimized algorithm for best profit calculation.
    Args:
    actions: array of action dictionaries with price and profit keys.
    budget=500: int or float.
    Returns: int of best possible profits with the given budget.
    """
    nonnegatives = [a for a in actions if a["price"] > 0]
    profits = [a["profit"] for a in nonnegatives]
    prices = [round(a["price"]) for a in nonnegatives]
    n = len(nonnegatives)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0
                if prices[i - 1] <= j:
                    pick = profits[i - 1] + dp[i - 1][j - prices[i - 1]]
                not_pick = dp[i - 1][j]

                dp[i][j] = max(pick, not_pick)

    return dp[n][budget]


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
    storage_names = data_manager.get_storage()
    file, storage = get_user_input(filenames, storage_names)
    raw_actions, fieldname = get_raw_actions(file)
    actions = convert_actions(raw_actions, fieldname)
    start_time = time.time()
    best2 = optimized(actions)
    best_dict2 = transform_to_dict(best2)
    data_manager.save(best_dict2, storage)
    print(f"{time.time() - start_time} seconds")

main()
