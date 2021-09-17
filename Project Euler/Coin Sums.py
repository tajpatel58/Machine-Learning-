

z = [1,2,5,10,20,50,100,200]
w =0
for a in range(0,201):
    for b in range(0,101):
        for c in range(0,41):
            for d in range(0,21):
                for e in range(0,11):
                    for f in range(0,5):
                        for g in range(0,3):
                            t = (a*1)+(b*2)+(c*5)+(d*10)+(e*20)+(f*50)+(g*100)
                            if t==200:
                                w+=1
                            else:
                                continue
                            print(a)

print(w)