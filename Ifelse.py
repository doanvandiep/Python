import sys

N = int(input().strip())
if N % 2 == 1 or N % 2 == 0 and N >= 6 and N <= 20:
    print("Weird")
elif N % 2 == 0 and N >= 2 and N <= 5 or N % 2 == 0 and N > 20:
    print("Not Weird")