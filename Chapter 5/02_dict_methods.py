marks = {
    "Sujeet" : 100,
    "Prashant" : 64,
    "Prem" : 69,
    0 : "Sid"

}

# .items :  It will give the total no. of items in the dict but in the form of tuples
print(marks.items())

# .key : It will print the key in the dict
print(marks.keys())

# .values : It will print all the values in the dict
print(marks.values())

# .update
marks.update({"Sujeet" : 99, "Gauri" : 96}) # allows to update the marks , these is possible bcoz dict. is mutable : It can even add new key-value  to dict
print(marks)

# .get : Returns the value of the spcified keys (and value is returned)
print(marks.get("trushnali")) # It print 'None' bcoz the trushnali doesnt exist in the describe dict
print(marks.get("Sujeet"))  # It will print the 'Sujeet' : value(100) \

print(marks.get("Sujeet2")) # Prints None
print(marks["Sujeet2"]) # prints an error