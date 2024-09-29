def missingRolls(rolls, mean: int, n: int):
        m = len(rolls)
        total_sum = mean * (n + m)
        
        # Step 2: Calculate the sum of the given rolls
        current_sum = sum(rolls)
        
        # Step 3: Determine the sum of the missing rolls
        missing_sum = total_sum - current_sum
        
        # Step 4: Check if a solution is possible
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Step 5: Distribute the missing sum across n rolls
        # Start by giving each roll the minimum value of 1
        result = [1] * n
        missing_sum -= n  # Subtract n because we gave 1 to each
        
        # Now distribute the remaining missing_sum by adding up to 5 to each roll
        for i in range(n):
            add_value = min(5, missing_sum)
            result[i] += add_value
            missing_sum -= add_value
        
        return result

a = missingRolls([1,5,6],3,4)