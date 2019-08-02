numbers=int(input())
rev=0
s=0
while(n>0):
    s=n%10
    rev=(rev*10)+s
    numbers=numbers//10
print(rev)
