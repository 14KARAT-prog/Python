src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

from collections import Counter
counter = Counter(src)

result = [x for x, n in counter.items() if n==1]
print(result)