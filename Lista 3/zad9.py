def geomet(a1=1,q=1,ile=10):
    if (q!=1):
        suma=a1*(1-q**(ile))/(1-q)
    else:
        suma=a1*ile
    return suma

print(geomet(2,3,2))
