import re
regex = re.compile(r'(\w+)(-\w+)?-(\w+)')
x = regex.search('CBHRAN-COLETA-8309460')
print(x.groups())
print(len(x.groups()))

if x.group(1) + x.group(2) in 'CBHRAN-COLETA - CUPS 1.6.3':
    print('YEAh')