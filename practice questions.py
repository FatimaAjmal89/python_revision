info = [
    ("huzaifa","computer"),
    ("huzaifa","computer"),
    ("fatimah","arts"),
    ( "marium" , "sci"),
    ( "fatimah","phy"),
    ( "marium","arts"),
]
print("Question1")
set1 = set()
for tup in info:
    set1.add(tup[1])
print(set1)

print("question2")
set1 = set()
for name,courses in info:
    if(courses=="computer"):
        set1.add(name)

print(set1)

print("question3 ")
dictionary = {}

for name,courses in info:
    if(dictionary.get(name)==None ):
        dictionary.update({name : set()})
        dictionary[name].add(courses)
    else:
        dictionary[name].add(courses)
print(dictionary)