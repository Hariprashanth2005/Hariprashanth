class solution:
    def groupanagrams(self,strs):
        result={}
        for i in strs:
            x="".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x]=[i]
        return list(result.values())
ob1=solution()
print(ob1.groupanagrams(["eat","tea","tan","nat","ate","nat","bat"]))
