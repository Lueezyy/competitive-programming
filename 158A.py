n, k = map(int, input().split())

scores = list(map(int, input().split()))

advance = 0
for score in scores:
    if score >= scores[k-1]:
        advance += 1

print(advance)