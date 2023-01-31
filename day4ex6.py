def delchar(a,b):
 if(a!=1):
     return a.replace(b,"")
a=input("enter the string:")
b=input("enter the character to be deleted:")
print(delchar(a,b))
