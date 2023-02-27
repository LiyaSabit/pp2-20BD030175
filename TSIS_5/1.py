"""
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Menin nomirim (771) 842-9700')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
"""
"""
#1st
import re
word = input()
pattern = '^a(b*)$'
result = re.match(pattern, word)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
"""
"""
#2nd
import re
word = input()
pattern = '^a(b){2,3}$'
result = re.match(pattern, word)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
"""
"""
#3rd
import re
word = input()
pattern = '^[a-z]+_[a-z]+$'
result = re.match(pattern, word)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
"""
"""
#4th
import re
word = input()
pattern = '^[A-z]+[a-z]+$'
result = re.match(pattern, word)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
"""
"""
#5th
import re
word = input()
pattern = '^a+..b$'
result = re.match(pattern, word)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
"""
"""
#6th
import re
word = input()
pattern = '[\s,.]'
replace = ':'
res = re.sub(pattern, replace, word)
print(res)
"""
"""
#7th
import re
word = input()
pattern = r'snake'
replace = r'camel'
res = re.sub(pattern, replace, word)
print(res)
"""
"""
#8th
import re
word = input()
pattern = '[A-Z][^A-Z]*'
res = re.findall(pattern, word)
print(res)
"""
"""
#8th
import re
word = input()
phoneNumRegex = re.compile(r'[A-Z][^A-Z]*')
mo = phoneNumRegex.findall(word)
print(mo)
"""
"""
#9th
import re
word = input()
pattern = '[A-Z][a-z]*'
res = re.findall(pattern, word)
print(' '.join((res)))
"""
#10th
import re
word = input()
pattern = r'camel'
replace = r'snake'
res = re.sub(pattern, replace, word)
print(res)
