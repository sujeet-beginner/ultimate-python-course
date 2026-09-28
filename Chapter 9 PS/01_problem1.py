# WAP to read from the given txt file "poems.txt" and find out whether it contains the word "twinkle "


f = open("poems.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle twinkle is present in the content ")
else:
    print("The twinkle word is not present in the content")
f.close()