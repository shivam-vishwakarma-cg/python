n=int(input("enter no of strings"))
for i in range(1,n+1):
    st=input("enter a string")
    if st in "a":
        z=st.count("a")
    print("a",z)