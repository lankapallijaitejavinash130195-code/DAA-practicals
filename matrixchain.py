# practical - 6 : implementation of Matrix Chain Multiplication using dynamic programming
def matrix_chain(p, n):
    # dp[i][j] = min multiplications to compute matrices i..j
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


n = int(input("Enter number of matrices: "))

p = []
print("Enter dimensions:")
for i in range(n + 1):
    p.append(int(input()))

ans = matrix_chain(p, n)
print("Minimum number of multiplications:", ans)

# input-> dimensions - 3, enter dimensions - 10,20,30,40