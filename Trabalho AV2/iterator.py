class Iterator:
    __slots__ = ['lista','ponteiro']

    def __init__(self, lista):
        self.lista = lista
        self.ponteiro = 0

    def next(self):
        if(self.ponteiro>=0):
            dado = self.lista[self.ponteiro]            
            self.ponteiro = (self.ponteiro + 1)
            return dado
        else:
            self.ponteiro = 0
            return first()

    def after(self):
        if(self.ponteiro==0):
            return first()
        if(self.ponteiro>0):       
            self.ponteiro = (self.ponteiro - 1)
            dado = self.lista[self.ponteiro]     
            return dado


    def first(self):
        return self.lista[0]

    def last(self):
        return self.lista[len(self.lista)-1]