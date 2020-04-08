listazakupow = {
    "Chleb" : "sztuki",
    "Cukier" : "waga",
    "Mąka" : "waga",
    "Bułka" : "sztuki",
    "Lizak" : "sztuki"
}
lista=[x for x,y in listazakupow.items() if y=="sztuki"]

print(lista)