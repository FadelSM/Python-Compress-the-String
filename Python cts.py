from itertools import groupby

s = input().strip()

result = []

for key, group in groupby(s):
    count = len(list(group))
    result.append((count, int(key)))

for item in result:
    print(item, end=' ')
