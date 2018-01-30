import re

NAME = r'(?P<NAME>\w+)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
m = scanner.match()
a,b =m.lastgroup, m.group()
m = scanner.match()
a,b =m.lastgroup, m.group()
m = scanner.match()
a,b =m.lastgroup, m.group()
m = scanner.match()
a,b =m.lastgroup, m.group()
m = scanner.match()
a,b =m.lastgroup, m.group()
