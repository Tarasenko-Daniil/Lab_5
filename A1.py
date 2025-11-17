s = ' Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему недождь) () (()).'
while True:
    first = s.find('(')
    if first == -1:
        break
    last = s.find(')', first)
    if last == -1:
        break
    s = s.replace(s[first:last+1], "")
print(s)