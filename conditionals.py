some_condition = True
some_other_condition = False

if some_condition:
    print("This conditional is true therefore this will be printed")
else:
    print("This will not be printed")

if some_other_condition:
    print("This is false and this will never be printed")
else:
    print("Since condition is false this will be printed")



if some_other_condition:
    print("Cant print this")
elif some_condition:
    print("This elif is true so I am printed hehe")
else:
    print("This will not be printed")