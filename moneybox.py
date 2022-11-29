class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bank = 0
    def can_add(self,v):
        if self.bank + v > self.capacity:
            return False
        else:
            return True
    def add(self,v):
        if self.can_add(v) == True:
            self.bank += v

put = MoneyBox(10)
put.add(8)
put.add(2)

print(put.bank)
print('ver1;')