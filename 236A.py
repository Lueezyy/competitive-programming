name = input().strip()

unique = set(name)

if len(unique) % 2 == 1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')