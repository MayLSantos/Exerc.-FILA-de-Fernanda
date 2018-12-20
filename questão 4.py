class No:
    def _init_(self, elemento):
        self.elemento= elemento
        self.primeiro= None

def pecorrer(cabeça):
    valor= cabeça
    while(valor is not None):
        print(valor.elemento)
        valor=valor.proximo

def link(site, elementoBusca):  
    valor = site  
    while (valor is not None and valor.elemento != elementoBusca): 
        valor = valor.proximo 
    return valor is not None

def adicionar(site, elemento): 
    valor = site 
    anterior = None 
    while (valor is not None): 
        anterior = valor
        valor = valor.proximo 

    novoNo = No(elemento) 
    anterior.proximo = novoNo 

def remover(site, elementoRemovido): 
    antecessor = None 
    valor = site 
    while (valor is not None and valor.elemento!=elementoRemovido):
        antecessor = valor
        valor = valor.proximo 
    if (valor is not None):
        if (valor is site):
            site = valor.proximo 
        else: 
            antecessor.proximo = valor.proximo 
    return site 

def main():
    site= No("www.whatsapp.com.com.br")
    no2= No("www.google.com.br")
    site.proximo= no2
    no3= No("www.youtube.com.br")
    no2.proximo= no3
    print( link( site, "google"))
    print( link( site, "youtube"))
    print( link( site, "whatsapp"))
if(_nome=="main_"): 
    main()
