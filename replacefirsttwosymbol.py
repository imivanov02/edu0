import sys
import re

for line in sys.stdin:
    line = line.rstrip('\n')

    res = re.sub(r'(\w)(\w)(\w)?', r'\2\1\3', line)
    if res:
        print(res)
