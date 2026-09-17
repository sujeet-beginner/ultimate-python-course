# WAP to find out whether the given point is talking about "Harry" or not

post = input("Enter the post : ")

if ("Harry".lower() in post.lower()):
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")