n,l = map(int, input().split())

a = [int(x) for x in input().split()]

a.sort()

r = 0

if a[0] != 0:
    r = a[0]
    
if a[-1] != l:
    r = max(r, l - a[-1])
    
for i in range(n-1):
    r = max(r, (a[i+1] - a[i])/2)
    
    if i+1 == n:
        r = max(r, l - a[i+1])
    
            
print(r)