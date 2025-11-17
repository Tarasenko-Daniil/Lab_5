s = input()
words = s.split()
for i in words:
    if i[0].isupper() and len(i) >= 3:
        print(i[0], end = "")
