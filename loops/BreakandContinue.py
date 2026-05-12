# break terminates a loop
a=1
while(a<10):
    if(a%3==0):
        break
    a += 1
    print(a)


print("------------------------")
# continue skip any interation and odd number
i=0
while(i<10):
    i+=1
    if(i%3==0):
        continue
    print(i)

