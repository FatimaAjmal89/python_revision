h = [1,2,3,4,5,6]

print(h[1:3])

# list built in methods

h.append(22)
h.insert(1,33)
h.sort() #increasing
h.sort(reverse=True)# decreasing
h.reverse()

#loops in list

hh= [1,2,3,4,5,6,7]
i=3
count = 0
for val in hh:
    if(val == 3):
        print(count)
        break
    count+=1


