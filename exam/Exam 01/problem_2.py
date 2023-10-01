n = int(input())
lst = list(map(int, input().split()))
cnt = {}
for i in lst:
    if i in cnt:
        cnt[i] +=1
    else:
        cnt[i] =1

remove = 0

for num, count in cnt.items():
    
    if count > num:
        remove += count - num
    elif count < num:
        remove += count
print(remove)
