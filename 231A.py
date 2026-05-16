n = int(input())
solved = 0

for _ in range(n):
    if sum(map(int, input().split())) >= 2:
        solved += 1
    print(solved)