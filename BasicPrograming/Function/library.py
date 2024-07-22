from collections import defaultdict

items = {"1": 1, "2": 2, "0": 0}
print(sorted(items))
# key=で並べ替えの基準を指定できる
print(sorted(items, key=items.get, reverse=True))


s = "123456789"
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
