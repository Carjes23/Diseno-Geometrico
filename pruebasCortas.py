def aproxParametros(q):
    t=[]
    t.append(0)
    d=0
    for dato in range(1, len(q)):
        d+=(abs(int(q[dato])-int(q[dato-1]))) 
    for i in range(1,len(q)-1):
        t.append(t[i-1]+ (abs(int(q[i])-int(q[i-1]))/d))
    t.append(1)
    return t

j=[1,2,3]
a=aproxParametros(j)
print(a)