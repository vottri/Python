# Arithmetic Operators

# Task 
# Read two integers from STDIN and print three lines where:
# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.

# Input Format
# The first line contains the first integer, a. The second line contains the second integer, b.

# Constraints
# 1 <= a <= 10**10
# 1 <= b <= 10**10
 
# Output Format
# Print the three lines as explained above.

# ===== Write your code here =====

if __name__ == '__main__':
    a = int(input())
    b = int(input())

# The first line contains the sum of the two numbers.
print(a + b)

# The second line contains the difference of the two numbers (first - second).
print(a - b)

# The third line contains the product of the two numbers.
print(a * b)
