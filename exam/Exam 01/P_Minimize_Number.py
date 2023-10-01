n = int(input())
lst = list(map(int, input().split()))
num = 0
def even_num(lst):
    for i in lst:
        if i % 2 != 0:
            return False
    return True

while even_num(lst):
    for i in range(n):
        lst[i] //= 2
    num += 1

print(num)
