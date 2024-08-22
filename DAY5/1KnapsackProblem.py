# Introduction
# Given two integer arrays to represent weights and profits of ‘N’ items, find a subset of these items that will give us maximum profit such that their cumulative weight is not more than a given number ‘C’, and return the maxium profit. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

# Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

# Items: { Apple, Orange, Banana, Melon }

# Weights: { 2, 3, 1, 4 }

# Profits: { 4, 5, 3, 7 }

# Knapsack capacity: 5

# Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

# Apple + Orange (total weight 5) => 9 profit

# Apple + Banana (total weight 3) => 7 profit

# Orange + Banana (total weight 4) => 8 profit

# Banana + Melon (total weight 5) => 10 profit

# This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.

# Problem Statement
# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    # TODO: Write your code here
    res = [0]
    def dfs(w, p, pointer):
      if w>capacity or pointer>=len(weights):
        if w<=capacity:
          res[0] = max(res[0], p)
        return 
      res[0] = max(res[0], p)
      p+=profits[pointer]
      w+=weights[pointer]
      left = dfs(w, p, pointer+1)
      p-=profits[pointer]
      w-=weights[pointer]
      right = dfs(w, p, pointer+1)


    
    dfs(0,0, pointer=0)
    return res[0]