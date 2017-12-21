import re

patten = re.compile('he')
match1 = patten.match('hello hell world are you kiding me?')
match = re.match('he','hello hell world are you kiding me?')
print  match.string
print  match.re
print  match1.string