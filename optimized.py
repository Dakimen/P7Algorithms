from action import initialise_actions
from csv_reader import get_raw_actions
from data_manager import DataManager
import time
from input import get_user_input


def optimized(actions, budget=500):
    dp = [(0, 0.0, [])]
    for action in actions:
        new_entries = []
        for cost, profit, path in dp:
            new_cost = cost + action.price
            if new_cost <= budget:
                new_profit = profit + action.profit_value
                new_entries.append((new_cost, new_profit, path + [action.name]))
        combined = dp + new_entries
        combined.sort(key=lambda x: (x[0], -x[1]))
        new_dp = []
        max_profit_so_far = -1.0
        for cost, profit, path in combined:
            if profit > max_profit_so_far:
                new_dp.append((cost, profit, path))
                max_profit_so_far = profit
        dp = new_dp
    best_cost, best_profit, best_path = max(dp, key=lambda x: x[1])
    best = (best_cost, best_profit, best_path, "optimized solution 2")
    return best


def transform_to_dict(best):
    best_dict = {}
    best_dict["Actions"] = best[2]
    best_dict["Cost"] = best[0]
    best_dict["Returns"] = best[1]
    best_dict["Solution"] = best[3]
    return best_dict


def main():
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
    print("--- %s seconds ---" % (time.time() - start_time))


main()
