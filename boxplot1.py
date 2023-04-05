
thislist = [1,1,2,3,4,5,6,9,8,1]
liste3 = [1,2,9,4,5,6,7]
def mean(liste):
    #liste sortieren
    liste.sort()
#Länge der Liste bestimmen
    if len(liste) % 2 == 1:     # ungerade
        return liste[int(len(liste)/2)]    
    else:                       # gerade
        return  (liste[int(len(liste)/2)]+liste[int(len(liste)/2 - 1)])/2

def quantile1(liste):
        liste.sort()
        return  (liste[int(len(liste)/2)]+liste[int(len(liste)/2 - 1)])/2
def quantile2(liste):
    half = int(len(liste))//2
    return liste[:quantile2], liste[quantile2:]


def calc(liste):
    print("test "+ str(quantile1(liste)))
    return[0,quantile1(liste)[0], mean(liste), quantile1(liste)[1], 0]

print(8 % 2)
print(9 % 2)

#test

print("mean "+ str(calc(thislist))) 
print(quantile1(thislist))
print(quantile2(thislist))







