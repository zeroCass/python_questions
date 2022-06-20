import re
regex = re.compile(r'(\w+)-(\d+)')
x = regex.search('CBCSCA01-8257806 - CUPS 1.10')
print(x.group(1))