#message="GLUG{7h47_w45_50m3_m47h}"
m=1748226194988448769357166330286067012419930393119966062717
ms=str(m)
l=[]
for i in ms:
    l.append(i)
f=""
def sum1(t):
    s=0
    for i in t:
        s+=int(i)
    return str(s)

for i in range(1,len(ms)+1):
    f+=sum1(l[:i])
print(int(f))