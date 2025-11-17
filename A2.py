import re
s = "He jests at scars. That never felt a wound!  Hello, friend!  Are you OK?"
offers = 0
s = ' '.join(s.split())
for i in s:
    if i == "." or i == "!" or i == "?" :
        offers +=1
sentences = re.split(r'(?<=[.!?])\s*', s)

for i in sentences:
    if i:
        print(i)
print(offers)