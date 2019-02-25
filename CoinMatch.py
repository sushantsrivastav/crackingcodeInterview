# Calculate the number of ways to make change

def change_possibilities(amount,denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin,amount+1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
    return ways_of_doing_n_cents[amount]


print(change_possibilities(100,[1,5,10,25]))