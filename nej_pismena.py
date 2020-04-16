"""
nej_pismena.py
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

    def max_soucet_3(self, mnozina):
        """
        argument: množina - posloupnost, která je předmětem výpočtu
        druhá optimalizace - jeden průchod intervalem najde výsledek
        metoda potřebuje nejmenší počet kroků potřebných k výpočtu výstupu
        """
        pocet_prvku = len(mnozina)
        soucet_useku = 0
      

        # pro všechny prvky množiny
        for i in range(0, pocet_prvku + 1):
            if i < pocet_prvku:         # ohraničení i na vlastní interval
                if soucet_useku < len(mnozina[i]):       # tam, kde součet úseku a dalšího prvku je větší než 0, má smysl počítat dál
                    soucet_useku = len(mnozina[i])        # do součtu se připočítá další prvek
                    if self.maximum < soucet_useku:                 # hledání maxima
                        self.maximum = soucet_useku
                        self.maximum_prvek_j = i                    # konečný index nejbohatšího úseku
                        self.maximum_prvek_i = i
                        
                else:                       # tam, kde součet úseku a dalšího prvku je menší nebo rovna 0, nemá smysl další prvek připočítávat k součtu a čítač se nuluje
                    #soucet_useku = 0
                    #nula = True
                    pass
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



r = open("seznam_slov.txt", encoding="Utf-8")
retezec = r.read()
r_list = retezec.split()
r.close()
posloupnost = Posloupnost()
posloupnost.max_soucet_3(r_list)
posloupnost.sestav_vysledek(r_list)
print(r_list)
