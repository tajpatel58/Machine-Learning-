import datetime

print(datetime.datetime.today())
print(datetime.datetime(2019,2,11,17,30,30,173504).weekday())
t=0
for k in range(1,101):
    for i in range(1,13):
        if(datetime.datetime(1900+k,i,1, 17, 30, 30, 173504).weekday()==6):
            t=t+1
        else:
            continue

    print(t)