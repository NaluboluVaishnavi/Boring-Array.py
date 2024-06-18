#4
#1 2 3 4
n = int(input())
a = list(map(int,input().split()))
a.sort()
left = 0
right = len(a)-1
s = 0
while left<=right:
    d=abs(a[right]-a[left])
    s += d
    left +=1
    right -=1
print(s)    
