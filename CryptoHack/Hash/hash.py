i =1 
while(1):
    tmp = 1
    for x in range(i):
        tmp*=((2048-x-1)/2048.0)
    print(tmp)
    if(tmp<0.5):
        break
    i+=1
print(i)

