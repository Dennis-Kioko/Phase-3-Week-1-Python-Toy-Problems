def solution(A):
    N = len(A)
    target_bricks = 10
    total_moves = 0

    # Calculate the total number of bricks
    total_bricks = sum(A)

    # Check if it's possible to distribute bricks evenly
    if total_bricks % N != 0:
        return -1

    # Calculate the target number of bricks in each box
    target_per_box = total_bricks // N

    # Iterate through the boxes
    for i in range(N):
        diff = A[i] - target_per_box
        if diff > 0:
            if i == N - 1:
                return -1  # Cannot move bricks to the right beyond the last box
            A[i + 1] += diff  # Move excess bricks to the right
            total_moves += diff  # Increment total moves

    
    return total_moves


print(solution([7, 15, 10, 8])) 
print(solution([11, 10, 8, 12, 8, 10, 11])) 
print(solution([7, 14, 10]))  
