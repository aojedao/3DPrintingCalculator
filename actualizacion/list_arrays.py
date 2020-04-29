import numpy as np
from time import time

class list_array:
    def __init__(self,size):
        self.size=size
        self.count=0
        self.lista=np.zeros(self.size,"object")

    def full(self):
        return self.count==self.size
    def empty(self):
        return self.count==0
    def insertar(self,data):
        #if not self.full():  opcional
            self.lista[self.count]=data
            self.count+=1
    def modify(self,position,data):
        self.lista[position]=data

    def insertar_position(self,position,data):
        support=self.count
        while(support>position):
            self.lista[support]=self.lista[support-1]
            support-=1
        self.lista[position]=data
        self.count+=1
    def search_pos(self,position):
        return self.lista[position]
    def search(self,data):
        support=0

        for i in self.lista[:self.count]:

            if i==data:
                return support
            support+=1
        return -1
    def delete(self,data):
        if not self.empty():
            c=self.search(data)
            if c>=0 or c:
                while(c<self.count-1):
                    self.lista[c]=self.lista[c+1]
                    c+=1
                self.count-=1
    def delete_pos(self,pos):

        if not self.empty():
            while(pos<self.count-1):
                self.lista[pos]=self.lista[pos+1]
                pos+=1
            self.count-=1
    def consulta(self):
        return self.lista[:self.count]

    def sumatoria(self):
        a=0
        for i in self.lista:
            a+=i
        return a
"""
a=list_array(100000)
s=time()
for i in range(100000):
    a.insertar(i)
print(time()-s)

s=time()
for i in range(100000):
    print(i)
    a.delete(str(np.random.randint(0,100000)))
print(time()-s)


"""


