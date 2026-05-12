with open("log.txt","a") as f:
    f.write("program run successfully" + "\n")
    f.write("yeh its working" + "\n")

with open("log.txt","r") as f:
    print(f.read())

