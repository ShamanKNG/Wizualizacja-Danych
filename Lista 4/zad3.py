with open("zad3.txt","w+") as zad3:
    for n in range(10):
        zad3.write("zapisywanie\n")
with open("zad3.txt","r") as zad3:
    for n in zad3:
        print(n,end="")
