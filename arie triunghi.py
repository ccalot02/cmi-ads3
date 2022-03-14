def trgsrf(a,b,c):
    s=((a+b+c)/2)
    return (s*(s-a)*(s-b)*(s-c))**0.5
a=complex(input("insert parameter a : "))
b=complex(input("insert parameter b : "))
c=complex(input("insert parameter c : "))
print(trgsrf(a,b,c))