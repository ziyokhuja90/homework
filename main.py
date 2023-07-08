class Book():
    def __init__(self):
        self.kitoblar = {}
        
    def addBook(self,name,**kwargs):
        self.kitoblar[name] = kwargs 
        
        
    def getBook(self,name):
        return self.kitoblar[name]
    
    def searchBook(self , name):
        for name1 in self.kitoblar:
            if name1 == name:
                return self.kitoblar[name]
        
        # if self.kitoblar[name] in self.kitoblar:
        #     return self.kitoblar


h = Book()
h.addBook('kitob1',muallif='kimdur',narxi=1100,yili=2500)
h.addBook('kitob2',muallif='kim',narxi=120,yili=1700)
h.addBook('kitob3',muallif='mual',narxi=2000,yili=1000)


print(h.searchBook('kitob1'))
print(h.searchBook('kitob2'))
print(h.searchBook('kitob3'))

