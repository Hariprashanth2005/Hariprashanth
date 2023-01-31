ch="yes"
while ch=="yes":
    a=int(input("enter total users:"))
    if(a==0)or(a<0):
        print("invalid input")
        continue
    else:
        b=int(input("enter staff users:"))
        c=b/3 
        print("no.of student users:",a-b-c)
    ch=input("Do you want to continue?(yes/no) : ")
    print()
else:
    print("End of program.")
       
       
    

