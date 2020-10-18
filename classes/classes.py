"""
Objektovo orientované programovanie(OOP) je spôsob programovanie, v ktorom zoskupujeme dáta(premenné) a funkcie(metódy) do logických celkov nazývaných objekty;
Medzi objektovo orientované jazyku patria napr.: C++, C#, Java, Python, ... . Prvým objektovo orientovaným jazykom bola Simula;
Samotnú triedu môžme považovať za predlohu objektu. Samotný objekt, ktorý má data a funkcie sa nazýva inštancia, po anglicky instance;
Objekty majú 2 základné metódy: constructor(ktorý vytvára inštanciu) a deconstructor(ktorý "ničí/maže" inštanciu);
Constructor: viď riadok 26. Deconstructor v Pythone nie je samotný metódov ale je kľučovým slovom: viď riadok 179;
"""

import datetime

class Zamestnanec:


    #Trieda Zamestnanec
    #Každý zamestnanec by mal mať: meno, priezvisko, email a plat


    #zamestnavatel, navysenie_platu a nastupny_plat sú "class variable", preto ju má každa inštancia Triedy Zamestnanec
    zamestnavatel = "SOŠ Handlová" 
    navysenie_platu = 1.01         
    nastupny_plat = 9000

    #Funkcie, ktoré sa viažú k tiede sa volajú metódy/"method"


    #Na vytvorenie inštancie Triedy slúži "dunder/magic" metóda __new__(), ktorú netreba dávať do kódu, pokiaľ sa nejedná o zvláštny prípad


    #Dunder metóda __init__() - Contructor slúži na nastavenie vlastností inštancie a je zavolaná vždy automaticky pri vytváraní inštancie
    #Ako prvý parameter berie inštanciu triedy, vytvorenú metódou __new__(), zvyklosťou je pomenovávať tento parameter "self"
    #Toto môže byť zo začiatku metúce, preto uvediem príklad
    #Vytvárame inštanciu menom Adam, Adam = Zamestnanec("Adam","Horvát")
    #Všade, kde sa vyskitne slovo self, môžeme ho nahradiť "Adam"
    #Takže:
    def __init__(self,meno,priezvisko,plat=nastupny_plat): #self = Adam, meno = "Adam", priezvisko = "Horvát", plat=9000
        self.meno = meno                          #Adam.meno = "Adam"                          
        self.priezvisko = priezvisko              #Adam.priezvisko = "Horvát"
        self.plat = plat                          #Adam.plat = 9000
        #self.email = f"{meno.lower()}.{priezvisko.lower()}@zssha.edu.sk"


    #Dunder metóda __str__() vracia reprezentáciu objektu ako typ "string"
    #Metóda __str__() je zavolaná vždy, pri voláni funkcii: print(), str()
    #Ako jediný parameter berie inštanciu triedy
    #V tomto prípade metóda __str__() vráti krátke zhrnutie vlastnosti objektu
    def __str__(self):
        return f"{self.meno} {self.priezvisko}, email: {self.email}, plat: {self.plat}"


    #Dunder metóda __add__() je zavolaná vždy, keď sa inštancia triedy vyskitne v sčítacej operácii(+) na ľavej strane
    #Ako parametre berie 2 inštancie triedy(ščítance), prvá je inštancia na ľavo od + a druhá napravo, inštancia napravo sa podľa zvyklosti nazýva other
    #V tomto prípade sa metóda __add__() snaží vrátiť súčet platov pokiaľ je aj druhý ščítanec inštanciou Triedy Zamestnanec
    #Na overenie si, či je druhý ščítanec inštanciou Triedy Zamestnanec použijeme funkciu isinstance()
    #Funkcia isinstance() berie ako parametre inštanciu a Triedu, ktorej má byť prvý parameter inštanciou, vracia "bool" podľa toho, či je prvý parameter skutočne inštanciou
    def __add__(self,other):
        if isinstance(other,Zamestnanec):
            return self.plat + other.plat
        return NotImplemented


    #Metóda navysenie je "normálnou metódou"
    #Jej funkciou je navýšiť plat podľa vstupu
    def navysenie(self,navysenie=navysenie_platu):
        self.plat = int(self.plat * navysenie)


    #Decorátor @property zmení metódu na vlastnosť, to znamená, že táto metóda sa zavolá vždy, keď sa volá vlastnosť .email
    #V tomto prípade metóda email vracia email vo forme "meno.priezvisko@zzsha.edu.sk", pričom meno aj priezvisko su malými písmenami
    @property
    def email(self):
        return f"{self.meno.lower()}.{self.priezvisko.lower()}@zssha.edu.sk"


    #Metóda celé meno má tiež dekorátor @property
    #Metóda cele_meno() vracia celé meno vo forme "Meno Priezvisko"
    @property
    def cele_meno(self):
        return f"{self.meno} {self.priezvisko}"


    #Decorátor @property zmení prvý parameter metódy z inštancie triedy na Triedu
    #Keďže "class" je kľúčovým slovom Python-u tak je zvyklosťou tento parameter nazývať cls
    #V tomto prípade metóda slovnik() slúži ako alternatýva k funkcii __init__(), s tým, že: 
    #miesto tradičného vytvorenia inštancie meno_inštancie = Trieda(parameter1,parameter2,...,parametern), sa zavolá táto metóda viď riadok 181
    @classmethod
    def slovnik(cls,dict):
        try:
            return cls(dict["meno"],dict["priezvisko"],dict["plat"])
        except KeyError:
            return cls(dict["meno"],dict["priezvisko"],cls.nastupny_plat)


    #Decorátor @staticmethod odstráni prvý povinný parameter metódy(inštacia triedy)
    #Tieto metódy neinteraktujú priamo z dátamy objektu ale majú nejaké logické spojenie s objektom
    #V tomto prípade metóda pracovny_den() vráti "bool" podľa toho, či zadaný deň bol,je alebo bude pracovný
    #Modul datetime a jeho vlastnosť .weekday() vracia "int" pričom Pondelok = 0, Utorok = 1, ..., Nedeľa = 6
    @staticmethod
    def pracovny_den(den):
        if den.weekday() == 5 or den.weekday() == 6:
            return False
        return True


    #.setter dekorátory využivame, pokiaľ chceme využiť metódu s dekorátorom @property v priradení(=)
    #V tomto prípade @property metóda cele_meno() využíva vlastnosti meno a priezvisko, .setter spôsobý to, že ich budeme môcť jak zavolať tak ja priradiť vo forme "string" "Meno Priezvisko"
    #Všeobecný synatx pre setter je @{meno_metódy}.setter
    @cele_meno.setter
    def cele_meno(self, vstup):
        self.meno, self.priezvisko = vstup.split(" ")


"""
Dedenie alebo inheritance je presne to, ako sa to volá. Vieme vytvoriť podtriedy/"subclasses", ktoré "zdedia" vlastnosti po rodičovskej triede;
Dedia sa aj vlastnosti aj metódy. Pokiaľ je nejaká vlastnosť alebo metóda zadefinovaná znova, má vyšiu prioritu ako tá zdedená; 
"""

class Ucitel(Zamestnanec):


    #Trieda Ucitel okrem zákldaných vlastnosti z triedy zamestnanec implemetuje aj vlastnosť "triedny" a "povolanie"


    #Vlastnosti navysenie_platu a nastupny_plat su zadefinované z novými hodnotami, ktoré budú mať aj inštancie Triedy Ucitel. Vlasnosť povolanie je nová, takže nemá hodnotu na dedenie
    #Tieto hodnoty sú preferované voči hodnotám, ktoré boli zdedené
    navysenie_platu = 1.03
    nastupny_plat = 11000
    povolanie = "Učiteľ"


    #Aby sme nemuseli opakovať riadky z funkcie __init__() Triedy Zamestnanec môžeme použiť funkciu super(), ktorá reprezentuje rodičovskú funkciu
    #Pokiaľ pracujeme s mnohonásobným dedením, je najlepšie namiesto funkcie super() využiť priamo názov rodičovskej funkcie, v tomto prípade Zamestnanec.__init__()
    def __init__(self,meno,priezvisko,plat=nastupny_plat,triedny=False):
        super().__init__(meno,priezvisko,plat)
        self.triedny = triedny


class Majster(Zamestnanec):


    #Trieda Majster okrem základných vlastnosti z Triedy Zamestnanec implementuje aj vlastnosť "ucebna" a "povolanie"


    navysenie_platu = 1.02
    nastupny_plat = 10000
    povolanie = "Majster"

    def __init__(self,meno,priezvisko,plat=nastupny_plat,ucebna="Budova F"):
        super().__init__(meno,priezvisko,plat)
        self.ucebna = ucebna


#Zákldané inštancovanie inštancie triedy
maťko = Zamestnanec("Martin", "Dolník")
maroš = Majster("Maros","Matejov")
johny = Ucitel("Jan","Krausko")

#Pre prístup k vlastnosti používame . operátor
print("Plat of johny:", johny.plat)
#Pre prístup k metóde používame . operátor s tým, že pridávame zátvorku s parametrami
johny.navysenie(1.10)
print("Plat of johny:", johny.plat)

print("Celé meno of maťko:",maťko.cele_meno)
maťko.cele_meno = "Maťko Dolník"
print(maťko.email)

print("Email of johny:", johny.email)

print("Povolanie of johny:", johny.povolanie)

print("Učebňa of maroš:", maroš.ucebna)

print("Plat of maroš and johny together:", maroš + johny)

johny.cele_meno = "Jano Krausko"

print(johny)

del johny

johny_slovnik = {"meno":"Jan","priezvisko":"Krausko"}

johny = Ucitel.slovnik(johny_slovnik)

print(johny)
