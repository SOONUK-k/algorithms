T = int(input())
for a in range(0,T):
    k = int(input())
    n = int(input())

    num=0
    kum=0
    for i in range(1,n):
        num+=i
    for j in range(1,k+1):
        kum+=i
    result = ((k)*num)+n+kum
    print(result)

    
