#n is membership operator
#range is like range(5) here 0-4 use for sequence

word ="artificial"
ans=0
for ch in word:
   if(ch== 'i'  or ch=='o' or ch=='a'or ch=='e' or ch=='u' ):
       ans+=1
print(ans)

# sum of natural numbers
sum = 0
for i in range(1,11):
    sum+=i

print(sum)
