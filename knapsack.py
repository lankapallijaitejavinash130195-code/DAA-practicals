# practical - 5 : implementation of the 0/1 knapsack problem using dynamic programming
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[ i- 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

print("Maximum value:", knapsack(weights, values, capacity))

#Enter weights: 10 20 30
#Enter values: 60 100 20
#Enter capacity: 40
#Maximum value: 160