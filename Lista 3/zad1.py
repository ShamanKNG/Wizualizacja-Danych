A=[1/x for x in range(1,11)]
print(A)
B=[2**i for i in range(11) ]
print(B)
C=[i for i in B if i % 4==0]
print(C)