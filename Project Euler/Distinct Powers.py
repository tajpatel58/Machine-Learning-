
a=[4]
for k in range(2,101):
    for i in range(2,101):
        b = k**i
        if b in a:
            continue
        else:
            a.append(b)

print(len(a))



