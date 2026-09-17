# Dict : It is (Collection) used to store a key - value pair ; cannot duplicate keys

num = {} # Empty dictionary

marks = {
    "Sujeet" : 100,
    "Prashant" : 64,
    "Prem" : 69
}

print(marks, type(marks))

# print(marks[0]) it will give error as it cannot print the o index . but if we write the key it will tell us the value as the output 
# for ex : marks = [["Harry", 100]] the problem is that within list we cant access 100 and complex logic might computational expensive
print(marks["Sujeet"])
print(marks["Prashant"])




# we could  have use list also as list also allows list within list but the need of dict. came so bcoz we would have not able to access the key-value within the list 




# Dict - Properties
# It is unordered
# It is mutable
# It is indexed
# Cannot contain dupplicate keys