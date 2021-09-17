import inflect
p = inflect.engine()
SUM=0
for k in range(1,1001):
    t = list(str(p.number_to_words(k)))
    a = ' '
    b = '-'
    while( a in t):
        t.remove(a)
    while( b in t):
        t.remove(b)

    SUM = SUM + len(t)


print(SUM)


