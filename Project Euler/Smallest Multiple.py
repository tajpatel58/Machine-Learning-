def smallestMultiple():
    SMALLEST = 100000000000000000
    for i in range(1,1000000000):
        t=1
        while i%t==0 and t<=20:
            t=t+1
        if t==21 and i<=SMALLEST:
            SMALLEST =i
        else:
            continue

    return SMALLEST

print(smallestMultiple())

