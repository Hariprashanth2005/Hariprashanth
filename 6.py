test_list=[1,5,3,6,3,5,6,1]
print("the original list is:"+str(test_list))
res=[]
for i in testlist:
    if i not in res:
            res.append(i)
print("the list after removing duplicates:"+str(res))
