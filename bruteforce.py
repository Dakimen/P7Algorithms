from action import initialise_actions
from csv_reader import get_raw_actions
import itertools
from data_manager import DataManager

def bruteforce(actions):
    all_combinations = []
    for r in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, r):
            if sum(each.price for each in combination) <= 500:
                all_combinations.append(combination)
    best_returns = all_combinations[0]
    for combination in all_combinations:
        best_returns_value = sum(each.profit_value for each in best_returns)
        combination_value = sum(each.profit_value for each in combination)
        if combination_value > best_returns_value:
            best_returns = combination
    return best_returns


def sort_actions(actions):
    sorted_actions = sorted(actions, key=lambda action: action.profit_percent)
    for action in sorted_actions:
        print(f"{action.name}: {action.profit_percent}")


def transform_to_dict(best):
    best_dict = {}
    actions = {}
    n = 1
    for action in best:
        actions[f"Action{n}"] = action.to_dict()
        n = n + 1
    best_dict["Actions"] = actions
    best_dict["Cost"] = sum(each.price for each in best)
    best_dict["Returns"] = sum(each.profit_value for each in best)
    return best_dict


def main():
    data_manager = DataManager()
    raw_actions = get_raw_actions()
    actions = initialise_actions(raw_actions)
    best = bruteforce(actions)
    best_dict = transform_to_dict(best)
    data_manager.save(best_dict)
    sort_actions(actions)


main()