
import pandas as pd
from collections import Counter
import re

par = re.findall(r'\w+', open('vibe/bakroti.txt').read().lower())
print(Counter(par).most_common(10))


# with open("vibe/bakroti.txt", encoding='utf-8') as f:
#     lines = f.readlines()

# for i in range(len(lines)):
#     lines[i]=lines[i].rstrip()
# c = Counter(lines)


# # for key, value in c.items():
# #     print("{0}: {1}".format(key, value))
# print(c.most_common(10))

