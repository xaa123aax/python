import re

socialid = '''

身分證A223456789

阿花H123234789

小張的id h198723476

Happy new Year

12345 A543234567

A12398734567938

'''

a=re.findall(r'[a-zA-Z][1-2]\d{8}\D', socialid)

print(a)