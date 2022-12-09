import sys
import re

for line in sys.stdin:
    line = line.rstrip('\n')

    res = re.sub(r'(\b[a|A]+\b)', 'argh', line,count=1)
    if res:
        print(res)
