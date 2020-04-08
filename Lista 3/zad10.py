def zakupy(**nazwa):
    suma=0
    for x in nazwa:
        suma+=nazwa[x]
    print(suma)


zakupy(chleb=1,napoj=8,pomidor=4)
