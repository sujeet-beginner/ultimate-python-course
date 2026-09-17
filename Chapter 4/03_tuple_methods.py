# when you apply tuple method exsiting tuple is not change insted a new tuple is created
a = (2, 4, 5, 10, 12, False, "Sujeet" , "Shiv", 10)
print(a)

# count : returns the time of a  particular no occured within a tuple
no = a.count(10)
print(no)

# index : return the index of the specified no. from the tuples
i = a.index(10)
print(i)

i1 = a.index(Sujeet)
print(i1)