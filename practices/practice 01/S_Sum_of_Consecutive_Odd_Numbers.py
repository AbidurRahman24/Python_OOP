t = int(input()) 
while t > 0:
    x, y = map(int, input().split()) #multiple input
    # print(x, y)
    if x > y:
        x, y = y, x
    sum = 0
    for i in range(x+1,y+1-1):
        if(i%2==1):
            sum += i
    print(sum)       

    t -= 1  

