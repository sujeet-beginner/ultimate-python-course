# WAP to greet all the person names stored in a list 'i' and which starts with S


l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")