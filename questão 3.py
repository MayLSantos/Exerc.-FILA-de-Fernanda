class Fila:
    def _init_(self):
        self. paciente=[]

    def lenght (self):
        return len(self.paciente)

    def isEmpyt(self):
        return len(self.paciente) == 0

    def clínica(self, nome):
        while len((self.paciente)<=20):
            self.paciente.append(nome)

    def atendimento (self):
        if (not(self.isEmpyt())):
            self.paciente.pop(0)

fila= Fila()
fila.clínica ("Maria")
fila.clínica ("Luiz")
fila.clínica ("Anunciada")
fila.clínica ("Nalanda")
