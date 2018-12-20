class Fila:
  def --init--(self):
    self.valores=[]
  
  def lenght(self):
    return len (self,valores)

  def isempty(self):
    return len (self.valores)==0

  def enqueue(self,elemento):
     self.valores.append(elemento)

  def dequeue(self):
    if (not(self.isempty())):
      self.valores.pop(0)
