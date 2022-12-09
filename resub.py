import sys
import re

for line in sys.stdin:
    line = line.rstrip('\n')

    res = re.sub(r'human', 'computer', line)
    if res:
        print(res)
