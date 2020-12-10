class Money:

    def __init__(self,first=[],second=[]):
       self.first=first
       self.second=second


    def get(self):
        return  self.first,self.second

    def set(self,first=[],second=[]):
        self.first=first
        self.second=second


        def __init__(self, x):
            self.__x = x

        def get_x(self):
            return self.__x

        def set_x(self, x):
            self.__x = x


    def display_info(self):
        x= len(self.first)
        i = 0
        while x>0 :
            print("номінал",self.first[i],"кількість купюр",self.second[i])
            i+=1
            x-=1
    def get_summ(self):
        x = len(self.first)
        i = 0
        summa = 0

        while x>0:
            summa=summa+self.first[i]*self.second[i]
            i += 1
            x -= 1
        print("сумма купюр",summa)

        byu=125
        if byu > summa:
            print("недостатньо грошей для покупки")
        else:
            counter = summa // byu
            print("можна придбати", counter, "одиниць товару")






bank=Money([5,10,20],[10,10,10])
bank.display_info()
bank.get_summ()
bank.set([0,1],[0,1])
print(bank.get())


