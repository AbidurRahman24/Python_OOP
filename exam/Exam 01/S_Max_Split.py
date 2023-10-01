st = input()
cnt = 0
bal = []
curr = ""

for i in st:
    curr += i
    if i == "R":
        cnt += 1
    elif i == "L":
        cnt -= 1
    
    if cnt == 0:
        bal.append(curr)
        curr = ""

print(len(bal))
for i in bal:
    print(i)
