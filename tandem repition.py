import sys
import re


for line in sys.stdin:
    line = line.rstrip('\n')

    res = re.findall(r'\b(\w+)\1\b',line)
    if res:
        print(line)