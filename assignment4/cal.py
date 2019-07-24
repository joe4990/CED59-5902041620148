class Cal:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def Mul(self):
    return self.x * self.y
  def Plus(self):
    return self.x + self.y
  def Min (self):
    return self.x - self.y
  def Div(self):
    return self.x / self.y
x = int(input("input1: ") )
y = int(input("input2: ") )
a = Cal(x,y)
print(a.Plus());
print(a.Min());
print(a.Div());
print(a.Mul());


  

