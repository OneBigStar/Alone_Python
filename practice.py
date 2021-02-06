# 숫자야구
import random
key = list(random.randrange(0,10) for i in range(4))
s=0
b=0
print(key)
while 1:
    put_key= list(map(int,input().split()))
    if key==put_key:
        print("정답입니다!")
        print(key)
        break
    else:
        for i in range(0,4):
            if key[i]==put_key[i]:
                s+=1
        for i in put_key:
            if i in key:
                b+=1
        b=b-s    
    print(s,b)
    s=0
    b=0
