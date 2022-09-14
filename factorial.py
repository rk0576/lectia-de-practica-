n=int(input('n='))
m=int(input('m='))
def factorial(x):
    f=1
    for i in range(1,x+1):
        if (n>m):
            f=f*i
        return f
print('c=',factorial(n)/factorial(m)*factorial(n*m))