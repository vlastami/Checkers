import random


class Bojovnik:
    def __init__(self,jmeno,sila,obratnost, vitalita): #definice magické metody (metoda je funkce, která operuje/manipuluje s nějakým objektem, ovlivňuje jeho vlastnosti,
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

    def __gt__(self, nepritel): #greater than
        return (self.sila+self.obratnost) > (nepritel.sila+nepritel.obratnost)

jarda = Bojovnik("Jarda", 80,20,100)
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

# dekorátory => funkce kolem funkce => uzávěr
def skvelyDekorator(funkce): # ukázka dekorátoru
    funkce()
    print("Jsem skvělý a provedl jsem tu funkci úplně sám")

def pozdrav():
    print("Ahoj podsvětí")

skvelyDekorator(pozdrav)