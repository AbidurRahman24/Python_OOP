# Read input
n = int(input())
arr = list(map(int, input().split()))

mn = min(arr)
mx = max(arr)
mn_pos = arr.index(mn)
mx_pos = arr.index(mx)

arr[mn_pos], arr[mx_pos] = arr[mx_pos], arr[mn_pos]

print(*arr)
