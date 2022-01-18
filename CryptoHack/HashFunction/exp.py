def birthday2():
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
def birthday1():
    i= 1
    while(1):
        res = pow(2047/2048.0,i)
        print(res)
        if res < 0.5:
            print(i)
            break
        i+=1
birthday1()