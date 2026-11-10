def aa(a,b):
    if b == 1:
        return a
    e=aa(a,b-1)
    
    return e*a
    
print(aa(2,4))