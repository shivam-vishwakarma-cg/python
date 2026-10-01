

sen=input("enter a sentence")
if sen in "1234567890":
    print("digit detected")
if sen in ".":
    print("suspicious link detected")
if sen in "@":
    print("review")
    