list=[1,2,3,4,3,4,2,1]
print("the original list is"+str(list))
res=[]
for i in list:
    if i not in res:
     res.append(i)
print("the list after removing duplicates"+str(res))
