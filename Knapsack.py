import time
from itertools import combinations

items = [
    {'weight': 1, 'value': 10},
    {'weight': 3, 'value': 40},
    {'weight': 4, 'value': 50},
    {'weight': 5, 'value': 70}
]

capacity = 7

def knapsack_dynamic (items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range (n+1)]

    for i in range (n + 1):
        for w in range (capacity + 1):
            if i == 0 or w == 0:
                dp [i][w] = 0
            elif items [i - 1]['weight'] <= w:
                dp [i][w] = max (items [i-1]['value'] + dp[i-1][w-items[i-1]['weight']], dp[i-1][w])
            else:
                dp [i][w] = dp [i-1][w]
    
    w = capacity
    chosen_items = []

    for i in range (n, 0, -1):
        if dp [i][w] != dp [i-1][w]:
            chosen_items.append (items[i-1])
            w -= items [i-1]['weight']

    total_value = dp[n][capacity]

    print("Maximum value achievable:", total_value)
    print("Items selected to reach this value:")

    for idx, item in enumerate(chosen_items, start=1):
        print(f"- Selected item {idx} has a weight of {item['weight']} and a value of {item['value']}")



knapsack_dynamic(items, capacity)
