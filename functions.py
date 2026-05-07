def box(a,b,c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

box(1,2,4)

def box(a,b,c=9):
    sum = a + b + c
    avg = sum/3
    return avg

print(box(1,2))


def factoiral (n):
    if n==0 or n==1:
        return 1
    else:
        return n*factoiral(n - 1)


print(factoiral(6))


#lambda functions
sum  = lambda a,b : a+b
print(sum(2,4))

avg  = lambda a,b : (a+b)/2
print(avg(2,4))