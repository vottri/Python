# Loops

# Task 
# The provided code stub reads an integer "n" from STDIN. 
# For all non-negative integers i < n, print i**2. 

# Example
# n = 3
# The list of non-negative integers that are less than n=3 is [0, 1, 2].
# Print the square of each number on a separate line.
# 0
# 1
# 4

# Input Format
# The first and only line contains the integer, n.

# Constraints
# 1 <= N <= 20

# Output Format
# Print n lines, one corresponding to each i.

# ===== Write your code here =====

if __name__ == '__main__':
    n = int(input())

# Using while loop:

i = 0
while i<n:
    print(i ** 2)
    i += 1

# Using for loop:

for i in range(n):
    print(i ** 2)
    
