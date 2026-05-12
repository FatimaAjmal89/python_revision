#question1
with open("names.txt", "w") as f :
    count = 0
    while count<5:
         name = input("write name ")
         f.write(name + "\n")
         count+=1

with open("names.txt","r") as f:
    print(f.readlines())

