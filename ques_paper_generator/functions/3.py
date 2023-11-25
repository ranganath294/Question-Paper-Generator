# Memoization 

# Gives all possible combinations of marks for a target mark and empty list if marks is empty

def find_combinations_memoization(marks, target):
    dp = [set() for _ in range(target + 1)]
    dp[0].add(())
    for num in marks:
        for t in range(target, num - 1, -1):
            for prev in dp[t - num]:
                dp[t].add(prev + (num,))
    return [list(t) for t in dp[target]]

# Should give all values of marks

# marks = [1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,5,6,7,7,8,8,8,8,9,9,10]
# marks = []
# print(find_combinations_memoization(marks, 50))
