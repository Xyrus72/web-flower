arr = [900, 1100, 1235]
dep = [1000, 1200, 1240]

arr.sort()
dep.sort()
a=len(arr)
c=1
for i in range(a-1):
    if arr[i+1]-arr[i]>dep[i]-arr[i]:
        continue
    else:
        c+=1
print(c)

