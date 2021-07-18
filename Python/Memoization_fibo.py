
def fibo(n):
    global l
    if n<2:
        l[n]=n
    elif l[n]==-1:
        l[n]=(fibo(n-2)+fibo(n-1))
    return l[n]

n=int(input("Enter the fibonacci term to get the result: "))
l=[-1]*(n+1)
print(fibo(n))