import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\d\d\d\d\d')

mo = phoneNumRegex.search('Call me at 040-27990004')

print(mo.group())
