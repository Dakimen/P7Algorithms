from action import initialise_actions
from csv_reader import get_raw_actions
from data_manager import DataManager
import time
from input import get_user_input


def optimized_discarded1(actions, budget=500):
    dp = {0: 0}

    for action in actions:
        profit = action.profit_value * 100
        next_dp = dp.copy()
        for cost, total_profit in dp.items():
            action_cost = action.price * 100
            new_cost = cost + action_cost
            if new_cost <= budget * 100:
                new_profit = total_profit + profit
                if new_cost not in next_dp or new_profit > next_dp[new_cost]:
                    next_dp[new_cost] = new_profit
        dp = next_dp

    best_cost, best_profit = max(dp.items(), key=lambda x: x[1])
    best_cost = best_cost / 100
    best_profit = best_profit / 100
    best = (best_cost, best_profit, "optimized solution 1")
    return best


def transform_to_dict(best):
    best_dict = {}
    best_dict["Cost"] = best[0]
    best_dict["Returns"] = best[1]
    best_dict["Solution"] = best[2]
    return best_dict


def main():
    data_manager = DataManager()
    filenames = ["actions.csv", "actions1.csv", "actions2.csv"]
    storage_names = ["best_value.json", "data_set1.json", "data_set2.json"]
    file, storage = get_user_input(filenames, storage_names)
    raw_actions, fieldname = get_raw_actions(file)
    actions = initialise_actions(raw_actions, fieldname)
    start_time = time.time()
    best2 = optimized_discarded1(actions)
    best_dict2 = transform_to_dict(best2)
    data_manager.save(best_dict2, storage)
    print("--- %s seconds ---" % (time.time() - start_time))


main()
