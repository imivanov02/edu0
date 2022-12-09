import sys
import re

for line in sys.stdin:
    line = line.rstrip('\n')

    res = re.sub(r'(\w)\1+', r'\1', line)
    if res:
        print(res)

