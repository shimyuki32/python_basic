import string
import re
printable = string.printable
# print(printable)

# print(re.findall('\d', printable))
# print(re.findall('\w', printable))
# print(re.findall('\s', printable))

# x = 'abc' + '-/*' + '\u00ea' + '\u0115'
# print(x)
# print(re.findall('\w', x))

source = """I wish I may, I wish I might
Have a dish of fish tonight."""

print(re.findall(r'wish', source))
print(re.findall(r'wish|fish', source))
print(re.findall(r'^wish', source))
print(re.findall(r'fish tonight\.$', source))
print(re.findall(r'[wf]ish', source))
print(re.findall('\bfish', source))

