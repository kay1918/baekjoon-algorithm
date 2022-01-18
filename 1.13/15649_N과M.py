import sys 
import itertools

N, M = map(int, sys.stdin.readline().split())

arr = list(map(str, range(1, N+1)))
numbers = list(itertools.permutations(arr, M))


for num in numbers:
    print(' '.join(num))