# Hackerrank 30 days of code
# Day 1: Data Types

# Task
# Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. 

# You must:
# 1. Declare 3 variables: one of type int, one of type double, and one of type String.
# 2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
# 3. Use the "+" operator to perform the following operations:
#    1. Print the sum of i plus your int variable on a new line.
#    2. Print the sum of d plus your double variable to a scale of one decimal place on a new line.
#    3. Concatenate s with the string you read as input and print the result on a new line.

# Input Format
# The first line contains an integer that you must sum with i.
# The second line contains a double that you must sum with d.
# The third line contains a string that you must concatenate with s.

# Output Format
# Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line, 
# and then the two concatenated strings on the third line.

# ===== Write your code here =====

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
# Read and save an integer, double, and String to your variables.

j = int(input())
e = float(input())
t = input()

# Print the sum of both integer variables on a new line.

print(i + j)

# Print the sum of the double variables on a new line.

print(d + e)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.

print(s + t)

