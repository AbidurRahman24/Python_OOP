n = int(input())
arr = list(map(int,input().split()))
b = arr
reversed_list = b[::-1]

if arr == reversed_list:
    print("YES")
else: print("NO")

#n = int(input())
#arr = list(map(int, input().split()))