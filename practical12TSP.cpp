def tsp(curr, visited, cost, dp):
  n = len(cost)
  if len(visited) == n:
    return cost[curr][0]

  key = (curr, tuple(visited))
  if key in dp:
    return dp[key]

  ans = float("inf")
  for i in range(n):
    if i not in visited:
      visited.append(i)
      total = cost[curr][i] + tsp(i, visited, cost, dp)
      ans = min(ans, total)
      visited.pop()

  dp[key] = ans
  return ans



def solveTSP(cost):
  dp = {}
  visited = [0]
  return tsp(0, visited, cost, dp)


matrix = [[0, 10, 15, 20], 
          [10, 0, 35, 25], 
          [15, 35, 0, 30], 
          [20, 25, 30, 0]]
print(solveTSP(matrix))