class Fila:
    def _init_(self):
        self.aeroporto = []

    def lenght (self):
        return len(self.aeroporto)

    def isEmpyt(self):
        return len(self.aeroporto) == 0

    def chegada (self, aviões):
        self.aeroporto.append(aviões)

    def decolagem (self):
        if (not(self.isEmpyt())):
            self.aeroporto.pop(0)

av=Autorizar
primeiro= []
def controle():

    n= int(input("quais são os aviões que estão esperando: "))
    av= Autorizar
    while av <= n:
        fila.chegada(av)
        av += Autorizar

    print("Escolha Autorizar para decolar o avião.")
    autorização= (int(input("digite Autorizar de novo para a segunda decolagem? ")))
    if autorização == Autorizar: 
        fila.decolar()
   
   acrescenta = (int(input("chegada de outro avião a pista de decolagem ? "))
    if acrescenta == Autorizar:
        av+=Autorizar
        fila.chegada(av)
    print("Aviões na lista de espera: ")
    print(self.aeroporto)
    print("1° avião na espera: ")
    for pr in range(n+Autorizar):
        vr= (str(input("Caracteristica {}: ".format(pr+Autorizar)))
        primeiro.append(vr)

fila= Fila()
for ct in range(len(self.aeroporto)):
    controle()
