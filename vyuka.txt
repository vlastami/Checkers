import random


class Bojovnik:
    def __init__(self,jmeno,sila,obratnost, vitalita, poloha, zaporak): #definice magické metody (metoda je funkce, která operuje/manipuluje s nějakým objektem, ovlivňuje jeho vlastnosti,
        """
        magická metoda má dvě podtržítka
        existují pouze v těle objektu, mělo by se k nim přistupovat pouze zevnitř (jakoby private)
        __init__ je konstruktor třídy - vytvoří instanci objektu a přiřadí mu konkrétní vlastnosti
        self - skrytý parametr, který umožňuje manipulaci s vlastnostmi objektu
        """
        self.jmeno = jmeno #jméno konkrétního bojovníka, zadané parametrem
        self.sila = sila
        self.obratnost = obratnost
        self.vitalita = vitalita
        self.poloha = poloha
        self._vek = 50 #jakoby private parametr - měl by být dostupný pouze uvnitř třídy, ale Python to neví
        self.__vek = 50 #protected parametr

    @property #dekorátor označující getter kolem privátního parametru
    def vek(self):
        return self._vek

    @vek.setter #dekorátor - setter k privátnímu parametru
    def vek(self, cislo):
        self._vek = cislo

    def bojuj_s(self,nepritel):
        #pokus o zásah protivníka
        sance_na_zasah = random.random()*100 #náhodné desetinné čslo od 0 do 100
        if sance_na_zasah > nepritel.obratnost:
            zraneni = random.random()*self.sila
            nepritel.vitalita -= zraneni

    def posun(self,smer,mapa):
        mapa[self.poloha[0], self.poloha[1]]=0
        stara_poloha = list(self.poloha) # vyhýbat se referenčnímu přiřazení!
        if smer =="nahoru":
            self.poloha[1]+=1
        if smer == "dolu":
            self.poloha[1]-=1
        if smer=="vlevo":
            self.poloha[0]-=1
        if smer=="vpravo":
            self.poloha[0]+=1
        if(mapa[self.poloha[0],self.poloha[1]]==3):
            self.poloha = list(stara_poloha)
        if(mapa[self.poloha[0],self.poloha[1]] != 3 and mapa[self.poloha[0],self.poloha[1]]!= 0):
            pass
        if (self.pritel):
            mapa[self.poloha[0],self.poloha[1]] =1
        else:
            mapa[self.poloha[0],self.poloha[1]]=2

    def __gt__(self, nepritel): #greater than
        return (self.sila+self.obratnost) > (nepritel.sila+nepritel.obratnost)
"""
jarda = Bojovnik("Jarda", 80,20,100, [1,1])
bojovnik1 = Bojovnik("Biggus",80,20,100)
bojovnik2 = Bojovnik("Brian", 20,80,100)

print(f"lepší bojovník je {bojovnik1.jmeno if bojovnik1 > bojovnik2 else bojovnik2.jmeno}") #ukázka ternárního operátoru
while bojovnik1.vitalita > 0 and bojovnik2.vitalita > 0:
    bojovnik2.bojuj_s(bojovnik1)
    bojovnik1.bojuj_s(bojovnik2)


if bojovnik1.vitalita >0:
    print(f"Souboj vyhrál bojovník {bojovnik1.jmeno} a jeho vitalita po souboji je {bojovnik1.vitalita}.")
else:
    print(f"Souboj vyhrál bojovník {bojovnik2.jmeno} a jeho vitalita po souboji je {bojovnik2.vitalita}.")


print(jarda.jmeno) #vlastnosti objektu, získání konkrétního parametru, vlastnosti se volají bez závorek
print(jarda._vek)
print(jarda.vek)
"""
# dekorátory => funkce kolem funkce => uzávěr
def skvelyDekorator(funkce): # ukázka dekorátoru
    funkce()
    print("Jsem skvělý a provedl jsem tu funkci úplně sám")

def pozdrav():
    print("Ahoj podsvětí")

skvelyDekorator(pozdrav)

"""
BOJOVNÍK
jednoduchá textová hra
bojovníci náhodně rozmístěni na šachovnici
v každém tahu možnost posunout našeho bojovníka
pokud bude na políčku jiný bojovník, spustí se automatický souboj
vykreslení aktuálního stavu šachovnice

"""
# vytvořit šachovnici jako matici
import numpy as np
import matplotlib.pyplot as plt

sachovnice = np.zeros((8,8), dtype=int) #nulová matice celých čísel o rozměrech 8x8
sachovnice[0,:]=3 #všem sloupcům v prvním řádku nastavíme 3 jako zed
sachovnice[len(sachovnice)-1,:]=3
sachovnice[:,0]=3
sachovnice[:,len(sachovnice)-1]=3


jarda = Bojovnik("Jarda", 80,80,100, [0,0], True)

pocet_zaporaku =5
zaporaci = []
souradnice = [0,0]
for i in range(pocet_zaporaku):
    souradnice[0]=random.randint(1,6)
    souradnice[1]=random.randint(1,6)
    zaporaci.append(Bojovnik("",random.random()*100,random.random()*100,100,souradnice,False))
    sachovnice[souradnice[0],souradnice[1]]=2

sachovnice[jarda.poloha[0],jarda.poloha[1]]=1 #označení polohy bojovníka

print(sachovnice)
plt.imshow(sachovnice, cmap="gray") #vykreslení matice jako bitmap obrázku
plt.show()

while True:
    print("Co chcete dělat?")
    print("Možnosti jsou:")
    print("nahoru")
    print("dolu")
    print("vlevo")
    print("vpravo")
    print("mapa")
    print("konec")
    pokyn = input()

    if(pokyn =="konec"):
        break
    elif(pokyn =="mapa"):
        plt.imshow(sachovnice)
        plt.show()
    else:
        jarda.posun(pokyn,sachovnice)