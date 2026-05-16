n = int(input())
x = 0

for _ in range(n):
    bit = input()
    if '++' in bit:
        x += 1
    elif '--' in bit:
        x -= 1
print(x)