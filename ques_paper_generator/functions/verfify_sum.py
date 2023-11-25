def verify_combinations(combinations, target):
    for combination in combinations:
        if sum(combination) != target:
            print(f"Invalid combination: {combination}")
            return False
    print("All combinations are valid.")
    return True

combinations = []
verify_combinations(combinations, 50)