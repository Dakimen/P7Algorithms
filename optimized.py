from action import initialise_actions
from csv_reader import get_raw_actions
from data_manager import DataManager
import time
from functools import lru_cache


def optimized(actions, budget=500):
    dp = {0: (0, [])}
    for action in actions:
        profit = int(round(action.profit_value * 100))
        next_dp = dp.copy()
        for cost, (total_profit, path) in dp.items():
            new_cost = cost + action.price
            if new_cost <= budget:
                new_profit = total_profit + profit
                if new_cost not in next_dp or new_profit > next_dp[new_cost][0]:
                    next_dp[new_cost] = (new_profit, path + [action.name])
        dp = next_dp
    best_cost, (best_profit, best_path) = max(dp.items(), key=lambda x: x[0])
    best = (best_cost, best_profit / 100, best_path, "optimized solution 1")
    return best


def optimized_option2(actions, budget=500):
    dp = [(0, 0.0, [])]
    for action in actions:
        new_entries = []
        for cost, profit, path in dp:
            new_cost = cost + action.price
            if new_cost <= budget:
                new_profit = profit + action.profit_value
                new_entries.append((new_cost, new_profit, path + [action.name]))
        combined = dp + new_entries
        combined.sort(key=lambda x: (x[0], x[-1]))
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


def optimized_option3(actions, budget=500):
    names = [a.name for a in actions]
    prices = [a.price for a in actions]
    profit_values = [a.profit_value for a in actions]
    n = len(actions)

    @lru_cache(None)
    def loop(i, remaining_budget):
        if i == n or remaining_budget <= 0:
            return (0, [], 0)
        
        profit, path, price = loop(i+1, remaining_budget)

        if prices[i] <= remaining_budget:
            profit_with, path_with, price_with = loop(i + 1, remaining_budget - prices[i])
            profit_with += profit_values[i]
            price_with += prices[i]
            path_with = [names[i]] + path_with
            if profit_with > profit:
                profit, path, price = profit_with, path_with, price_with
        return (profit, path, price)

    best_profit, best_path, best_price = loop(0, budget)
    best = (best_price, best_profit, best_path, "optimized solution3")
    return best


def transform_to_dict(best):
    best_dict = {}
    best_dict["Actions"] = best[2]
    best_dict["Cost"] = best[0]
    best_dict["Returns"] = best[1]
    best_dict["Solution"] = best[3]
    return best_dict


def main():
    start_time = time.time()
    data_manager = DataManager()
    raw_actions = get_raw_actions()
    actions = initialise_actions(raw_actions)
    best1 = optimized(actions)
    best_dict1 = transform_to_dict(best1)
    data_manager.save(best_dict1)
    best2 = optimized_option2(actions)
    best_dict2 = transform_to_dict(best2)
    data_manager.save(best_dict2)
    best3 = optimized_option3(actions)
    best_dict3 = transform_to_dict(best3)
    data_manager.save(best_dict3)
    print("--- %s seconds ---" % (time.time() - start_time))


main()