
import pandas as pd
from collections import Counter
import re
from pprint import pprint
from tabulate import tabulate

# par = re.findall(r'\w+', open('vibe/bakroti.txt').read().lower())
# print(Counter(par).most_common(10))
with open("vibe/name_bonkroti.txt", encoding='utf-8') as f:
    bank = f.readlines()

with open("vibe/name_norm.txt", encoding='utf-8') as f:
    norm = f.readlines()

norm = Counter(norm).most_common(20)
bank = Counter(bank).most_common(20)

result = []

for i in range(len(norm)):
    a = norm[i]
    for i in range(len(bank)):
        if a[0] in bank[i]:
            id= bank[i]
            all = a[1]+id[1]
            proc = id[1]/(a[1]/100)
            proc_from_all = id[1]/(all/100)
            result.append([a[0].rstrip(),all, a[1], id[1], proc, proc_from_all])


print(tabulate((result),headers=['Name',"All", "Norm", "Bank", "Proc", "Proc_from_all"], tablefmt="orgtbl"))



# for key, value in c.items():
#     print("{0}: {1}".format(key, value))


