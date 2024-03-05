def digit_sum(num):
        return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1

    # Iterate through all pairs of numbers in the array
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            sum_i = digit_sum(A[i])
            sum_j = digit_sum(A[j])

            # Check if the sums of digits are equal
            if sum_i == sum_j:
                # Update the maximum sum if the current sum is greater
                max_sum = max(max_sum, A[i] + A[j])

    return max_sum

print(solution([51, 71, 17, 42])) 
print(solution([42, 33, 60]))       
print(solution([51, 32, 43]))       
