
import pandas as pd
from collections import Counter


with open("vibe/vibe.txt", encoding='utf-8') as f:
    lines = f.readlines()

c = Counter(lines)


for key, value in c.items():
    print("{0}: {1}".format(key, value))
print(c.most_common(3))

