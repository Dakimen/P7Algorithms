from functools import lru_cache


def optimized_discarded1(actions, budget=500):
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


def optimized_discarded2(actions, budget=500):
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
