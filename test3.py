
N=0
li = input()


box=0

if int(li)<10:
        ls = [int(li),0]
        checkli=[0,int(li)]
        N+=1

        while(checkli[0] !=ls[0] and checkli[1]!=ls[1]):    
            box=ls[0]+ls[1]
            ls=[ls[1], box]
            N+=1

else:    
    ls = list(map(int, li))
    checkli = ls
    
    if ls[0]+ls[1]>=10:
        box=ls[0]+ls[1]
        box-=10

        ls=[ls[1], box]
        
        N+=1
        while(ls[0]!=checkli[0] and ls[1] != checkli[1]):
            if ls[0]+ls[1] >=10:
                box = ls[0]+ls[1]
                box -= 10
                ls=[ls[1], box]
                N+=1
            else:
                box=ls[0]+ls[1]
                ls=[ls[1], box]
                N+=1

    else:
        box=ls[0]+ls[1]
        ls=[ls[1], box]
        N+=1
        while(ls[0]!=checkli[0] and ls[1] != checkli[1]):
            if ls[0]+ls[1] >=10:
                box = ls[0]+ls[1]
                box -= 10
                ls=[ls[1], box]
                N+=1
            else:
                box=ls[0]+ls[1]
                ls=[ls[1], box]
                N+=1

print(N)

