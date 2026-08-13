t1 = (2,4,3,1)
t2 = (3,2,5,7)

merged = t1 + t2
result = ()

for x in merged:
    if x not in result:
        result += (x,)  
        
print("Merged tuple without duplicates:", result)