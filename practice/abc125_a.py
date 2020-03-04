import sys
input = sys.stdin.readline
A, B, T = map(int, input().split())

print(int((T + 0.5) // A * B))
