coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> dict:
    if amount <= 0:
        return "Amount must be > 0"

    res = {}
    for coin in coins:
        if amount >= coin:
            res[coin] = amount // coin
            amount %= coin
    return res


def find_min_coins(amount: int) -> dict:
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    coin_count = [{} for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_count[i] = dict(coin_count[i - coin])
                coin_count[i][coin] = coin_count[i].get(coin, 0) + 1
    return coin_count[amount] if min_coins[amount] != float("inf") else {}

# Example usage
amount = int(input("sum: "))
print("Greedy approach:", find_coins_greedy(amount))
print("DP approach:", find_min_coins(amount))
