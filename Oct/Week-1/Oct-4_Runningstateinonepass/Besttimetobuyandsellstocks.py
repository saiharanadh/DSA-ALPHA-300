def MaxProfit(prices):
    min = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        else:
            profit = prices[i] - min

            if profit > max_profit:
                max_profit = profit

    return max_profit

print(MaxProfit([7, 1, 5, 3, 6, 4]))