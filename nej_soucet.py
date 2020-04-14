"""
nej_soucet.py
najde největší součet v posloupnosti
"""
class Posloupnost():
    def __init__(self):
        self.maximum = 0
        self.kroku = 0
        self.maximum_prvek_i = 0
        self.maximum_prvek_j = 0
            
    def max_soucet_1(self, mnozina):
        pocet_prvku = len(mnozina)
        for i in range(0, pocet_prvku + 1):
            for j in range(0, pocet_prvku + 1):
                soucet_useku = 0
                if i < j:
                    print("i= ",i,"j = ",j)
                    print(mnozina[i:j])
                    for k in range(i,j):
                        soucet_useku = soucet_useku + mnozina[k]
                        self.kroku = self.kroku + 1
                        print("krok", self.kroku )
                    print("součet useku", soucet_useku)
                    print("-"*20)
                    if soucet_useku > self.maximum:
                        self.maximum = soucet_useku
                        self.maximum_prvek_i = i
                        self.maximum_prvek_j = j - 1
        
    def max_soucet_2(self, mnozina):
        pocet_prvku = len(mnozina)
        for i in range(0, pocet_prvku + 1):
            soucet_useku = 0
            for j in range(0, pocet_prvku + 1):
                if i < j:   # and j <= pocet_prvku:
                    print("i= ",i,"j = ",j)
                    print(mnozina[i:j])
                    soucet_useku = soucet_useku + mnozina[j-1]
                    self.kroku = self.kroku + 1
                    print("krok", self.kroku )
                    print("součet useku", soucet_useku)
                    print("-"*20)
                    if soucet_useku > self.maximum:
                        self.maximum = soucet_useku
                        self.maximum_prvek_i = i
                        self.maximum_prvek_j = j - 1
        
    def max_soucet_3(self, mnozina):
        pocet_prvku = len(mnozina)
        soucet_useku = 0
        nula = False
        for i in range(0, pocet_prvku + 1):
            if i < pocet_prvku:
                if soucet_useku + mnozina[i] > 0: 
                    _pom = soucet_useku
                    soucet_useku = soucet_useku + mnozina[i]
                    if self.maximum < soucet_useku:
                        self.maximum = soucet_useku
                        self.maximum_prvek_j = i
                        if nula:
                            self.maximum_prvek_i = i
                            nula = False
                else:
                    soucet_useku = 0
                    nula = True
            self.kroku = self.kroku + 1       
                
    def sestav_vysledek(self, mnozina):
        print (f"Nejbohatší úsek má hodnotu {self.maximum} a je v úseku [{self.maximum_prvek_i}:{self.maximum_prvek_j}] a je tvořen prvky {mnozina[self.maximum_prvek_i:self.maximum_prvek_j+1]}. Pro výpočet bylo potřeba provést {self.kroku} kroků. ")


mnozina = (1, -2, 4, 5, -1, -5, 2, 7, -13, -1, 15, -22, 42, 16, -3, 13, -22)
#mnozina = (5, 2, -6, -3, -1, 4)
posloupnost_1 = Posloupnost()
posloupnost_1.max_soucet_1(mnozina)
print("X"*20)
posloupnost_2 = Posloupnost()
posloupnost_2.max_soucet_2(mnozina)
print("X"*20)
posloupnost_3 = Posloupnost()
posloupnost_3.max_soucet_3(mnozina)
print("X"*20)
posloupnost_1.sestav_vysledek(mnozina)
posloupnost_2.sestav_vysledek(mnozina)
posloupnost_3.sestav_vysledek(mnozina)
print("X"*20)