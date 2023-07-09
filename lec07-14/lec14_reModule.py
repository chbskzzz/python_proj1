'''
FUNCTIONS:
re.compile(pattern, flags)
re.search(pattern, string, flags)
re.match(pattern, string, flags)
re.split(pattern, string, max, flag)
re.findall(pattern, string, flag)
re.finditer(pattern, string, flags)
re.sub(pattern, repl, string, count)
re.subn(pattern, repl, string, count)
re.escape(pattern)p
'''

import re

pattern = "bbb ccc ddd"
x = re.compile(pattern)
y = x.match("bbb ccc ddd")
if y:
    print("Match found")
else:
    print("Match not found")


pattern1 = "bbb ccc ddd"
x1 = re.match(pattern1, "bbb ccc ddd")
if x1:
    print("Match found")
else:
    print("Match not found")