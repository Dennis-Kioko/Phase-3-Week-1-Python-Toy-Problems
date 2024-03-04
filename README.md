# Phase 3 Week 1 Python Toy Problems

## Challenge 1: Minimum Moves to Reach 10 Bricks in Every Box

### Description:
- Given N boxes arranged in a row and the number of bricks in each box, the task is to determine the minimum number of moves needed to end up with exactly 10 bricks in every box. In one move, you can take one brick from a box and move it to a box next to it (on the left or right).

### Function Signature:
function solution(A);
that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

Examples:
For A = [7, 15, 10, 8], the function should return 7.
For A = [11, 10, 8, 12, 8, 10, 11], the function should return 6.
For A = [7, 14, 10], the function should return -1.

## Challenge 2: Maximum Sum of Two Numbers with Equal Digit Sum

### Description:
- Given an array A of integers, the task is to find the maximum sum of two numbers whose digits add up to an equal sum. If no such pair exists, return -1

### Function Signature:
function solution(A);
Examples:
Given A = [51, 71, 17, 42], the function should return 93.
Given A = [42, 33, 60], the function should return 102.
Given A = [51, 32, 43], the function should return -1.

## Challenge 2: Challenge 3: Constructing a String with Equal Occurrences of Letters

### Description:
- Given an integer N, the task is to construct a string of length N containing as many different lowercase letters ('a'-'z') as possible, where each letter occurs an equal number of times.

### Function Signature:
function solution(N);

Examples:
Given N = 3, the function may return "fig", "pea", "nut", etc.
Given N = 5, the function may return "mango", "grape", "melon", etc.
Given N = 30, the function may return "aabbcc...oo" (each letter from 'a' to 'o' occurs twice).

#### Algorithm Assumptions:
- N is an integer within the range [1..200,000].

