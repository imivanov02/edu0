class Buffer:
    def __init__(self):
        self.buff = []
        self.summ = 0
    def add(self,*a):
        self.buff.extend(a)
        for i in range(len(self.buff)//5):
            for j in range(5):
                self.summ += self.buff.pop(0)
            print(self.summ)
            self.summ = 0

    def get_current_part(self):
        return self.buff

print('ver1')
