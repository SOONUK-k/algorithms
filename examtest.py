#T = int(input())
H, W, N = map(int, input().split())
n=1
while n*H<N:
    n+=1
num = n
print(n)
move = num*H - N
print(move)
WW = n
HH = H - move

sH=str(H)
sW=str(W)

Hd = len(list(sH))
Hw = len(list(sW))

print(Hd)
print(Hw)

print(WW)
print(HH)

snW = str(WW)
snH = str(HH)
print(snH+snW)

