"""
nej_soucet.py
najde největší součet v posloupnosti
3 různé, postupně více optimalizované algoritmy
"""
class Posloupnost():
    """
    třída obsahuje 3 různé způsoby výpočtu "nejbohatšího" úseku v zadané posloupnosti
    metody
    max_soucet_1(posloupnost) - základní výpočet
    max_soucet_2(posloupnost) - první optimalizace
    max_soucet_3(posloupnost) - druhá optimalizace
    sestav_vysledek(posloupnost) - připraví výstup: součet nejbohatšího úseku, výpis a indexy prvků nejbohatšího úseku a počet potřebných kroků výpočtu
    """
    def __init__(self):
        """
        iniciuje instanci a její základní parametry
        """
        self.maximum = 0
        self.kroku = 0
        self.maximum_prvek_i = 0
        self.maximum_prvek_j = 0
            
    def max_soucet_1(self, mnozina):
        """
        argument: množina - posloupnost, která je předmětem výpočtu
        metoda potřebuje největší počet kroků potřebných k výpočtu výstupu
        """
        pocet_prvku = len(mnozina)

        # pro všechny prvky množiny
        for i in range(0, pocet_prvku + 1):
        
            # bere všechny možné kombinace intervalů
            for j in range(0, pocet_prvku + 1):
                soucet_useku = 0
        
                # pro smysluplné kombinace (neopakující se)
                if i < j:
                    print("i= ",i,"j = ",j)
                    print(mnozina[i:j])
        
                    # počítá součet daného intervalu
                    for k in range(i,j):
                        soucet_useku = soucet_useku + mnozina[k]
                        self.kroku = self.kroku + 1
                        print("krok", self.kroku )
                    print("součet useku", soucet_useku)
                    print("-"*20)

                    # hledání maxima
                    if soucet_useku > self.maximum:
                        self.maximum = soucet_useku
                        self.maximum_prvek_i = i
                        self.maximum_prvek_j = j - 1
        
    def max_soucet_2(self, mnozina):
        """
        argument: množina - posloupnost, která je předmětem výpočtu
        první optimalizace - k součtu úseků připočítává poslední úsek
        metoda potřebuje druhý největší počet kroků potřebných k výpočtu výstupu
        """
        pocet_prvku = len(mnozina)

        # pro všechny prvky množiny
        for i in range(0, pocet_prvku + 1):
            soucet_useku = 0
        
            # bere všechny možné kombinace intervalů
            for j in range(0, pocet_prvku + 1):

                # pro smysluplné neopakujícíse kombinace
                if i < j: 
                    print("i= ",i,"j = ",j)
                    print(mnozina[i:j])
                    
                    # počítá součet intervalu tak, že k dosaženému součtu připočítá další prvek intervalu
                    # tzn. nepočítá vždy znovu součet všech prvků intervalu 
                    soucet_useku = soucet_useku + mnozina[j-1]
                    self.kroku = self.kroku + 1
                    print("krok", self.kroku )
                    print("součet useku", soucet_useku)
                    print("-"*20)

                    # hledání maxima
                    if soucet_useku > self.maximum:
                        self.maximum = soucet_useku
                        self.maximum_prvek_i = i
                        self.maximum_prvek_j = j - 1
        
    def max_soucet_3(self, mnozina):
        """
        argument: množina - posloupnost, která je předmětem výpočtu
        druhá optimalizace - jeden průchod intervalem najde výsledek
        metoda potřebuje nejmenší počet kroků potřebných k výpočtu výstupu
        """
        pocet_prvku = len(mnozina)
        soucet_useku = 0
        nula = False

        # pro všechny prvky množiny
        for i in range(0, pocet_prvku + 1):
            if i < pocet_prvku:         # ohraničení i na vlastní interval
                if soucet_useku + mnozina[i] > 0:       # tam, kde součet úseku a dalšího prvku je větší než 0, má smysl počítat dál
                    soucet_useku = soucet_useku + mnozina[i]        # do součtu se připočítá další prvek
                    if self.maximum < soucet_useku:                 # hledání maxima
                        self.maximum = soucet_useku
                        self.maximum_prvek_j = i                    # konečný index nejbohatšího úseku
                        if nula:                                    # pokud předchozí interval měl soucet_useku = 0, pak počáteční index nejbohatšího úseku je roven i
                            self.maximum_prvek_i = i
                            nula = False
                else:                       # tam, kde součet úseku a dalšího prvku je menší nebo rovna 0, nemá smysl další prvek připočítávat k součtu a čítač se nuluje
                    soucet_useku = 0
                    nula = True
            print("i= ",i)
            print(mnozina[self.maximum_prvek_i:self.maximum_prvek_j+1])
            print("krok", self.kroku )
            print("součet useku", soucet_useku)
            print("-"*20)     
            self.kroku = self.kroku + 1  
                
    def sestav_vysledek(self, mnozina):
        """
        argument: množina - posloupnost, která je předmětem výpočtu
        vypíše výsledek výpočtu
        """
        print (f"Nejbohatší úsek má hodnotu {self.maximum} a je v úseku [{self.maximum_prvek_i}:{self.maximum_prvek_j}] a je tvořen prvky {mnozina[self.maximum_prvek_i:self.maximum_prvek_j+1]}. Pro výpočet bylo potřeba provést {self.kroku} kroků. ")


# main
mnozina = (1, -2, 4, 5, -1, -5, 2, 7, -13, -1, 15, -22, 42, 16, -3, 13, -22)
#mnozina = (5, 2, -6, -3, -1, 4)

# použití první metody
posloupnost_1 = Posloupnost()
posloupnost_1.max_soucet_1(mnozina)
print("X"*20)
# použití druhé metody
posloupnost_2 = Posloupnost()
posloupnost_2.max_soucet_2(mnozina)
print("X"*20)
# použití třetí metody
posloupnost_3 = Posloupnost()
posloupnost_3.max_soucet_3(mnozina)
print("X"*20)
# vyhodnocení výsledků

print(f"Pro posloupnost {mnozina} ")
print()
posloupnost_1.sestav_vysledek(mnozina)
posloupnost_2.sestav_vysledek(mnozina)
posloupnost_3.sestav_vysledek(mnozina)
print("X"*20)