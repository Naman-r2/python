def coin_change(coins, amount):

    coins.sort(reverse=True)

    count = 0

    for coin in coins:

        while amount >= coin:
            amount -= coin
            count += 1

    return count


coins = [1, 2, 5, 10]
amount = 27

print(coin_change(coins, amount))